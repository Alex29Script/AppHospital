import sqlite3

from routes.controlador.conexion.conexion import Conexion
from routes.controlador.general.moduloAuxiliar import Auxiliar


class superControlador:
    def tablaPaciente(self):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT idusuario,nombres,apellidos FROM persona JOIN user USING (idusuario) WHERE user.tipousuario="paciente"')
            todos_pacientes=cursor.fetchall()
            if todos_pacientes is not None:
                for paciente in todos_pacientes:
                    print(paciente)
                return todos_pacientes   
            else:
                return "vacio"  
        except:
            return "error en el controlador SuperU"
        finally:
            cursor.close()
            conexion.close()
    
    def tablaMedico(self):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT idusuario,nombres,apellidos FROM persona JOIN user USING (idusuario) WHERE user.tipousuario="medico"')
            todos_medicos=cursor.fetchall()
            if todos_medicos is not None:
                for medico in todos_medicos:
                    print(medico)
                return todos_medicos
            else:
                return "vacio"       
        except:
            return "error en el controlador tablaMedico-superUsurio"
        finally:
            cursor.close()
            conexion.close()
            
    def tablaCitas(self):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT idcitas,idhistoriaclinica,idpacientes,idmedicos,fechayhora FROM Citas')
            todas_citas=cursor.fetchall()
            if todas_citas is not None:
                todas_citas= Auxiliar.obtenerHCnombre(todas_citas,Conexion.url)
                for cita in todas_citas:
                    print(cita)
                return todas_citas   
            else:
                return "vacio"
            
        except:
            return "error en el controlador -funcion tablaCitas-superUsurio"
        finally:
            cursor.close()
            conexion.close()
    
    def tablaHS(self):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT idhistoriaclinica,idcitas,idpacientes,idmedicos,diagnostico FROM Historiaclinica')
            todas_HS=cursor.fetchall()
            if todas_HS is not None:
                todas_HS=Auxiliar.obtenerHCnombre(todas_HS,Conexion.url)
                for hs in todas_HS:
                    print(hs)
                return todas_HS
            else:
                return "vacio"

        except:
            return "error en el controlador -funcion tablaCitas-superUsurio"
        finally:
            cursor.close()
            conexion.close()
    
    
    


