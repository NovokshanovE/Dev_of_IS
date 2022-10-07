import json

from flask import Flask, render_template, request, url_for
from db_work import select
from blueprint_query.route import blueprint_query
app = Flask(__name__)

app.register_blueprint(blueprint_query, url_prefix='/zaproses')

with open('data_file/db_config.json', 'r') as f:
    db_config = json.load(f)
app.config['dbconfig'] = db_config
'''
site: str = 'form'

db_config = {
    'host': '127.0.0.1',
    'user': 'zhenya',
    'password':'12345',
    'database':'supermarket'
}

@app.route('/')
def index() -> str:
    return "Hello world"

'''
@app.route('/', methods=['GET', 'POST'])
def query():
    return render_template('start_request.html')

@app.route('/exit', methods=['GET','POST'])
def goodbye():
    return 'Goodbye. Return back!'

@app.route('/greeting')
@app.route('/greeting/<name>')
def greeting_handler(name: str = None) -> str:
    if name is None:
        return "Чертила неавторизованная"
    return f'Hello {name}'

'''

@app.route('/index', methods=['GET', 'POST'])
def form_handler(site: str = 'form'):
    print(request.method)
    if(request.method == 'GET'):
        return render_template('form.html')
    elif(request.method == 'POST'):
        login = request.form.get('login')
        password = request.form.get('password')

        return render_template('index.html')


@app.route('/index', methods=['GET', 'POST'])
def index_handler():
    print(request.method)
    if (request.method == 'GET'):
        return render_template('index.html')
    elif (request.method == 'POST'):
        direction = request.form.get('direction')


        return 'direction'


@app.route('/product')
def get_product_all():
    if request.method == 'GET':
        return render_template('index.html')
    sql = "SELECT * FROM product"
    result, schema = select(db_config, sql)
    return str(result)
'''
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)