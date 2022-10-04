
from flask import Blueprint, session,render_template,redirect,request
from routes.controlador.superusuario.super import superControlador


superU=Blueprint("admin",__name__)

@superU.route("/")
def mostrarAdmin():
    try:
        if session:
            if session["tipoUsuario"]=="superusuario":
                controladorS=superControlador()
                tPaciente=controladorS.tablaPaciente()
                tMedicos=controladorS.tablaMedico()
                tcitas2=controladorS.tablaCitas()
                tHS=controladorS.tablaHS()

                return render_template("appForm.html", Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
            else:
                return redirect("/")
        else:
            return redirect("/")
    except:
        print("errores en aca en mostrarAdmin")
        return redirect("/")
##---Eliminar--##
@superU.route("/eliminar/paciente/", methods=["POST"])
def eliminar():
    if session:
        if session["tipoUsuario"]=="superusuario":
            IDPaciente=request.form["IDPaciente"]
            print(IDPaciente)
            controladorS=superControlador()
            controladorS.eliminarPaciente(IDPaciente)
            return redirect("/admin/")
        else:
            return redirect("/")
    else:
        return redirect("/")
        
@superU.route("/eliminar/paciente/tabla/<string:id>", methods=["GET"])        
def eliminarTabla(id):
    if session:
        if session["tipoUsuario"]=="superusuario":
            print(id)
            controladorS=superControlador()
            controladorS.eliminarPaciente(id)
            return redirect("/admin/")
        else:
            return redirect("/")
    else:
        return redirect("/")

##--Editar--#
@superU.route("/buscar/paciente/<string:id>", methods=["GET"])
def buscarPaciente(id):
    if session:
        if session["tipoUsuario"]=="superusuario":
            controladorS=superControlador()
            DataPaciente=controladorS.buscarPaciente(id)
            print(DataPaciente)
            tPaciente,tMedicos,tcitas2,tHS=dataTable()
            return render_template("appForm.html", paraFormPaciente=DataPaciente,Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
        else:
            return redirect("/")
    else:
        return redirect("/")

@superU.route("actualizar/paciente/", methods=["POST"])
def actualizarPaciente():
    if session:
        if session["tipoUsuario"]=="superusuario":
            pacienteLista=list()
            pacienteLista=tomarInfoPaciente()
            print(pacienteLista)
            controladorS=superControlador()
            controladorS.actualizarPaciente(pacienteLista)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")

@superU.route("/crear/paciente/", methods=["POST"])
def prepararCrearPaciente():
    if session:
        if session["tipoUsuario"]=="superusuario":
            idPaciente=[request.form["IDPaciente"]]
            return render_template("crearPacienteAdmin.html", Apaciente=idPaciente)
        else:
            return redirect("/")
    else:
        return redirect("/")

@superU.route("/crear/nuevopaciente/", methods=["POST"])
def crearNuevoPaciente():
    if session:
        if session["tipoUsuario"]=="superusuario":
            pacienteLista=list()
            pacienteLista=tomarInfoPaciente()
            print(pacienteLista)
            controladorS=superControlador()
            controladorS.crearnuevopaciente(pacienteLista)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")

##---medico--##



#Editar Medico
@superU.route("/buscar/medico/<string:id>", methods=["GET"])
def buscarMedico(id):
    if session:
        if session["tipoUsuario"]=="superusuario":
            controladorS=superControlador()
            DataMedico=controladorS.buscarMedico(id)
            print(DataMedico)
            tPaciente,tMedicos,tcitas2,tHS=dataTable()
            return render_template("appForm.html", paraFormMedico=DataMedico,Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
        else:
            return redirect("/")
    else:
        return redirect("/")

@superU.route("/actualizar/medico/", methods=["POST"])
def actualizarMedico():
    if session:
        if session["tipoUsuario"]=="superusuario":
            medicoLista=list()
            medicoLista=tomarInfoMedico()
            print(medicoLista)
            controladorS=superControlador()
            controladorS.actualizarMedico(medicoLista)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")

#eliminar Medico
@superU.route("/eliminar/medico/<string:id>", methods=["GET"])
def eliminarMedico(id):
    if session:
        if session["tipoUsuario"]=="superusuario":
            controladorS=superControlador()
            controladorS.eliminarMedico(id)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")

#crear Medico
@superU.route("/crear/medicofromulario/", methods=["POST"])
def formularioMedico():
    if session:
        if session["tipoUsuario"]=="superusuario":
            idMedico=[request.form["IDMedico"]]
            return render_template("crearMedicoAdmin.html", Amedico=idMedico)
        else:
            return redirect("/")
    else:
        return redirect("/")

@superU.route("/crear/nuevomedico/", methods=["POST"])
def crearNuevoMedico():
    if session:
        if session["tipoUsuario"]=="superusuario":
            infoMedico=dicInfoMedico()
            controladorS=superControlador()
            controladorS.crearMedico(infoMedico)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")

##--Citas--##

#eliminar
@superU.route("/eliminar/cita/<string:id>", methods=["GET"])
def eliminarCita(id):
    if session:
        if session["tipoUsuario"]=="superusuario":
            controladorS=superControlador()
            controladorS.eliminarCita(id)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")
#buscar
@superU.route("/buscarCita/<string:id>", methods=["GET"])
def buscarCita(id):
    if session:
        if session["tipoUsuario"]=="superusuario":
            controladorS=superControlador()
            cita=controladorS.buscarCita(id)
            tPaciente,tMedicos,tcitas2,tHS=dataTable()
            return render_template("appForm.html",citaRender=cita,Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
        else:
            return redirect("/")
    else:
        return redirect("/")

#actualizar
@superU.route("/actualizar/cita/", methods=["POST"])
def actualizarCita():
    if session:
        if session["tipoUsuario"]=="superusuario":
            infoCita=dicInfoCita()
            controladorS=superControlador()
            controladorS.actualizarCita(infoCita)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")
#crear
@superU.route("/crear/cita/formulario/", methods=["GET"])
def formularioCita():
    if session:
        if session["tipoUsuario"]=="superusuario":
            tPaciente,tMedicos,tcitas2,tHS=dataTable()
            return render_template("crearCitaAdmin.html",Todos_Medicos=tMedicos,Todos_Pacientes=tPaciente)
        else:
            return redirect("/")
    else:
        return redirect("/")

@superU.route("/crear/cita/", methods=["POST"])
def crearCita():
    if session:
        if session["tipoUsuario"]=="superusuario":
            infoCita={
                "idmedico":request.form["IDmed"],
                "idpaciente":request.form["IDPaciente"],
                "fecha":request.form["fecha"]
            }
            controladorS=superControlador()
            controladorS.crearCita(infoCita)

            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")

##---Historia Clinica--##

#crear a formulario
@superU.route("/crear/hc/formulario/", methods=["POST"])
def fromularioCita():
    if session:
        if session["tipoUsuario"]=="superusuario":
            controladorS=superControlador()
            idcita=(request.form["IDCita"])
            tPaciente,tMedicos,tcitas2,tHS=dataTable()
            idcita=controladorS.buscarinfoHC(tcitas2,idcita)
            return render_template("crearHCAdmin.html", idcita=idcita,Todos_Medicos=tMedicos,Todos_Pacientes=tPaciente)
        else:
            return redirect("/")
    else:
        return redirect("/")

@superU.route("/crear/hc/", methods=["POST"])
def crearHC():
    if session:
        if session["tipoUsuario"]=="superusuario":
            infoHC={
                "idcita":request.form["IDCita"],
                "idmedico":request.form["IDmed"],
                "idpaciente":request.form["IDPaciente"],
                "diagnostico":request.form["ndiag"],
                "tratamiento":request.form["trata"]
            }
            controladorS=superControlador()
            controladorS.crearHC(infoHC)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")

@superU.route("/editar/hc/<string:id>", methods=["GET"])
def editarHC(id):
    if session:
        if session["tipoUsuario"]=="superusuario":
            if request.method=="GET":
                controladorS=superControlador()
                historia=controladorS.buscarHistClinica(id)
                
                tPaciente,tMedicos,tcitas2,tHS=dataTable()
                return render_template("appForm.html",histRender=historia,Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
        else:
            return redirect("/")
    else:
        return redirect("/")  

@superU.route("/editar/hc/", methods=["POST"])
def actualizarHC():
    if session:
        if session["tipoUsuario"]=="superusuario":
            infoHC={
                "idHC":request.form["IDHistoria"],
                "idcita":request.form["IDCita"],
                "idmedico":request.form["IDmed"],
                "idpaciente":request.form["IDPaciente"],
                "diagnostico":request.form["ndiag"],
                "tratamiento":request.form["trata"]
            }
            controladorS=superControlador()
            controladorS.actualizarHC(infoHC)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")


@superU.route("/eliminar/hc/<string:id>", methods=["GET"])
def elimnarHC(id):
    if session:
        if session["tipoUsuario"]=="superusuario":
            controladorS=superControlador()
            controladorS.eliminarHC(id)
            return redirect("/admin")
        else:
            return redirect("/")
    else:
        return redirect("/")















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