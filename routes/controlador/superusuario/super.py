from pickle import NONE
import sqlite3
import string

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
            cursor.execute('SELECT idusuario,nombres,apellidos,especialidad FROM persona JOIN user USING (idusuario) WHERE user.tipousuario="medico"')
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
            cursor.execute("""
                            SELECT t1.idcitas,t1.fechayhora as fecha,t1.idpacientes, t2.nombres,t2.apellidos,t1.idmedicos,t3.nombres AS nombre_medico,t3.apellidos AS apellido_medico
                            FROM Citas AS t1
                            INNER JOIN persona AS t2
                            ON t1.idpacientes = t2.idusuario
                            INNER JOIN persona AS t3
                            ON t1.idmedicos = t3.idusuario
                            """)
            todas_citas=cursor.fetchall()
            if todas_citas is not None:
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
            cursor.execute(""" 
                            SELECT t1.idhistoriaclinica, t1.idcitas, t1.idpacientes,t2.nombres,t2.apellidos,t1.idmedicos,t3.nombres,t3.apellidos, t1.diagnostico
                            FROM Historiaclinica AS t1
                            INNER JOIN persona AS t2
                            ON t1.idpacientes=t2.idusuario
                            INNER JOIN persona AS t3
                            ON t1.idmedicos=t3.idusuario
                            """)
            todas_HS=cursor.fetchall()
            if todas_HS is not None:
                for hs in todas_HS:
                    print(hs)
                return todas_HS
            else:
                return "vacio"

        except:
            return "error en el controlador -funcion HistoriaClinica-superUsurio"
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
    
    def eliminarMedico(self,id):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute("DELETE FROM User WHERE (idusuario=%s AND tipousuario='medico')" %id)
            conexion.commit()
        except:
            print("usuario no encontrado o errores en eliminarMedico-superUsurio")
        finally:
            cursor.close()
            conexion.close()

    def crearMedico(self,dicMedico={}):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            datosUser=(dicMedico['id'], dicMedico['pass'] ,"medico")
            cursor.execute("INSERT INTO User (idusuario,contrasena,tipousuario) VALUES (?,?,?)",datosUser)
            conexion.commit()
        except:
            print("usuario no encontrado o errores en crearMedico-superUsurio parte1")
        finally:
            cursor.close()
            conexion.close()
        
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            datos=(dicMedico['id'],dicMedico['nombre'],dicMedico['apellido'],dicMedico['bird'],dicMedico['sexo'],dicMedico['escivil'],dicMedico['job'],dicMedico['tel'],dicMedico['direccion'],dicMedico['tp'],dicMedico['rh'],dicMedico['especialidad'],dicMedico['email'])
            cursor.execute('INSERT INTO persona (idusuario,nombres,apellidos,fechanacimiento,genero,estadocivil,ocupacion,telefono,direccion,tp,rh,especialidad,email) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', datos )
            conexion.commit()        
        except:
            print("usuario no encontrado o errores en crearMedico-superUsurio parte2")
        finally:
            cursor.close()
            conexion.close()
        
    def eliminarCita(self,id):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute("DELETE FROM Citas WHERE idcitas=%s" %id)
            conexion.commit()
        except:
            print("erro al eliminarCita-superUsurio")
        finally:
            cursor.close()
            conexion.close()
    
    def buscarCita(self,id):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute("""
                            SELECT t1.idcitas,t1.fechayhora as fecha, t1.puntaje,t1.comentarios,t1.idpacientes, t2.nombres,t2.apellidos,t1.idmedicos,t3.nombres AS nombre_medico,t3.apellidos AS apellido_medico
                            FROM Citas AS t1
                            INNER JOIN persona AS t2
                            ON t1.idpacientes = t2.idusuario
                            INNER JOIN persona AS t3
                            ON t1.idmedicos = t3.idusuario
                            WHERE idcitas=%s
                            """ %id)
            cita=cursor.fetchone()
            if cita is not NONE:
                print(cita)
                return cita
            else:
                return "vacio"
        except:
            print("error al buscarCita - superUsurio")
            return "vacio"
        finally:
            cursor.close()
            conexion.close()
    
    def actualizarCita(self,cita={}):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            data=(cita["id"],cita["fecha"],cita["puntaje"],cita["comentarios"],cita["idpaciente"],cita["idmedico"],cita["id"])
            cursor.execute("UPDATE Citas SET idcitas=?,fechayhora=?,puntaje=?,comentarios=?,idpacientes=?,idmedicos=? WHERE idcitas=?", data)
            conexion.commit()
            #comprobar si la cita tiene una historia asociada
            data2=(cita["id"])
            cursor.execute("SELECT idhistoriaclinica FROM Historiaclinica WHERE idcitas=?", data2)
            
            citaAsociada=cursor.fetchone()
            print("###### esta es una cita asociada:",citaAsociada,"campo",citaAsociada[0])
            if citaAsociada is not None:
                data3=(cita["idpaciente"],cita["idmedico"],citaAsociada[0])
                cursor.execute('UPDATE Historiaclinica SET idpacientes=?,idmedicos=? WHERE idhistoriaclinica=?', data3)
                conexion.commit()
            else:
                print("Sin Cambios..................................")
        except:
            print("error al actualizarCita - superUsurio")
            return "vacio"
        finally:
            cursor.close()
            conexion.close()
    
    def crearCita(self,cita={}):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            data=(cita["idmedico"],cita["idpaciente"],cita["fecha"])
            cursor.execute("INSERT INTO Citas (idmedicos,idpacientes,fechayhora) VALUES (?,?,?)", data)
            conexion.commit()    
        except:
            print("error al crear una cita - superUsurio")

        finally:
            cursor.close()
            conexion.close()

    def buscarinfoHC(self,citas=(),id=string):
        for cita in citas:
            if int(cita[0])==int(id):
                infoHC=(cita[0],cita[2],cita[5])
                return infoHC


    def crearHC(self, hc={}):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            data=(hc["idpaciente"],hc["idmedico"],hc["idcita"],hc["diagnostico"],hc["tratamiento"])
                    #idpacientes,idmedicos,idcitas,diagnostico,tratamiento
            cursor.execute("INSERT INTO Historiaclinica (idpacientes,idmedicos,idcitas,diagnostico,tratamiento) VALUES (?,?,?,?,?)", data)
            conexion.commit()
            cursor.execute("SELECT idhistoriaclinica From Historiaclinica WHERE idcitas=%s" %hc["idcita"])
            HCEncontrada=cursor.fetchone()
            print("acaaaa---------",HCEncontrada)
            if HCEncontrada is not NONE:
                data2=(HCEncontrada[0],hc["idcita"])
                cursor.execute("UPDATE Citas SET idhistoriaclinica=? WHERE idcitas=?", data2)
                conexion.commit()
        except:
            print("error al crear una HistoriaClinica - superUsurio")
        finally:
            cursor.close()
            conexion.close()
    
    def buscarHistClinica(self,id):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT * FROM Historiaclinica WHERE idhistoriaclinica=%s' %id)
            historiaC=cursor.fetchone()
            if historiaC is not NONE:
                print("esta es la HC:",historiaC)
                return historiaC
        except:
            print("error al consultar una HistoriaClinica - superUsurio")
        finally:
            cursor.close()
            conexion.close()

    def actualizarHC(self,hc={}):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            data=(hc["idpaciente"],hc["idmedico"],hc["diagnostico"],hc["tratamiento"],hc["idHC"])
            cursor.execute('UPDATE Historiaclinica SET idpacientes=?,idmedicos=?,diagnostico=?,tratamiento=? WHERE idhistoriaclinica=?', data)
            conexion.commit()
            data2=(hc["idpaciente"],hc["idmedico"],hc["idcita"])
            cursor.execute('UPDATE Citas SET idpacientes=?,idmedicos=? WHERE idcitas=?', data2)
            conexion.commit()
            
        except:
            print("error al acutalizar una HistoriaClinica - superUsurio")
        finally:
            cursor.close()
            conexion.close()
    
    def eliminarHC(self,id):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            data=(id)
            cursor.execute('DELETE FROM Historiaclinica WHERE idhistoriaclinica=?', data)
            conexion.commit()
            
        except:
            print("error al  eliminar HC - superUsurio")
        finally:
            cursor.close()
            conexion.close()
