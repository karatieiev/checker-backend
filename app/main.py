from flask import Flask
from app.db import get_employees


app = Flask(__name__, instance_relative_config=True)


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/employees')
def create():
    return get_employees()

