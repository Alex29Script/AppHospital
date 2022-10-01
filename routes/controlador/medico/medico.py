class medicocControlador:
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
            return "error en el controlador tablaMedico-medico"
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


