# db_util.py

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
    
    cursor = con.cursor(dictionary=True)
    return (con, cursor)


def close(connection = None, cursor = None):
    if cursor != None:
        cursor.close()
    if connection != None:
        connection.close()
