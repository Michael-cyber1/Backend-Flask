from flask import Blueprint, request, render_template, current_app
from sql_provider import SQL_Provider
from access import login_permission_required
from database import db_update, work_with_db


edit_app = Blueprint('edit', __name__, template_folder='templates')
provider = SQL_Provider('sql/')


@edit_app.route('/', methods=['GET', 'POST'])
@login_permission_required
def edit_foo():
    db_config = current_app.config['dbconfig']
    if request.method == 'POST':
        id_z = request.form.get('id_z', None)
        if id_z is not None:
            sql = provider.get('delete.sql', gen1=id_z)
            db_update(db_config, sql)
    sql = provider.get('list.sql')
    result = work_with_db(db_config, sql)
    return render_template('edit.html', items=result)


@edit_app.route('/insert', methods=['GET', 'POST'])
@login_permission_required
def insert_foo():
    if request.method == 'GET':
        return render_template('insert.html', forma=True)
    else:
        date_z = request.form.get('date_z', None)
        contact = request.form.get('contact', None)
        total_v= request.form.get('total_v', None)
        if date_z is not None and contact is not None and total_v is not None:
            db_config = current_app.config['dbconfig']
            sql = provider.get('insert.sql', gen1=date_z, gen2=contact, gen3=total_v)
            db_update(db_config, sql)
        return edit_foo()
