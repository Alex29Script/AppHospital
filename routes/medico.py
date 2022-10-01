from flask import Blueprint,session, render_template

medico=Blueprint("medico",__name__)


@medico.route("/")
def inicioMedico():
    idmedico=session["idusuario"]
    
    return render_template("MedicoCitas.html")