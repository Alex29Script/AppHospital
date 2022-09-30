
from flask import Blueprint, session,render_template,redirect,request
from routes.controlador.superusuario.super import superControlador


superU=Blueprint("admin",__name__)

@superU.route("/")
def mostrarAdmin():
    try:
        if session["tipoUsuario"]=="superusuario":
            controladorS=superControlador()
            tPaciente=controladorS.tablaPaciente()
            tMedicos=controladorS.tablaMedico()
            tcitas2=controladorS.tablaCitas()
            tHS=controladorS.tablaHS()

            return render_template("appForm.html", Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
        else:
            print("no seesion")
            return redirect("/")
    except:
        print("errores en aca en mostrarAdmin")
        return redirect("/")
##---Eliminar--##
@superU.route("/eliminar/paciente/", methods=["POST"])
def eliminar():
    if session["tipoUsuario"]=="superusuario":
        IDPaciente=request.form["IDPaciente"]
        print(IDPaciente)
        controladorS=superControlador()
        controladorS.eliminarPaciente(IDPaciente)
        return redirect("/admin/")
    else:
            print("no seesion")
            return redirect("/")
        
@superU.route("/eliminar/paciente/tabla/<string:id>", methods=["GET"])        
def eliminarTabla(id):
    if session["tipoUsuario"]=="superusuario":
        print(id)
        controladorS=superControlador()
        controladorS.eliminarPaciente(id)
        return redirect("/admin/")
    else:
            print("no seesion")
            return redirect("/")

##--Editar--#
@superU.route("/buscar/paciente/<string:id>", methods=["GET"])
def buscarPaciente(id):
    if session["tipoUsuario"]=="superusuario":
        controladorS=superControlador()
        DataPaciente=controladorS.buscarPaciente(id)
        print(DataPaciente)
        tPaciente,tMedicos,tcitas2,tHS=dataTable()
        return render_template("appForm.html", paraFormPaciente=DataPaciente,Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
    else:
            print("no seesion")
            return redirect("/")

@superU.route("actualizar/paciente/", methods=["POST"])
def actualizarPaciente():
    pacienteLista=list()
    pacienteLista=tomarInfoPaciente()
    print(pacienteLista)
    controladorS=superControlador()
    controladorS.actualizarPaciente(pacienteLista)
    return redirect("/admin")

@superU.route("/crear/paciente/", methods=["POST"])
def prepararCrearPaciente():
    idPaciente=[request.form["IDPaciente"]]
    
    return render_template("crearPacienteAdmin.html", Apaciente=idPaciente)

@superU.route("/crear/nuevopaciente/", methods=["POST"])
def crearNuevoPaciente():
    pacienteLista=list()
    pacienteLista=tomarInfoPaciente()
    print(pacienteLista)
    controladorS=superControlador()
    controladorS.crearnuevopaciente(pacienteLista)
    return redirect("/admin")

##---medico--##



#Editar Medico
@superU.route("/buscar/medico/<string:id>", methods=["GET"])
def buscarMedico(id):
    if session["tipoUsuario"]=="superusuario":
        controladorS=superControlador()
        DataMedico=controladorS.buscarMedico(id)
        print(DataMedico)
        tPaciente,tMedicos,tcitas2,tHS=dataTable()
        return render_template("appForm.html", paraFormMedico=DataMedico,Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
    else:
            print("no seesion")
            return redirect("/")

@superU.route("/actualizar/medico/", methods=["POST"])
def actualizarMedico():
    medicoLista=list()
    medicoLista=tomarInfoMedico()
    print(medicoLista)
    controladorS=superControlador()
    controladorS.actualizarMedico(medicoLista)
    return redirect("/admin")
#eliminar Medico
@superU.route("/eliminar/medico/<string:id>", methods=["GET"])
def eliminarMedico(id):
    controladorS=superControlador()
    controladorS.eliminarMedico(id)
    return redirect("/admin")
#crear Medico
@superU.route("/crear/medicofromulario/", methods=["POST"])
def formularioMedico():
    idMedico=[request.form["IDMedico"]]
    return render_template("crearMedicoAdmin.html", Amedico=idMedico)

@superU.route("/crear/nuevomedico/", methods=["POST"])
def crearNuevoMedico():
    infoMedico=dicInfoMedico()
    controladorS=superControlador()
    controladorS.crearMedico(infoMedico)
    return redirect("/admin")

##--Citas--##

#eliminar
@superU.route("/eliminar/cita/<string:id>", methods=["GET"])
def eliminarCita(id):
    controladorS=superControlador()
    controladorS.eliminarCita(id)
    return redirect("/admin")
#buscar
@superU.route("/buscarCita/<string:id>", methods=["GET"])
def buscarCita(id):
    controladorS=superControlador()
    cita=controladorS.buscarCita(id)
    tPaciente,tMedicos,tcitas2,tHS=dataTable()
    return render_template("appForm.html",citaRender=cita,Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
#actualizar
@superU.route("/actualizar/cita/", methods=["POST"])
def actualizarCita():
    infoCita=dicInfoCita()
    controladorS=superControlador()
    controladorS.actualizarCita(infoCita)
    return "actualizada"
#crear
@superU.route("/crear/cita/formulario/", methods=["GET"])
def formularioCita():
    tPaciente,tMedicos,tcitas2,tHS=dataTable()
    return render_template("crearCitaAdmin.html",Todos_Medicos=tMedicos,Todos_Pacientes=tPaciente)

@superU.route("/crear/cita/", methods=["POST"])
def crearCita():
    infoCita={
        "idmedico":request.form["IDmed"],
        "idpaciente":request.form["IDPaciente"],
        "fecha":request.form["fecha"]
    }
    controladorS=superControlador()
    controladorS.crearCita(infoCita)

    return "cita creada"


##--Auxiliares--##

def dataTable():
    controladorS=superControlador()
    tPaciente=controladorS.tablaPaciente()
    tMedicos=controladorS.tablaMedico()
    tcitas2=controladorS.tablaCitas()
    tHS=controladorS.tablaHS()
    return tPaciente,tMedicos,tcitas2,tHS

def tomarInfoPaciente():
    pacienteLista=list()
    pacienteLista.append(request.form["idusuario"])
    pacienteLista.append(request.form["nombre"])
    pacienteLista.append(request.form["apellido"])
    pacienteLista.append(request.form["bird"])
    pacienteLista.append(request.form["sexo"])
    pacienteLista.append(request.form["escivil"])
    pacienteLista.append(request.form["job"])
    pacienteLista.append(request.form["tel"])
    pacienteLista.append(request.form["direccion"])
    pacienteLista.append(request.form["discapacidad"])
    pacienteLista.append(request.form["rh"])
    pacienteLista.append(request.form["eps"])
    pacienteLista.append(request.form["email"])
    pacienteLista.append(request.form["pass"])
    return pacienteLista

def tomarInfoMedico():
    medico=list()
    medico.append(request.form["idusuario"])
    medico.append(request.form["nombre"])
    medico.append(request.form["apellido"])
    medico.append(request.form["pass"])
    medico.append(request.form["espM"])
    medico.append(request.form["tel"])
    medico.append(request.form["email"])
    medico.append(request.form["bird"])
    medico.append(request.form["sexo"])
    medico.append(request.form["escivil"])
    medico.append(request.form["direccion"])
    medico.append(request.form["tp"])
    medico.append(request.form["job"])
    medico.append(request.form["rh"])
    return medico

def dicInfoMedico():
    medico={}
    medico={
        "id":request.form["idusuario"],
        "nombre":request.form["nombre"],
        "apellido":request.form["apellido"],
        "pass":request.form["pass"],
        "especialidad":request.form["espM"],
        "tel":request.form["tel"],
        "email":request.form["email"],
        "bird":request.form["bird"],
        "sexo":request.form["sexo"],
        "escivil":request.form["escivil"],
        "direccion":request.form["direccion"],
        "tp":request.form["tp"],
        "job":request.form["job"],
        "rh":request.form["rh"]
        }
    return medico

def dicInfoCita():
    cita={}
    cita={
        "id":request.form["IDCitasB"],
        "fecha":request.form["fecha"],
        "puntaje":request.form["puntaje"],
        "comentarios":request.form["calificacion"],
        "idpaciente":request.form["IDPaciente"],
        "idmedico":request.form["IDmed"]
        }
    return cita