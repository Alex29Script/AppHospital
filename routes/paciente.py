from contextlib import redirect_stderr
from pickle import GET
from flask import Flask 
from flask import Flask, render_template, redirect
import pacientes

paciente = Flask (__name__)
@paciente.route('/pacientes/Citas', methods= [GET])
def asignarCita():
    return render_template("Pacientes.html")


@paciente.route('/pacientes/ConsultarCitas', methods= [GET])
def CitasAsignadas():
    return render_template ("Pacientes.html")