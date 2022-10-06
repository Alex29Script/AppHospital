
from flask import Flask,jsonify, request, render_template,redirect, url_for,session
#render_template para mostrar las paginas html rendelizarlas
#redirect redireccionar
#request.form recibir la informacion de los fromularios
#jsonify manejar los  json
#session para manejar las sessiones

from routes.controlador.superusuario.super import superControlador
from routes.controlador.conexion.loginConsulta import loginConsultaDB
from routes.admin import tomarInfoPaciente


from routes.admin import superU
from routes.medico import medico
from routes.paciente import paciente

app = Flask(__name__)

app.register_blueprint(superU,url_prefix="/admin")
app.register_blueprint(medico,url_prefix="/medico")
app.register_blueprint(paciente,url_prefix="/paciente")


#cambios
app.secret_key=  b'_5#y2L"F4Q8z\n\xec]/'
"""
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
"""


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def loguear():
    if request.method=="POST":
        login=loginConsultaDB()
        FormUsuario= request.form["usuario"]
        FormPass=request.form["contraseña"]
        print(FormUsuario,FormPass)
        comprobacion,tipoUser=login.autenticar(FormUsuario,FormPass)
        if comprobacion==True:
            session["idusuario"]=FormUsuario
            session["tipoUsuario"]=tipoUser
            #print(session)
            if tipoUser=="paciente":
                return redirect("/paciente")
            elif tipoUser=="medico":
                return redirect("/medico")
            elif tipoUser=="superusuario":
                return redirect("/admin")
            else:
                return "Usuario con error comuniquese con el admin"
        else: 
            return redirect("/")

    
@app.route("/formregistrarce", methods=["POST","GET"])
def registroform():
    if request.method=="GET":
        return render_template("registro.html")
    elif request.method=="POST":
        nuevo_paciente=tomarInfoPaciente()
        controladorS=superControlador()
        controladorS.crearnuevopaciente(nuevo_paciente)
        return redirect("/")
    else:
        return redirect("/")

@app.route("/cerrar/",methods=["GET"])
def cerrarSession():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)