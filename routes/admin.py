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
    print(pacienteLista)
    controladorS=superControlador()
    controladorS.actualizarPaciente(pacienteLista)
    return "actualizar"

@superU.route("/crear/paciente/", methods=["POST"])
def prepararCrearPaciente():
    idPaciente=[request.form["IDPaciente"]]
    
    return render_template("crearPacienteAdmin.html", Apaciente=idPaciente)

@superU.route("/crear/nuevopaciente/", methods=["POST"])
def crearNuevoPaciente():
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
    print(pacienteLista)
    controladorS=superControlador()
    controladorS.crearnuevopaciente(pacienteLista)
    return "listo para crear"


def dataTable():
    controladorS=superControlador()
    tPaciente=controladorS.tablaPaciente()
    tMedicos=controladorS.tablaMedico()
    tcitas2=controladorS.tablaCitas()
    tHS=controladorS.tablaHS()
    return tPaciente,tMedicos,tcitas2,tHS


