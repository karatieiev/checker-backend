import app.db as db
from flask import Flask
from flask import request


app = Flask(__name__, instance_relative_config=True)


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
