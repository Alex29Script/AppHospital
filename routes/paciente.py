from flask import Blueprint, session,render_template,redirect,request
from flask import Flask, render_template
from routes.admin import tomarInfoPaciente

from routes.controlador.paciente.paciente import pacienteControlador

paciente=Blueprint("paciente",__name__)

@paciente.route("/")
def consultarCita():
    try:
        if session["tipoUsuario"]=="idpaciente":
            controladorP=pacienteControlador()
            consultarCita=controladorP.tablaCitas(idpaciente)
            return render_template("pacientes.html", Todas_citas=idpaciente)
        else:
            print("no session")
            return redirect("/pacientes.html")
    except:
        print("errores en aca en mostrarpaciente")
        return redirect("/")

@paciente.route("/")
def asignarCita():
    try:
        if session["tipoUsuario"]=="idpaciente":
        controladorP=pacienteControlador()
        citasMedicos=controla