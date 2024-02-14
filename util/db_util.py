import mysql.connector
from flask import current_app

def get_connection():
    db_config = current_app.config['DB']
    con = mysql.connector.connect(
        host = db_config['host'],
        port = db_config['port'],
        user = db_config['user'], 
        password = db_config['password'], 
        database = db_config['database'],
        charset="utf8")
    # print("=== open DB connection >>>")
    
    cursor = con.cursor(dictionary=True)
    return (con, cursor)


def close(connection = None, cursor = None):
    if cursor != None:
        # print(">>> close cursor ===")
        cursor.close()
    if connection != None:
        # print(">>> close DB connection ===")
        connection.close()


def attr_value(obj, key):
    return '' if obj.get(key) is None else obj.get(key)
