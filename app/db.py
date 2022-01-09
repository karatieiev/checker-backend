import psycopg2
import json
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    dbname='ddfcjsqnp2k2fm',
    user='kekcwokcpwjykc',
    password='a832412499adad830b261458744deca09aba3da5408aa99e937f483639393dc9',
    host='ec2-54-220-223-3.eu-west-1.compute.amazonaws.com'
)
cursor = conn.cursor(cursor_factory=RealDictCursor)


def get_employees():
    cursor.execute('SELECT * FROM employees')
    return json.dumps(cursor.fetchall())

