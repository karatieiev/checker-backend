from flask import Flask

# create and configure the app
from app.persist_manager import PersistManager

app = Flask(__name__, instance_relative_config=True)


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/create')
def create():
    # PersistManager.init(app.config)
    return 'file has been created'


@app.route('/read')
def read():
    my_file = open("BabyFile.txt", "r")
    file_content = my_file.read()
    my_file.close()
    return file_content
