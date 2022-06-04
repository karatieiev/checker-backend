import psycopg2
import json
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    dbname='d1q47tkodnglqg',
    user='peqkgwcvqmdgdr',
    password='b84df18e3fa54a74cd47d72da3366afc73442a25d782da280be9cc051cc8f9b3',
    host='ec2-54-171-25-232.eu-west-1.compute.amazonaws.com'
)
cursor = conn.cursor(cursor_factory=RealDictCursor)


def get_employees():
    cursor.execute('SELECT * FROM employees')
    return json.dumps(cursor.fetchall())


def get_employee(_id):
    cursor.execute('SELECT * FROM employees WHERE id = {}'.format(_id))
    return json.dumps(cursor.fetchall())


def delete_employee(_id):
    cursor.execute('DELETE FROM employees WHERE id = {}'.format(_id))
    conn.commit()
    return ''


def post_employee(_json):
    cursor.execute(
        'INSERT INTO employees(name, photo) VALUES(\'{}\', \'{}\')'.format(
            _json['name'], _json['photo']
        )
    )
    conn.commit()
    return ''


def put_employee(_id, _json):
    cursor.execute(
        'UPDATE employees SET name = \'{}\', photo = \'{}\' WHERE id = {}'.format(
            _json['name'], _json['photo'], _id
        )
    )
    conn.commit()
    return ''


def get_employee_photo_base64(_id):
    cursor.execute('SELECT * FROM employees WHERE id = {}'.format(_id))
    return cursor.fetchone()
