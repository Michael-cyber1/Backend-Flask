from flask import Flask, render_template
import json
from sql_provider import SQL_Provider
from scenario_user.routes import user_app
from scenario_auth.routes import auth_app
from scenario_user.edit import edit_app
from scenario_basket.routes import basket_app

app = Flask(__name__)

app.register_blueprint(user_app, url_prefix='/user')
app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(edit_app, url_prefix='/edit')
app.register_blueprint(basket_app, url_prefix='/basket')

app.config['dbconfig'] = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'password' : '1234',
    'db' : 'proj_sem5'
}
app.config['ACCESS_CONFIG'] = json.load(open('configs/access.json'))
app.config['SECRET_KEY'] = 'super secret key'
provider = SQL_Provider('sql/')


@app.route('/')
def index():
    return render_template("base.html")


if (__name__ == "__main__"):
    app.run(host="127.0.0.1", port=5001)