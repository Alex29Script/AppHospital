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
    
    def eliminarPaciente(self,id):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute("DELETE FROM User WHERE (idusuario=%s AND tipousuario='paciente')" %id)
            conexion.commit()
            cursor.execute("DELETE FROM persona WHERE idusuario=%s" %id)
            conexion.commit()
            cursor.execute("DELETE FROM Historiaclinica WHERE idpacientes=%s" %id)
            conexion.commit()
            cursor.execute("DELETE FROM Citas WHERE idpacientes=%s" %id)
            conexion.commit()
            print("usuario eliminado")

        except:
            print("usuario no encontrado o errores en eliminarPaciente-superUsurio")
        
        finally:
            cursor.close()
            conexion.close()
    
    def buscarPaciente(self,id):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT * FROM persona JOIN user USING (idusuario) WHERE persona.idusuario=%s' %id)
            busquedaPaciente=cursor.fetchone()
            if busquedaPaciente is not None:
                return busquedaPaciente
            else: return ("vacio")
        except:
            print("usuario no encontrado o errores en buscarPaciente-superUsurio")
        finally:
            cursor.close()
            conexion.close()

    def actualizarPaciente(self,infopaciente=list()):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            datos=(infopaciente[0], infopaciente[1], infopaciente[2], infopaciente[3], infopaciente[4], infopaciente[5], infopaciente[6], infopaciente[7],infopaciente[8],infopaciente[9],infopaciente[10],infopaciente[11],infopaciente[12],infopaciente[0])
            cursor.execute('UPDATE persona SET  idusuario=?,nombres=?,apellidos=?,fechanacimiento=?,genero=?,estadocivil=?,ocupacion=?,telefono=?,direccion=?,discapacidad=?,rh=?,eps=?,email=? WHERE idusuario=?', datos )
            conexion.commit()
        except:
            print("usuario no encontrado o errores en actualizarPaciente-superUsurio")
        finally:
            cursor.close()
            conexion.close()
    
    def crearnuevopaciente(self,infopaciente=list()):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            #  0 cc      1          2           3           4           5           6           7               8                   9         10      11        12                      13
            #['8888', 'Alfonso', 'Lopez', '12/20/2002', 'femenino', 'solter@', 'ingeniero', '3005005050', 'Direccion Cr50', 'discapacitado', 'ab+', 'EPS', 'alfonso@hotmail.com', 'contraseña']
            datosUser=(infopaciente[0], infopaciente[13] ,"paciente")
            cursor.execute("INSERT INTO User (idusuario,contrasena,tipousuario) VALUES (?,?,?)",datosUser)
            conexion.commit()
        except:
            print("error añadir paciente 1")
        finally:
            cursor.close()
            conexion.close()
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            #  0 cc      1          2           3           4           5           6           7               8                   9         10      11        12                      13
            #['8888', 'Alfonso', 'Lopez', '12/20/2002', 'femenino', 'solter@', 'ingeniero', '3005005050', 'Direccion Cr50', 'discapacitado', 'ab+', 'EPS', 'alfonso@hotmail.com', 'contraseña']
            datosUser=(infopaciente[0], infopaciente[1], infopaciente[2], infopaciente[3], infopaciente[4], infopaciente[5], infopaciente[6], infopaciente[7],infopaciente[8],infopaciente[9],infopaciente[10],infopaciente[11],infopaciente[12])
            cursor.execute("INSERT INTO persona (idusuario,nombres,apellidos,fechanacimiento,genero,estadocivil,ocupacion,telefono,direccion,discapacidad,rh,eps,email) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",datosUser)
            conexion.commit()
        except:
            print("error añadir paciente 2")
        finally:
            cursor.close()
            conexion.close()
    
    def buscarMedico(self,id):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT * FROM persona JOIN user USING (idusuario) WHERE persona.idusuario=%s' %id)
            busquedaMedico=cursor.fetchone()
            if busquedaMedico is not None:
                return busquedaMedico
            else: return ("vacio")
        except:
            print("usuario no encontrado o errores en buscarPaciente-superUsurio")
        finally:
            cursor.close()
            conexion.close()
    
    def actualizarMedico(self,infopaciente=list()):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            #       ['467'0, 'Esebio'1, 'Sanchez'2, '123'3, 'Cirujano'4, '88888888'5, 'ninguno@hotmial.com'6, '28/09/2022'7, 'Masculino'8, 'solter@'9, 'Cr80#23'10, 'sin discapacidad'11, 'Medico'12, 'a+'13]
            datos=(infopaciente[0], infopaciente[1], infopaciente[2], infopaciente[7], infopaciente[8], infopaciente[9], infopaciente[12], infopaciente[5],infopaciente[10],infopaciente[11],infopaciente[13],infopaciente[4],infopaciente[6],infopaciente[0])
            cursor.execute('UPDATE persona SET  idusuario=?,nombres=?,apellidos=?,fechanacimiento=?,genero=?,estadocivil=?,ocupacion=?,telefono=?,direccion=?,tp=?,rh=?,especialidad=?,email=? WHERE idusuario=?', datos )
            conexion.commit()
        except:
            print("usuario no encontrado o errores en actualizarPaciente-superUsurio")
        finally:
            cursor.close()
            conexion.close()
