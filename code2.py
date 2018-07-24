#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
import mysql.connector
from mysql.connector import MySQLConnection, Error
import json

 

app = Flask(__name__)

def getter():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='employees',
                                       user='root',
                                       password='welcome')
        cursor = conn.cursor()
        if conn.is_connected():
            cursor.execute("SELECT * FROM users")
            row = cursor.fetchall()
            cursor.close()
        
    except Error as e:
        print(e)
 
    finally:
        conn.close()
    return (row)    

def setter():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='employees',
                                       user='root',
                                       password='welcome')
        cursor = conn.cursor()
        if conn.is_connected():
            cursor.execute("SELECT * FROM users")
            row = cursor.fetchall()
            cursor.close()
        
    except Error as e:
        print(e)
 
    finally:
        conn.close()
    return (row)    

@app.route('/', methods=['GET'])
def get():

    if request.method == "GET":
        row = getter()
    return (json.dumps(str(row)))

@app.route('/POST', methods=['POST'])
def post():
    if request.method == "POST":
        print('GET RECIBIDO')
        datos=request.get_json()
        name=datos["name"]
        load()
        return ("POST")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
