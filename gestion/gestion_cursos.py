import json
import os
import gestion.gestion_estudiantes as gte

db_dir = os.path.join("gestion", "db_sys")
database_file = os.path.join(db_dir, "database.json")

# Definir las tuplas de cursos para cada carrera
CURSOS_ANALISTA_PROGRAMADOR = ("Introducción a la Programación", "Algoritmos y Estructuras de Datos", "Base de Datos", "Desarrollo Web")
CURSOS_COMPUTACION_INFORMATICA = ("Matemáticas Discretas", "Sistemas Operativos", "Redes de Computadoras", "Inteligencia Artificial")
CURSOS_PREVENCION_RIESGOS = ("Química General", "Seguridad Laboral", "Ergonomía", "Gestión Ambiental")

# Diccionario de carreras y sus respectivos cursos
CARRERAS = {  
    "Analista Programador": CURSOS_ANALISTA_PROGRAMADOR,
    "Computación Informática": CURSOS_COMPUTACION_INFORMATICA,
    "Prevención de Riesgos": CURSOS_PREVENCION_RIESGOS
}

def cargar_datos():
    if os.path.exists(database_file):
        with open(database_file, "r") as file:
            return json.load(file)
    return {}

def guardar_datos(datos_estudiantes):
    with open(database_file, "w") as file:
        json.dump(datos_estudiantes, file, indent=4)

def visualizar_cursos(carrera):
    """
    Muestra los cursos disponibles para una carrera específica.
    """
    cursos = CARRERAS.get(carrera)
    if cursos:
        print(f"Cursos para {carrera}:")
        for curso in cursos:
            print(f"- {curso}")
    else:
        print("Carrera no encontrada.")

def agregar_curso_estudiante(rut_estudiante, curso):
    """
    Agrega un curso específico a un estudiante si no lo tiene asignado.
    """
    datos_estudiantes = cargar_datos()
    estudiante = datos_estudiantes.get(rut_estudiante)
    
    if not estudiante:
        print("Error: Estudiante no encontrado.")
        return
    
    if curso not in estudiante["cursos"]:
        estudiante["cursos"].append(curso)
        estudiante["calificaciones"].append({"curso": curso, "nota": None})  # Agregar curso sin calificación
        guardar_datos(datos_estudiantes)
        print(f"Curso '{curso}' añadido al estudiante con RUT {rut_estudiante}.")
    else:
        print(f"El curso '{curso}' ya está asignado al estudiante.")

def eliminar_curso_estudiante(rut_estudiante, curso):
    """
    Elimina un curso específico de un estudiante.
    """
    datos_estudiantes = cargar_datos()
    estudiante = datos_estudiantes.get(rut_estudiante)
    
    if not estudiante:
        print("Error: Estudiante no encontrado.")
        return
    
    if curso in estudiante["cursos"]:
        estudiante["cursos"].remove(curso)
        estudiante["calificaciones"] = [cal for cal in estudiante["calificaciones"] if cal["curso"] != curso]
        guardar_datos(datos_estudiantes)
        print(f"Curso '{curso}' eliminado del estudiante con RUT {rut_estudiante}.")
    else:
        print(f"El curso '{curso}' no está asignado al estudiante.")
