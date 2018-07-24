#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
import mysql.connector
from mysql.connector import MySQLConnection, Error
import json

 

app = Flask(__name__)

def getf():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='employees',
                                       user='root',
                                       password='welcome')
        cursor = conn.cursor()
        if conn.is_connected():
            query = "SELECT * FROM users"
            cursor.execute(query)
            row = cursor.fetchall()
            cursor.close()
        
    except Error as e:
        print(e)
 
    finally:
        conn.close()
    return ("Se han mostrado todos los registros")    

def putf(data):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='employees',
                                       user='root',
                                       password='welcome')
        cursor = conn.cursor()
        if conn.is_connected():
            query ="INSERT INTO employees.users(Name,LastName,Age,Profession,Area,Email,Phone,Address,City,Country,MaritalState) VALUES ('%s', '%s',%d,'%s','%s','%s',%d,'%s','%s','%s','%s')" % (data["Name"],data["LastName"],int(data["Age"]),data["Profession"],data["Area"],data["Email"],int(data["Phone"]),data["Address"],data["City"],data["Country"],data["MaritalState"]) 
            cursor.execute(query)
            conn.commit()
            cursor.close()
        
    except Error as e:
        print(e)
 
    finally:
        conn.close()
    return ("Se ha añadido a"+data["Name"])    





@app.route('/', methods=['GET'])
def get():

    if request.method == "GET":
        row = getf()
    return (json.dumps(str(row)))

@app.route('/PUT', methods=['PUT'])
def put():
    if request.method == "PUT":
        data=request.get_json()
        putf(data)
        return ("PUT")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
