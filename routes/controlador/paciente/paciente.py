from routes.modelos.clases import Citas, Historiaclinica


class pacienteControlador:

    def AsignarCitas(self):
        try:
            conexion=Citas.connect(conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT * FROM Citas WHERE citas.idcitas')
            todas_citas=cursor.fetchall()
            if todas_citas is not None:
                todas_citas= "idcitas"(todas_citas,conexion.url)
                for cita in todas_citas:
                    print(cita)
                return todas_citas   
            else:
                return "vacio"
            
        except:
            return "error en el controlador -funcion tablaCitas-paciente"
        finally:
            cursor.close()
            conexion.close()
    
    def ConsultarCitas(self,id):
        try:
            conexion=Citas.connect(conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT * FROM citas JOIN user USING (idpaciente) WHERE citas.idcitas=%s' %id)
            consultarCita=cursor.fetchone()
            if consultarCita is not None:
                return consultarCita
            else: return ("vacio")
        except:
            print("usuario no encontrado o errores en buscarCitas-citas")
        finally:
            cursor.close()
            conexion.close()

    def tablaHistoriaclinica(self):
    
        try:
            conexion=Historiaclinica.connect(conexion.url)
            cursor=conexion.cursor()
            cursor.execute('SELECT idhistoriaclinica,idcitas,idpacientes,idmedicos,diagnostico FROM Historiaclinica')
            todas_HS=cursor.fetchall()
            if todas_Historiaclinica is not None:
                todas_Historiaclinica="Historiaclinica"(todas_Historiaclinica,conexion.url)
                for hs in todas_Historiaclinica:
                    print(Historiaclinica)
                return todas_Historiaclinica
            else:
                return "vacio"

        except:
            return "error en el controlador -funcion tablaCitas"
        finally:
            cursor.close()
            conexion.close()
    