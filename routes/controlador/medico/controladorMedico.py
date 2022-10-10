import sqlite3

from routes.controlador.conexion.conexion import Conexion

class superMedico():

    def obtenerCitasMedico(self,idmedico):
        try:
            conn=sqlite3.connect(Conexion.url)
            cur=conn.cursor()
            data=(idmedico,)
            cur.execute("""
                        SELECT t1.idcitas, t1.fechayhora, t1.idpacientes, t2.nombres, t2.apellidos,t1.idhistoriaclinica
                        FROM Citas AS t1
                        INNER JOIN persona AS t2
                        ON t1.idpacientes=t2.idusuario
                        WHERE t1.idmedicos=?
                        """,data)
            citasMedico=cur.fetchall()
            if citasMedico is not None:
                print("esta es la info de CITA: ",citasMedico)
                return citasMedico
            else:
                citasMedico2=(0,"1900-01-01T01:00",0,"sin pacientes","sin pacientes",999)
                return citasMedico2
        except:
            print("Error en obtenerCitasMedico-controlador Medico")
            citasMedico2=(0,"1900-01-01T01:00",0,"sin pacientes","sin pacientes",999)
            return citasMedico2
        finally:
            cur.close()
            conn.close()

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
                if HCEncontrada is not None:
                    data2=(HCEncontrada[0],hc["idcita"])
                    cursor.execute("UPDATE Citas SET idhistoriaclinica=? WHERE idcitas=?", data2)
                    conexion.commit()
            except:
                print("error al crear una HistoriaClinica - controlador Medico")
            finally:
                cursor.close()
                conexion.close()

    def buscarHistoriaCLinica(self,id):
        try:
            conn=sqlite3.connect(Conexion.url)
            cur=conn.cursor()
            data=(id,)
            cur.execute("""
                        SELECT t1.idhistoriaclinica, t1.idcitas, t4.fechayhora, t1.idpacientes, t2.nombres, t2.apellidos,t1.idmedicos, t3.nombres, t3.apellidos,
                        t4.puntaje,t4.comentarios, t1.diagnostico,t1.tratamiento
                        FROM Historiaclinica AS t1
                        INNER JOIN persona AS t2
                        ON t1.idpacientes=t2.idusuario
                        INNER JOIN persona AS t3
                        ON t1.idmedicos=t3.idusuario
                        INNER JOIN Citas AS t4
                        ON t1.idcitas=t4.idcitas
                        WHERE t1.idhistoriaclinica=?
            """,data)
            infoHistoriaC=cur.fetchone()
            return infoHistoriaC

        except:
            print("Error al buscar una HC desde controlador Medico")
        finally:
            cur.close()
            conn.close()

    def actualizarHC(self,info={}):
        try:
            conn=sqlite3.connect(Conexion.url)
            cur=conn.cursor()
            data=(info["diagnostico"],info["tratamiento"],info["idhistoriacita"])
            cur.execute("""
                        UPDATE Historiaclinica SET diagnostico=?,tratamiento=? WHERE idhistoriaclinica=?
                        """,data)
            conn.commit()

        except:
            print("Error al actualizar una Historia en Controlador Medico")
        finally:
            cur.close()
            conn.close()
