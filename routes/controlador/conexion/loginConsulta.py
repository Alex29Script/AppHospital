import sqlite3
from routes.controlador.conexion.conexion import Conexion
from werkzeug.security import check_password_hash as checkph

class loginConsultaDB():
    login=False

    def __init__(self):
        self.login=self.login

    def autenticar(self, usuario,contrasena):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute("SELECT * FROM user WHERE idusuario='%s'" %usuario)
            variable = cursor.fetchone()
            #print(variable[1])
            if variable is not None:
                if checkph(variable[1],contrasena)==True:
                    #print(variable[1], contrasena)
                    return True,variable[2]
                else:
                    print("no concuerdan")
                    return False,"ninguno"
            else:
                return False,"ninguno"
        except:
            print("error en la conexion-class login")
            return False,"ninguno"
        finally:
            cursor.close()
            conexion.close()
