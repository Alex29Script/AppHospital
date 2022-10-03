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
    controladorM=superMedico()
    controladorM.crearHC(infoHC)
    return redirect("/medico/")

@medico.route("/editar/HC/<id>", methods=["GET"])
def editarHistoriaClinica(id):
    controladorM=superMedico()
    infoHistoriaClinic=controladorM.buscarHistoriaCLinica(id)
    print(infoHistoriaClinic)
    return render_template("MedicoHistoriaClinica.html",historiaC=infoHistoriaClinic)

@medico.route("/editar/HC/", methods=["POST"])
def actualizarDiagnostico():
    infoHistoria={
        "idhistoriacita":request.form["IDHistoria"],
        "diagnostico": request.form["ndiag"],
        "tratamiento": request.form["trata"]
    }
    print("info generada del medico",infoHistoria)
    controladorM=superMedico()
    controladorM.actualizarHC(infoHistoria)
    return redirect("/medico/")
