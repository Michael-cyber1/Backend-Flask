from flask import Blueprint, render_template, current_app, request, session, redirect
from sql_provider import SQL_Provider
from database import work_with_db, db_update
from .basket_session import add_to_basket, clear_basket

basket_app = Blueprint('basket_app', __name__, template_folder='templates')
provider = SQL_Provider('sql/')


@basket_app.route('/', methods=['GET', 'POST'])
def basket():
    if request.method == 'GET':
        current_basket = session.get('basket', [])
        sql = provider.get('order_list.sql')
        items = work_with_db(current_app.config['dbconfig'], sql)
        return render_template("basket_order_list.html", items=items, basket=current_basket)
    else:
        item_id = request.form['item_id']
        print(item_id)
        sql = provider.get('order_items.sql', idorder_list=item_id)
        items = work_with_db(current_app.config['dbconfig'], sql)
        add_to_basket(items)
        return redirect('/basket')


@basket_app.route('/todo')
def todo_basket_handler():
    return redirect('/basket')


@basket_app.route('/clear')
def clear_basket_handler():
    clear_basket()
    return redirect('/basket')