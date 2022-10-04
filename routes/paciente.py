
from flask import Flask, render_template, redirect,Blueprint, request, session

from routes.controlador.paciente.paciente import pacienteControlador


paciente=Blueprint("paciente",__name__)


@paciente.route('/', methods= ["GET"])
def asignarCita():
    controladorP=pacienteControlador()
    listaMedicos=controladorP.llamarMedicos()
    idpaciente={"idpaciente":session["idusuario"]}
    listaCitas=controladorP.citasProgramadas(idpaciente)
    print("estas son las citas", listaCitas)
    return render_template("Pacientes.html",medicos_disponibles=listaMedicos,citas_pacientes=listaCitas)

@paciente.route('/asignarCita/', methods=["POST"])
def Cita_asignada():
    infoCita={
        "idmedico":request.form["idmedico"],
        "fecha":request.form["fecha"],
        "idpaciente": session["idusuario"]
        }
    controladorP=pacienteControlador()
    controladorP.PacienteTomarCita(infoCita)
    

    return redirect("/paciente/")

@paciente.route("/eliminar/cita/", methods=["POST"])
def pacienteEliminarCitas():
    infoCita={ #datos necesarios para eliminar una cita tomados del formulario y de la sesion
        "idpaciente": session["idusuario"],
        "idcita": request.form["idcita"],
    }
    controladorP=pacienteControlador()
    controladorP.eliminarCitaPaciente(infoCita)
    return redirect("/paciente/")

@paciente.route("/modificar/cita/", methods=["POST"])
def actualizarCitaPaciente():
    infoCita={
        "idpaciente": session["idusuario"],
        "idcita": request.form["idcita"],
        "idmedico":request.form["idmedico2"],
        "fecha": request.form["fecha"]
    }
    controladorP=pacienteControlador()
    controladorP.modificarCitaPaciente(infoCita)
    return redirect("/paciente/")

@paciente.route("/vercitas/", methods=["GET"])
def verCitasAtendidasPaciente():
    controladorP=pacienteControlador()
    idpaciente={"idpaciente":session["idusuario"]}
    listaCitas=controladorP.citasProgramadasExtedida(idpaciente)
    print(listaCitas)
    return render_template("PacienteHistoriaClinica.html", citas_paciente=listaCitas)



