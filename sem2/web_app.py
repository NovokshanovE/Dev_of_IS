import datetime

from flask import Flask, render_template, request
from werkzeug.exceptions import abort
from threading import Thread

#from webdriver_manager.chrome import ChromeDriverManager
import datetime

app = Flask(__name__) #если вызывается явно

@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/index', methods=['post', 'get'])
def time_handler():
    return render_template('index.html')

# ...

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)