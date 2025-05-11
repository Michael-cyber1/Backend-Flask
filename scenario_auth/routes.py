import os
from flask import Blueprint, render_template, session, request, current_app
from sql_provider import SQL_Provider
from database import  work_with_db

auth_app = Blueprint('auth', __name__, template_folder='templates')
provider = SQL_Provider('./sql')


@auth_app.route('/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login = request.form.get('login', None)
        password = request.form.get('password', None)
        if login is not None and password is not None:
            sql = provider.get('sql_auth.sql', gen1=login, gen2=password)
            result = work_with_db(current_app.config['dbconfig'], sql)
            if not result:
                return 'Invalid login or password'
            session['group_name'] = result[0]['user_group']
            return render_template("base.html", name = result[0]['user_group'])
        else:
            return 'Not found value'
