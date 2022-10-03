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
    

    return redirect("/paciente")