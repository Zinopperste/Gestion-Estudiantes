"""Lista estudiantes"""
import json

def agregar_estudiante ():
    # Abrir json y cargar datos de la lista estudiantes
    try:
        with open('gestion/gestion_estudiantes.json', 'r', encoding='utf-8') as archivo:
            listaEstudiantes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        listaEstudiantes = []

    # Pedir el nombre del estudiante
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    listaEstudiantes.append(nombre_estudiante)

    # Guardar la lista actualizada en el archivo
    with open('gestion/gestion_estudiantes.json', 'w', encoding='utf-8') as archivo:
        json.dump(listaEstudiantes, archivo, ensure_ascii=False, indent=4)

    print(f"El estudiante {nombre_estudiante} ha sido agregado con exito.")