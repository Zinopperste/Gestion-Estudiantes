import json

def cargar_datos_json_sedes():
    try:
        with open("gestion/main_db.json","r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return tuple(datos.get("sedes", []))
    except (FileNotFoundError, json.JSONDecodeError):
        return []
