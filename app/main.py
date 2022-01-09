import app.db as db
from flask import Flask


app = Flask(__name__, instance_relative_config=True)


@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/employees', methods=['GET'])
def employees():
    return db.get_employees()


@app.route('/employees/<employee_id>')
def employee(employee_id):
    return db.get_employee(employee_id)
