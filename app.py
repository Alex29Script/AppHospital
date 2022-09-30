from flask import Flask,jsonify, request, render_template,redirect, url_for,session
#render_template para mostrar las paginas
#redirect los routers
#request recibir la infromacion de los fromularios
#jsonify manejar los archivos json
#session para manejar las sessiones
#cambio para probar en el portatil

from routes.controlador.conexion.loginConsulta import loginConsultaDB



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
            session["contraseña"]=FormPass
            session["tipoUsuario"]=tipoUser
            print(session)
            if tipoUser=="paciente":
                return redirect("/paciente")
            elif tipoUser=="medico":
                return redirect("/medico")
            elif tipoUser=="superusuario":
                return redirect("/admin")
            else:
                return "Usuario con error comuniquese con el admin"
        else: 
            return "no logueado"

    
@app.route("/formregistrarce")
def registroform():
    return render_template("registro.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)