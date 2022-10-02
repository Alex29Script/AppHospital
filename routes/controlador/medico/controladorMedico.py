from pickle import NONE
import sqlite3

from routes.controlador.conexion.conexion import Conexion

class superMedico():

    def obtenerCitasMedico(self,idmedico):
        try:
            conn=sqlite3.connect(Conexion.url)
            cur=conn.cursor()
            data=(idmedico,)
            cur.execute("""
                        SELECT t1.idcitas, t1.fechayhora, t1.idpacientes, t2.nombres, t2.apellidos
                        FROM Citas AS t1
                        INNER JOIN persona AS t2
                        ON t1.idpacientes=t2.idusuario
                        WHERE t1.idmedicos=?
                        """,data)
            citasMedico=cur.fetchall()
            if citasMedico is not NONE:
                return citasMedico
            else:
                citasMedico2=(0,"1900-01-01T01:00",0,"sin pacientes","sin pacientes")
                return citasMedico2
        except:
            print("Error en obtenerCitasMedico-controlador Medico ")
            citasMedico2=(0,"1900-01-01T01:00",0,"sin pacientes","sin pacientes")
            return citasMedico2
        finally:
            cur.close()
            conn.close()
