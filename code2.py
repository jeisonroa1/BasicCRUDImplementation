#!/usr/bin/python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------
#Se importan librerias
from flask import Flask, request
import mysql.connector
from mysql.connector import MySQLConnection, Error
import json

app = Flask(__name__)
#-------------------------------------------------------------------------------------------------
#Metodos especificos
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
    return (row)    

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

def postf(data):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='employees',
                                       user='root',
                                       password='welcome')
        cursor = conn.cursor()
        if conn.is_connected():
            query ="UPDATE employees.users SET Age=Age+1 WHERE Name='%s'" % (data["Name"]) 
            cursor.execute(query)
            conn.commit()
            cursor.close()
        
    except Error as e:
        print(e)
 
    finally:
        conn.close()

def deletef(data):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='employees',
                                       user='root',
                                       password='welcome')
        cursor = conn.cursor()
        if conn.is_connected():
            query = "DELETE FROM employees.users WHERE Name='%s'" % (data["Name"])  
            cursor.execute(query)
            conn.commit()
            cursor.close()
        
    except Error as e:
        print(e)
 
    finally:
        conn.close()



#----------------------------------------------------------------------------------------------
#Metodos de Flask
@app.route('/', methods=['GET'])
def get():

    if request.method == "GET":
        row = getf()
    return ("Se han mostrado todos los registros"+json.dumps(str(row)))

@app.route('/PUT', methods=['PUT'])
def put():
    if request.method == "PUT":
        data=request.get_json()
        putf(data)
        return ("Se ha añadido a"+data["Name"])

@app.route('/POST', methods=['POST'])
def post():
    if request.method == "POST":
        data=request.get_json()
        print(data)
        postf(data)
        return ("Se ha actualizado a"+data["Name"])

@app.route('/DELETE', methods=['DELETE'])
def delete():
    if request.method == "DELETE":
        data=request.get_json()
        deletef(data)
        return ("Se ha eliminado "+data["Name"])
#----------------------------------------------------------------------------------------------
#Main Principal
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

