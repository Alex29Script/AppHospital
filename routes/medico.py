from flask import Blueprint,session, render_template,redirect
from routes.admin import tomarInfoPaciente

from routes.controlador.medico.medico import medicocControlador

medico=Blueprint("medico",__name__)


@medico.route("/")
def inicioMedico():  
    try:
        if session["tipoUsuario"]=="medico":
            controladorM=medicocControlador()
            tmedico=controladorM.tablaMedico()
            return render_template("appForm.html", todos_medicos=tmedico)
        else:
            print("no seesion")
            return redirect("/")
    except:
        print("errores en aca en mostrarmedico")
        return redirect("/")

@medico.route("consultar/Cita/", methods=["POST"])
def asignarCita():
    citaLista=list()
    citaLista=tomarInfocita()
    print(citaLista)
    controladorM=medico()
    controladorM.consultarcita(citaLista)
    return redirect("/medico")

@medico.route("consultar/paciente/", methods=["POST"])
def consultarPaciente():
    pacienteLista=list()
    pacienteLista=tomarInfoPaciente()
    print(pacienteLista)
    controladorM=medico()
    controladorM.consultarpaciente(pacienteLista)
    return redirect("/medico")