# Se crea la clase User
class User: 

    # atributos de la clase User
    idusuario= ' '
    contraseña = ' '
    tipousuario = ' '
    
    # constructor de la clase User
    def __init__(self, idusuario, contraseña, tipousuario):
        print(f"consultar_usuario: {idusuario}, {contraseña}, {tipousuario}")

    # atributos de la instancia User
        self.idusuario = idusuario
        self.contraseña = contraseña
        self.tipousuario = tipousuario
    
    # metodos de la clase User
    def consultar_usuario(self):
        print("Su Login es: {tipousuario}")

class Citas: # clase citas

    # atributos de la clase citas
    idcitas = ' ' 
    idpacientes = ' '
    idmedicos = ' '
    idhistoriaclinica = ' '
    fechayhora = ' '
    calificacion = ' '

    # constructor de la clase citas
    def __init__(self, idpacientes, idmedicos, idhistoriaclinica, fechayhora, calificacion):
        print(f"consultar_citas: {idpacientes}, {idmedicos}, {idhistoriaclinica}, {fechayhora}, {calificacion}")

    # atributos de la instancia de la clase citas
        self.idpacientes = idpacientes
        self.idmedicos = idmedicos
        self.idhistoriaclinica = idhistoriaclinica
        self.fechayhora = fechayhora
        self.calificacion = calificacion
    
    # metodos de la clase citas
    def consultar_citas(self):
        print("Tiene cita con: {idmedicos}, {fechayhora}")

    def modificar_citas(self):
        print("Modificacion exitosa:  {idmedicos}, {fechayhora}")

    def cancelar_citas(self):
        print("Cita cancelada")

    def calificar_citas(self):
        print(" ")


# se crea clase Historiaclinica
class Historiaclinica: 

    # atributos de la clase Historiaclinica
    idhistoriaclinica = ' ' 
    idpacientes = ' '
    idmedicos = ' '
    idcitas = ' '
    diagnostico = ' '
    tratamiento = ' '

    # constructor de la clase Historiaclinica
    def __init__(self, idpacientes, idmedicos, idcitas, diagnostico, tratamiento):
        print(f"consultar_historiaclinica: {idpacientes}, {idmedicos}, {idcitas}, {diagnostico}, {tratamiento}")

    # atributos de la instancia de la clase Historiaclinica
        self.idpacientes = idpacientes
        self.idmedicos = idmedicos
        self.idcitas = idcitas
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        
    
    # metodos de la clase Historiaclinica
    def consultar_historiaclinica(self):
        print("Imprimir: {idpacientes}, {idmedicos}, {idcitas}, {diagnostico}, {tratamiento}")

    
    # Se crea la clase persona
class Persona: 

    # atributos de la clase persona
    idusuario = ' ' 
    nombres = ' '
    apellidos = ' '
    fechanacimiento = ' '
    genero = ' '
    estadocivil = ' '
    ocupacion = ' '
    telefono = ' '
    direccion = ' '
    EPS = ' '
    discapacidad = ' '
    rh = ' '
    tarjetaprofesional = ' '
    especialidad = ' '


    # constructor de la clase persona
    def __init__(self, idusuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh, tarjetaprofesional, especialidad):
        print(f"{idusuario} {nombres}, {apellidos}, {estadocivil}")

    # atributos de la instancia de la clase persona
        self.idusuario = idusuario
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
        self.tarjetaprofesional = tarjetaprofesional
        self.especialidad = especialidad
    
    # metodos de la clase persona
    def consultar_persona(self):
        print("{idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

    def modificar_persona(self):
        print("Modificacion exitosa: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

    def agregar_persona(self):
        print("Se agrego exitosamente: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

# Se crea la clase medico
class Medico: 

    # atributos de la clase medico
    idusuario = ' ' 
    nombres = ' '
    apellidos = ' '
    fechanacimiento = ' '
    genero = ' '
    estadocivil = ' '
    ocupacion = ' '
    telefono = ' '
    direccion = ' '
    EPS = ' '
    discapacidad = ' '
    rh = ' '
    tarjetaprofesional = ' '
    especialidad = ' '


    # constructor de la clase medico
    def __init__(self, idusuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh, tarjetaprofesional, especialidad):
        print(f"{idusuario, nombres, apellidos, fechanacimiento,genero , estadocivil, ocupacion, telefono, direccion, EPS, discapacidad, rh, tarjetaprofesional, especialidad}")

    # atributos de la instancia de la clase medico
        self.idusuario = idusuario
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
        self.tarjetaprofesional = tarjetaprofesional
        self.especialidad = especialidad
    
    # metodos de la clase medico
    def consultar_medico(self):
        print("{idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

    def modificar_medico(self):
        print("Modificacion exitosa: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

    def agregar_medico(self):
        print("Se agrego exitosamente: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}, {tarjetaprofesional}, {especialidad}")

# Se crea la clase paciente
class Paciente: 

    # atributos de la clase paciente
    idusuario = ' ' 
    nombres = ' '
    apellidos = ' '
    fechanacimiento = ' '
    genero = ' '
    estadocivil = ' '
    ocupacion = ' '
    telefono = ' '
    direccion = ' '
    EPS = ' '
    discapacidad = ' '
    rh = ' '


    # constructor de la clase paciente
    def __init__(self, idusuario, nombres, apellidos, fechanacimiento,genero , estadocivil,
    ocupacion, telefono, direccion, EPS, discapacidad, rh):
        print(f"{idusuario} {nombres}, {apellidos}, {estadocivil}")

    # atributos de la instancia de la clase paciente
        self.idusuario = idusuario
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
    
    # metodos de la clase paciente
    def consultar_paciente(self):
        print("{idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}")

    def modificar_paciente(self):
        print("Modificacion exitosa: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}")

    def agregar_paciente(self):
        print("Se agrego exitosamente: {idusuario}, {nombres}, {apellidos}, {fechanacimiento}, {genero}, {estadocivil}, {ocupacion}, {telefono}, {direccion}, {EPS}, {discapacidad}, {rh}")


class_usuario=User(1,1234,"paciente")

print(class_usuario)