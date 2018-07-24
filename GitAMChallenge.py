#!/usr/bin/python
import MySQLdb
from flask import Flask, request, json

app = Flask(__name__)
db = MySQLdb.connect(host="localhost",user="root",passwd="welcome",db="sys")
cursor=db.cursor()
#----------------------------------------------------------------------------------------------------------

@app.route('/', methods=['GET'])
def registrar_producto():
    if request.method == "GET":
        sql_command = """SELECT * FROM sys.workers;"""  
        cursor.execute(sql_command)
        results = cursor.fetchall()
        return(json.dumps(str(results)))

#----------------------------------------------------------------------------------------------------------

@app.route('/put', methods=['PUT'])
def insertar_producto():
    if request.method == "PUT":
        data = request.get_json()
        sql_command2 ="INSERT INTO sys.workers(Name,LastName,Age,Profession,Area,Email,Phone,Address,City,Country,MaritalState) VALUES ('%s', '%s',%d,'%s','%s','%s',%d,'%s','%s','%s','%s')" % (data["Name"],data["LastName"],int(data["Age"]),data["Profession"],data["Area"],data["Email"],int(data["Phone"]),data["Address"],data["City"],data["Country"],data["MaritalState"])        
        cursor.execute(sql_command2)
        db.commit()
        return("se ha agregado a "+ data["Name"])

#------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)