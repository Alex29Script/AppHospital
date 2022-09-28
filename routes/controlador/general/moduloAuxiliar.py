
import sqlite3

class Auxiliar:
    # la posicion en el vector de Historia clinica para id usuario debe en la posicion 2 y la del medico la 3
    #al final devuelve un vector con la lista y recupera el nombre del paciente y del medico junto con sus apellidos apellido
    def obtenerHCnombre(list=list(),url=str):
        try: 
            conexion=sqlite3.connect(url)
            cur=conexion.cursor()
            personasCitas=[]
            for i in range(0,len(list)):
                cur.execute('SELECT nombres,apellidos FROM persona WHERE idusuario==%s' %list[i][2])
                nombrePaciente=cur.fetchone()
                cur.execute('SELECT nombres,apellidos FROM persona WHERE idusuario==%s' %list[i][3])
                nombremedico=cur.fetchone()
                personasCitas.append((nombrePaciente, nombremedico))
            listPacMed=[]
            Completa=[]
            for i in range(0,len(list)):
                nombrePaciente=personasCitas[i][0][0]+" "+personasCitas[i][0][1]
                nombreMedico=personasCitas[i][1][0]+" "+personasCitas[i][1][1]
                listPacMed.append((nombrePaciente,nombreMedico))
                Completa.append(list[i]+listPacMed[i])
                
            return Completa
        except:
                print("error")
        finally:
            cur.close()
            conexion.close()

"""
ejemplo:
lista=[(1, 1, 467, 445), (2, 2, 467, 1083467445)]
url="F:/Dropbox/Grupo_5_2126/Sprint 3/AppHospitalGeneralBarranquilla v2/routes/controlador/conexion/db/DBHospitalGeneralBarranquilla.db"
palmas=Auxiliar.obtenerHCnombre(lista,url)

print(palmas)
# resultado [(1, 1, 467, 445, 'Esebio Sanchez', 'Andres Morales'), (2, 2, 467, 1083467445, 'Esebio Sanchez', 'Alexis Ariza')]
"""