from routes.controlador.conexion.conexion import Conexion
import sqlite3

class pacienteControlador:
    def llamarMedicos(self):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            cursor.execute("""
                            SELECT persona.idusuario, persona.nombres,persona.apellidos, persona.especialidad
                            FROM User
                            INNER JOIN persona
                            ON User.idusuario= persona.idusuario
                            WHERE User.tipousuario="medico"
                            """)
            Medicos=cursor.fetchall()
            for medico in Medicos:
                print(medico)
            return Medicos
        except:
                print(" este es un error al consultar los medicos")
        finally:
            cursor.close()
            conexion.close()
        
    def PacienteTomarCita(self,info={}):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            data=(info["idpaciente"],info["idmedico"],info["fecha"])
            cursor.execute("""
                            INSERT INTO Citas (idpacientes,idmedicos,fechayhora) VALUES (?,?,?)
                            """,data)
            conexion.commit()
        except:
                print(" este es un error al tomar una cita")
        finally:
            cursor.close()
            conexion.close()


    def citasProgramadas(self,info={}):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            data=(info["idpaciente"],)
            cursor.execute("""
                            SELECT t1.idcitas, t1.idhistoriaclinica,t1.fechayhora,t1.idmedicos,t2.nombres,t2.apellidos,t2.especialidad
                            FROM Citas AS t1
                            INNER JOIN persona AS t2
                            ON t2.idusuario=t1.idmedicos
                            WHERE t1.idpacientes=?
                            """,data)
            citas_paciente=cursor.fetchall()
            if citas_paciente is not None:
                return citas_paciente
            else: 
                return ("vacio")
        except:
                print(" este es un error al consultar citasProgramadas  Controlador Paciente")
        finally:
            cursor.close()
            conexion.close()

    def eliminarCitaPaciente(self,info={}):
        try:
            conn=sqlite3.connect(Conexion.url)
            cursor=conn.cursor()
            data=(info["idcita"],info["idpaciente"])
            cursor.execute("DELETE FROM Citas WHERE (idcitas=? AND idpacientes=?)",data)
            conn.commit()
        except:
            print("Error en eliminar cita -controlador Paciente")
        finally:
            cursor.close()
            conn.close()
    
    def modificarCitaPaciente(self,info={}):
        try:
            conn=sqlite3.connect(Conexion.url)
            cursor=conn.cursor()
            data=(info["fecha"],info["idmedico"],info["idcita"],info["idpaciente"])
            cursor.execute("UPDATE Citas SET fechayhora=?,idmedicos=? WHERE (idcitas=? AND idpacientes=?)",data)
            conn.commit()
        except:
            print("Error en modificar cita -controlador Paciente")
        finally:
            cursor.close()
            conn.close()
    
    def citasProgramadasExtedida(self,info={}):
        try:
            conexion=sqlite3.connect(Conexion.url)
            cursor=conexion.cursor()
            data=(info["idpaciente"],)
            cursor.execute("""
                            SELECT t1.idcitas, t1.idhistoriaclinica,t1.fechayhora,t1.idmedicos,t2.nombres,t2.apellidos,t2.especialidad, t3.diagnostico,t1.puntaje
                            FROM Citas AS t1
                            INNER JOIN persona AS t2
                            ON t2.idusuario=t1.idmedicos
                            INNER JOIN Historiaclinica AS t3
                            ON t1.idcitas=t3.idcitas
                            WHERE t1.idpacientes=?
                            """,data)
            citas_paciente=cursor.fetchall()
            if citas_paciente is not None:
                return citas_paciente
            else: 
                return ("vacio")
        except:
                print(" este es un error al consultar citasProgramadas  Controlador Paciente")
        finally:
            cursor.close()
            conexion.close()
