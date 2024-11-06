import json

def cargar_datos_json_cursos():
    try:
        with open("gestion/main_db.json","r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return tuple(datos.get("cursos", []))
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def agregar_curso(cursos):
    nuevo_curso = input("Escriba el nombre del curso que quiere agregar: ")
    cursos = list(cursos)
    cursos.append(nuevo_curso)
    cursos = tuple(cursos)
    print("Curso agregado con exito")
    return cursos

def actualizar_info_cursos(cursos, db_json):
    db_json.update({"cursos":cursos})
    return db_json