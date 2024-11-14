import json
import os


def cargar_datos_json():
    if not os.path.exists("gestion/main_db.json"):
        datos_default = {
                    "estudiantes": {
                        "info_estudiantes": [],
                        "cursos": [],
                        "calificaciones": []
                    },
                    "cursos": [],
                    "sedes": []
}
        with open("gestion/main_db.json", 'w') as archivo:
            json.dump(datos_default, archivo, indent=2, separators=(',', ': '))
        try:
            with open("gestion/main_db.json","r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    else:
        try:
            with open("gestion/main_db.json","r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def cargar_datos_json_estudiantes():
    try:
        with open("gestion/main_db.json","r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos.get("estudiantes", {})
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(db_json):
    with open("gestion/main_db.json", 'w') as archivo:
        json.dump(db_json, archivo, indent=2, separators=(',', ': '))

def info_estudiantes():
    db_json = cargar_datos_json_estudiantes()
    estudiantes = db_json["info_estudiantes"]
    estudiantes = [tuple(estudiante) for estudiante in estudiantes]
    return estudiantes

def info_cursos():
    db_json = cargar_datos_json_estudiantes()
    cursos = db_json["cursos"]
    return cursos

def actualizar_info_estudiantes(estudiantes, db_json):
    db_json.update({"info_estudiantes":estudiantes})
    return db_json

def cargar_backup():
    if not os.path.exists("gestion/db_sys.json"):
        datos_default = {
                    "estudiantes": {
                        "info_estudiantes": [],
                        "cursos": [],
                        "calificaciones": []
                    },
                    "cursos": [],
                    "sedes": []
}
        with open("gestion/db_sys.json", 'w') as archivo:
            json.dump(datos_default, archivo, indent=2, separators=(',', ': '))
    else:
        try:
            with open("gestion/db_sys.json","r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
def guardar_backup(db_backup):
    with open("gestion/db_sys.json", 'w') as archivo:
        json.dump(db_backup, archivo, indent=2, separators=(',', ': '))
