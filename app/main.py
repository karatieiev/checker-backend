import app.db as db
import app.bl as bl
from flask import Flask
from flask import request
from flask import render_template, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__
            , instance_relative_config=True
            , static_folder='../web/static/js'
            , template_folder='../web'
            , static_url_path=''
            )
CORS(app)


@app.route('/')
@app.route('/web/employees')
def serve():
    return render_template('index.html')


@app.route('/static/js/<file>')
def serve_js(file):
    return send_from_directory('../web/static/js', file)


@app.route('/static/css/<file>')
def serve_css(file):
    return send_from_directory('../web/static/css', file)


@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('../web', 'manifest.json')


@app.route('/logo192.png')
@app.route('/favicon.ico')
def serve_logo():
    return send_from_directory('../web', 'favicon.ico')


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
