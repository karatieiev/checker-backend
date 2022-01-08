import os

from flask import Flask

# create and configure the app
from app.persist_manager import PersistManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
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
    # PersistManager.init(app.config)
    return app.config.get('DATABASE')
    return 'file has been created'


@app.route('/read')
def read():
    my_file = open("BabyFile.txt", "r")
    file_content = my_file.read()
    my_file.close()
    return file_content


f = open("BabyFile.txt", "w+")
f.write('AAAAAAA')
f.close()
