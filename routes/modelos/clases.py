# Se crea la clase User
class User: 

    # atributos de la clase User
    idusuario= ' '
    contraseña = ' '
    tipousuario = ' '
    
    # constructor de la clase User
    def __init__(self, idusuario, contraseña, tipousuario):
        
        self.idusuario = idusuario
        self.contraseña = contraseña
        self.tipousuario = tipousuario

    
    # Se crea la clase persona
class Persona(User): 
    def __init__(self, idusuario, contraseña, tipousuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh):

    # constructor de la clase persona
        User.__init__(self, idusuario, contraseña, tipousuario)

    # atributos de la instancia de la clase persona
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechanacimiento=fechanacimiento
        self.genero=genero
        self.generoestadocivil = estadocivil
        self.ocupacion = ocupacion
        self.telefono = telefono
        self.direccion = direccion
        self.EPS = EPS
        self.discapacidad = discapacidad
        self.rh = rh
    
    # metodos de la clase persona

"""     def consultar_persona(self):
        print("{idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

    def modificar_persona(self):
        print("Modificacion exitosa: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

    def agregar_persona(self):
        print("Se agrego exitosamente: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")
 """
# Se crea la clase medico
class Medico(Persona): 
    def __init__(self, idusuario, idmedico, contraseña, tipousuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh, tarjetaprofesional, especialidad):

    # constructor de la clase medico
        Persona.__init__(self,idusuario,contraseña,tipousuario,nombres,apellidos,fechanacimiento,genero,estadocivil,ocupacion,telefono,direccion,EPS,discapacidad,rh)

    # atributos de la instancia de la clase medico
        self.idmedico = idmedico
        self.tarjetaprofesional = tarjetaprofesional
        self.especialidad = especialidad
    
"""     # metodos de la clase medico
    def consultar_medico(self):
        print("{idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

    def modificar_medico(self):
        print("Modificacion exitosa: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

    def agregar_medico(self):
        print("Se agrego exitosamente: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")
 """
# Se crea la clase paciente
class Paciente(Persona): 

    # constructor de la clase paciente
    def __init__(self, idusuario, idpaciente, contraseña, tipousuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh):

        Persona.__init__(self,idusuario,contraseña,tipousuario,nombres,apellidos,fechanacimiento,genero,estadocivil,ocupacion,telefono,direccion,EPS,discapacidad,rh)
        self.idpaciente = idpaciente
    # metodos de la clase paciente
"""    def consultar_paciente(self):
        print("{idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}")

    def modificar_paciente(self):
        print("Modificacion exitosa: ")

    def agregar_paciente(self):
        print("Se agrego exitosamente: ")
 """
class Citas(Paciente, Medico): # clase citas

    def __init__(self, idusuario, idpaciente, contraseña, tipousuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh,idmedico,tarjetaprofesional, especialidad,idcita,fechayhora,calificacion):
    # constructor de la clase citas
    
        Paciente.__init__(self,idusuario,idpaciente,contraseña,tipousuario,nombres,apellidos,fechanacimiento,genero,estadocivil,ocupacion,telefono,direccion,EPS,discapacidad,rh)
        Medico.__init__(self,self, idusuario, idmedico, contraseña, tipousuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh, tarjetaprofesional, especialidad)

    # atributos de la instancia de la clase citas
        self.idcita = idcita
        self.fechayhora = fechayhora
        self.calificacion = calificacion
    
    # metodos de la clase citas
"""   def consultar_citas(self):
        print("Tiene cita con: {idmedicos}, {fechayhora}")

    def modificar_citas(self):
        print("Modificacion exitosa:  {idmedicos}, {fechayhora}")

    def cancelar_citas(self):
        print("Cita cancelada")

    def calificar_citas(self):
        print(" ")
 """

# se crea clase Historiaclinica
class Historiaclinica (Citas,Medico): 

    def __init__(self, idusuario, idpaciente, idhistoriaclinica,contraseña, tipousuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh,idmedico,tarjetaprofesional, especialidad,idcita,fechayhora,calificacion, diagnostico, tratamiento):

    # constructor de la clase Historiaclinica
        Medico.__init__(self,self, idusuario, idmedico, contraseña, tipousuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh, tarjetaprofesional, especialidad)
        Citas.__init__(self, idusuario, idpaciente, contraseña, tipousuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh,idmedico,tarjetaprofesional, especialidad,idcita,fechayhora,calificacion)

    # atributos de la instancia de la clase Historiaclinica
        self.idhistoriaclinica = idhistoriaclinica
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        
    
"""  # metodos de la clase Historiaclinica
    def consultar_historiaclinica(self):
        print("Imprimir: {idpacientes}, {idmedicos}, {idcitas}, {diagnostico}, {tratamiento}")
 """
clase_usuario=User(1234,9876,Medico)
clase_usuario=User(4567,9876,Paciente)


User = list()
Persona=list()
Medico=list()
Paciente=list()
Citas=list()
Historiaclinica=list()

print("este es el id: "[Medico[0].idusuario],"este la contraseña:" [Medico[0].contraseña],"esta tipo:"[Medico[0].tipousuario])

