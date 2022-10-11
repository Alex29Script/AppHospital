from select import select
import sqlite3
import os
#from flask import Flask
#from flask import url_for

class Conexion:
    #url=os.path.abspath(os.path.dirname(__file__))+"\db\DBHospitalGeneralBarranquilla.db"
    url="/app/routes/controlador/conexion/db/DBHospitalGeneralBarranquilla.db"
    #url=url_for('routes',filename='controlador\db\DBHospitalGeneralBarranquilla.db')
    
    def __init__(self):
        self.url=self.url
        

    def tomarDB(self):
            conexion =  sqlite3.connect(self.url)
            print("conexion creada")
            return conexion
        
    
    def crearCursor(self):
        if self.cursor is None:
            self.cursor=self.conexion.cursor()
            print("Cursor Creado")
            return self.cursor
    
    def inicializador(self):
        self.conexion= self.tomarDB()
        self.cursor = self.crearCursor()
        print("conexion y cursor estan ready")
        return self.conexion,self.cursor

"""
#print(Conexion.url)
#print(Conexion.url2)
print(Conexion.url)
conexion =  sqlite3.connect(url_for('routes\controlador\conexion\db\DBHospitalGeneralBarranquilla.db'))
if conexion is None:
    print("error")
else:
    print("conectado")
"""