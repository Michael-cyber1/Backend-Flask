from flask import Blueprint, render_template, current_app, request
from sql_provider import SQL_Provider
import os
from database import work_with_db
import access

user_app = Blueprint('user_app', __name__, template_folder='templates')
provider = SQL_Provider('sql/')


@user_app.route('/')
@access.login_permission_required
def user_index():
    return render_template('menu.html')


@user_app.route('/sql1', methods=['GET', 'POST'])
def user_sql1():
    if request.method == 'GET':
        return render_template('user_input.html')
    else:
        value = request.form.get('value', None)
        if value is not None:
            sql = provider.get('sql1.sql', gener=value)
            result = work_with_db(current_app.config['dbconfig'], sql)
            if not result:
                return 'Not found'
            return render_template("out.html", name="boxes", items=result)
        else:
            return 'Not found value'
