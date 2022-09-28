from flask import Blueprint,session

medico=Blueprint("medico",__name__)


@medico.route("/")
def inicioMedico():
    return "soy medico"