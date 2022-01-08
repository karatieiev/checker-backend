import os

from flask import Flask


# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/create')
def create():
    my_file = open("BabyFile.txt", "w+")
    my_file.write("this text is from file")
    my_file.close()
    return 'file has been created'


@app.route('/read')
def read():
    my_file = open("BabyFile.txt", "r")
    file_content = my_file.read()
    return file_content
