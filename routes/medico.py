from flask import Blueprint,session, render_template

medico=Blueprint("medico",__name__)


@medico.route("/")
def inicioMedico():
    
    return render_template("MedicoCitas.html")