import json

def cargar_datos_json():
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
        json.dump(db_json, archivo, indent=4)

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
    try:
        with open("gestion/db_sys.json","r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def guardar_backup(db_backup):
    with open("gestion/db_sys.json", 'w') as archivo:
        json.dump(db_backup, archivo, indent=4)
