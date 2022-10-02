from flask import Blueprint,session




paciente=Blueprint("paciente",__name__)


@paciente.route("/")
def inicioPaciente():
    
    return "soy paciente"