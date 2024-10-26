"""Lista estudiantes"""
import json

def cargar_datos():
    try:
        with open('gestion/gestion.json', 'r', encoding='utf-8') as archivo:
            campos = json.load(archivo)
            return [tuple(estudiante) for estudiante in campos.get("estudiantes", [])]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def guardar_datos(lista):
    # Guardar la lista actualizada en el archivo
    with open('gestion/gestion.json', 'w', encoding='utf-8') as archivo:
        estudiantes_json = [list(estudiante) for estudiante in lista]
        json.dump({"estudiantes": estudiantes_json }, archivo, ensure_ascii=False, indent=4)


def agregar_estudiante(lista):
    # Pedir el nombre del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    rut = input("Ingrese el rut del estudiante: ")
    matricula = input("Ingrese la matricula del estudiante: ")


    estudiante = (nombre, rut, matricula)
    lista.append(estudiante)
    print(f"El estudiante {nombre} ha sido agregado con exito.")
    return lista

def modificar_datos_estudiante(lista):
    rut = input("Escriba el rut del estudiante a modificar: ")
    
    for i, estudiante in enumerate(lista):
        if estudiante[1] == rut:
            nombre_estudiante, rut_estudiante, matricula_estudiante = estudiante
            nuevo_nombre = input("Escriba el nuevo nombre del estudiante: ")
            nueva_matricula = input("Escriba la nueva matricula del estudiante: ")
            nuevo_nombre = nuevo_nombre if nuevo_nombre else nombre_estudiante
            nueva_matricula = nueva_matricula if nueva_matricula else matricula_estudiante
            lista[i] = (nuevo_nombre, rut_estudiante, nueva_matricula)
            print("Estudiante actualizado.")
            return lista
    print("Estudiante no encontrado.")
    return lista

def eliminar_estudiante(lista):
    rut = input("Escriba el rut del estudiante a eliminar")

    for estudiante in lista:
        if estudiante[1] == rut:
            lista.remove(estudiante)
            print(f"Estudiante con rut {estudiante[1]} eliminado exitosamente")
            return lista
            
    print("Estudiante no encontrado.")
    return lista
    

def visualizar_estudiantes(lista):
    if not lista:
        print("No hay estudiantes registrados.")
    else:
        print("Lista de Estudiantes:")
        for i in lista:
            print(f"Nombre: {i[0]}, RUT: {i[1]}, Matrícula: {i[2]}")

def menu_estudiantes():
    listaEstudiantes = cargar_datos()
    while True:
        opcion = input("uwu")

        if opcion == "1":
            listaEstudiantes = agregar_estudiante(listaEstudiantes)
        elif opcion == "2":
            listaEstudiantes = modificar_datos_estudiante(listaEstudiantes)
        elif opcion == "3":
            visualizar_estudiantes(listaEstudiantes)
        elif opcion == "4":
            listaEstudiantes = eliminar_estudiante(listaEstudiantes)
        elif opcion == "5":
            guardar_datos(listaEstudiantes)
            break
menu_estudiantes()