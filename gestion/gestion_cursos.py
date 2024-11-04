from .datos_estudiantes import *

def modificar_curso(cursos):
    curso = input("Cual curso quiere modificar?: ")
    cursos = list(cursos)
    if curso in cursos:
        indice = cursos.index(curso)
        nuevo_curso = input("Como se llamara el curso?: ")
        cursos.insert(indice, nuevo_curso)
        cursos = tuple(cursos)
        return cursos
    else:
        cursos = tuple(cursos)
        print("Curso no encontrado")

def eliminar_curso(cursos, db_backup):
    curso = input("Cual curso quiere modificar?: ")
    cursos = list(cursos)
    if curso in cursos:
        db_backup["cursos"].append(curso)
        cursos.remove(curso)
        cursos = tuple(cursos)
        return cursos
    else:
        cursos = tuple(cursos)
        print("Curso no encontrado")

def visualizar_cursos(cursos):
    print("Listado de Cursos:")
    print("-------------------")
    
    for curso in cursos:
        print(curso)
        print("-------------------")


def agregar_curso_estudiante(cursos, cursos_estudiante):
    rut = input("Escriba el rut de quien quiere agregar el curso: ")
    for estudiante in cursos_estudiante:
        if estudiante[0] == rut:
            nuevo_curso = input("Que curso quiere agregarle al estudiante?(Tiene que estar en la lista de cursos): ")
            if nuevo_curso in cursos:
                estudiante[1].append(nuevo_curso)
                return cursos_estudiante
            else:
                print("El curso no es valido o no se encuentra en la lista")
    else:
            print("Estudiante no encontrado")

def eliminar_curso_estudiante(cursos_estudiante, db_backup):
    rut = input("Escriba el rut de quien quiere agregar el curso: ")
    for estudiante in cursos_estudiante:
        if estudiante[0] == rut:
            curso = input("Que curso quiere borrar del estudiante?: ")
            if curso in estudiante[1]:
                db_backup['estudiantes']['cursos'].append(curso)
                estudiante[1].remove(curso)
                return cursos_estudiante
            else:
                print("El curso no es valido o no se encuentra en la lista")
    else:
            print("Estudiante no encontrado")