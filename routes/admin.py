
from flask import Blueprint, session,render_template,redirect
from routes.controlador.superusuario.super import superControlador


superU=Blueprint("admin",__name__)

@superU.route("/")
def mostrarAdmin():
    try:
        if session["tipoUsuario"]=="superusuario":
            controladorS=superControlador()
            tPaciente=controladorS.tablaPaciente()
            tMedicos=controladorS.tablaMedico()
            tcitas2=controladorS.tablaCitas()
            tHS=controladorS.tablaHS()

            return render_template("appForm.html", Todos_Pacientes=tPaciente, Todos_Medicos=tMedicos,Todos_citas=tcitas2,Todos_hs=tHS)
        else:
            print("no seesion")
            return redirect("/")
    except:
        print("errores en aca en mostrarAdmin")
        return redirect("/")

@superU.route("/saludar")
def saludar():
    return "Hola soy el admin"