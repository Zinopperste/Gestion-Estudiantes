from .datos_estudiantes import *

def modificar_curso(cursos):
    curso = input("Escriba el nombre del curso a modificar: ")
    cursos = list(cursos)
    if curso in cursos:
        indice = cursos.index(curso)
        nuevo_curso = input("Escriba el nuevo nombre del curso: ")
        cursos[indice] = nuevo_curso
        cursos = tuple(cursos)
        print("Curso modificado con exito")
        return cursos
    else:
        print("Curso no encontrado")
        return tuple(cursos)

def eliminar_curso(cursos, db_backup):
    curso = input("Escriba el nombre del curso a eliminar: ")
    cursos = list(cursos)
    if curso in cursos:
        db_backup["cursos"].append(curso)
        cursos.remove(curso)
        cursos = tuple(cursos)
        print("Curso eliminado con exito")
        return cursos
    else:
        print("Curso no encontrado")
        return tuple(cursos)

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
            nuevo_curso = input("Escriba el nombre del curso a agregar(Tiene que estar en la lista de cursos): ")
            if nuevo_curso in cursos:
                estudiante[1].append(nuevo_curso)
                print("Curso agregado al estudiante con exito")
                return cursos_estudiante
            else:
                print("El curso no es valido o no se encuentra en la lista")
                return cursos_estudiante
    else:
        print("Estudiante no encontrado")
        return cursos_estudiante


def eliminar_curso_estudiante(cursos_estudiante, db_backup):
    rut = input("Escriba el rut de quien quiere agregar el curso: ")
    for estudiante in cursos_estudiante:
        if estudiante[0] == rut:
            curso = input("Escriba el nombre del curso a eliminar: ")
            if curso in estudiante[1]:
                db_backup['estudiantes']['cursos'].append(curso)
                estudiante[1].remove(curso)
                print("Curso eliminado al estudiante con exito")
                return cursos_estudiante
            else:
                print("El curso no es valido o no se encuentra en la lista")
                return cursos_estudiante
    else:
        print("Estudiante no encontrado")
        return cursos_estudiante

def visualizar_cursos_estudiantes(cursos_estudiantes):
    for estudiante in cursos_estudiantes:
        rut = estudiante[0]
        cursos = estudiante[1]

        print(f"Cursos de el estudiante con RUT {rut}:")
        for curso in cursos:
            print(f"  {curso}: {cursos_estudiantes if cursos_estudiantes else 'No hay cursos'}")