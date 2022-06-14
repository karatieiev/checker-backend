import app.db as db
import app.bl as bl
from flask import Flask
from flask import request
from flask import render_template
from flask_cors import CORS
import os


app = Flask(__name__, instance_relative_config=True)
CORS(app)


@app.route('/', methods=['GET'])
def root():
    try:
        return render_template(os.path.join('web', 'index.html'))
    except Exception as e:
        return str(e)


@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'GET':
        return db.get_employees()
    if request.method == 'POST':
        return db.post_employee(request.json)


@app.route('/employees/<employee_id>', methods=['GET', 'PUT', 'DELETE'])
def employee(employee_id):
    if request.method == 'GET':
        return db.get_employee(employee_id)
    if request.method == 'DELETE':
        return db.delete_employee(employee_id)
    if request.method == 'PUT':
        return db.put_employee(employee_id, request.json)


@app.route('/employees/check', methods=['POST'])
def check():
    if request.method == 'POST':
        return bl.check(request.json)


@app.route('/report', methods=['GET'])
def report():
    if request.method == 'GET':
        return db.get_report()

