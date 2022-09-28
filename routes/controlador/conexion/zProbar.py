from inspect import ClassFoundException
from flask import url_for
import sqlite3


#url="{{url_for('db',filename='DBHospitalGeneralBarranquilla.db') }}"
url="F:\Dropbox\Curso MinTIC\Proyectos Python\Clase MinTic\Ciclo 3\Retos\Reto3\AppHospitalGeneralBarranquilla\db\DBHospitalGeneralBarranquilla.db"
url2={url_for('db',filename='DBHospitalGeneralBarranquilla.db')}
print(url)
print(url2)

conexion=sqlite3.connect(url)
cursor=conexion.cursor()
cursor.execute("SELECT * FROM user")
usuarios= cursor.fetchall()
for user in  usuarios:
    print(user)