"""Lista estudiantes"""
import pandas as pd

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
    visualizar_estudiantes(lista)
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
        #queria agregar encabezados pero... necesitamos saber como uniremos todos los datos de los demás modulos
        #ya que para mostrarlos con ese parametro es necesario que el número de columnas sean fijas a las definidas en "encabezados"
        #encabezados = ["Nombre", "RUT", "Matrícula"]
        visualizar = pd.DataFrame(lista)
        print(f"{visualizar}\n")