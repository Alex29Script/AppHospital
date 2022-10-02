
from flask import Blueprint, request,session, render_template,redirect

from routes.controlador.medico.controladorMedico import superMedico

medico=Blueprint("medico",__name__)


@medico.route("/")
def inicioMedico():
    idmedico=session["idusuario"]
    #print("medico en session:",idmedico)
    controladorM=superMedico()
    citasMedico=controladorM.obtenerCitasMedico(idmedico)
    #print("estas son las citas del medico",citasMedico)
    return render_template("MedicoCitas.html", citas_medico=citasMedico)

@medico.route("/atender/<string:info>",methods=["GET"])
def atenderCita(info):
    cita=list()
    cita=info.split("_")
    cita.append(session["idusuario"])
    print(cita)
    
    return render_template("MedicoAtender.html",info_cita=cita)

@medico.route("/atender/",methods=["POST"])
def crearHG():
    infoHC={
        "idcita": request.form["IDCita"],
        "idpaciente":request.form["IDPaciente"],
        "idmedico":request.form["IDmed"],
        "diagnostico":request.form["ndiag"],
        "tratamiento":request.form["trata"]
    }
    return infoHC