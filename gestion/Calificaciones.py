from .datos_estudiantes import cargar_datos_json_estudiantes

def datos_calificaciones():
    db_json = cargar_datos_json_estudiantes()
    calificaciones = db_json["calificaciones"]
    return calificaciones

def actualizar_info_calificaciones(calificaciones, db_json):
    db_json.update({"calificaciones":calificaciones})
    return db_json

def Agregar_calificaciones(calificaciones):
    visualizar_calificaciones(calificaciones)
    rut = input("Escriba el rut al estudiante que quiere agregar calificacion: ")
    for estudiante in calificaciones:
        if rut == estudiante[0]:
            while True:
                materia = input("De que materia quiere agregar la calificacion?(Si desea cancelar escriba 2): ")
                if materia in estudiante[1]:
                    calificacion = input("Ingrese la calificacion: ")
                    estudiante[1][materia].append(calificacion)
                    print(f"Calificacion de {calificacion} agregada a {materia} para el estudiante con RUT {rut}")
                    return calificaciones
                elif materia == "2":
                    return calificaciones
                else:
                    print("No es una materia valida")
    else:
        print("RUT no encontrado")

def eliminar_calificaciones(calificaciones, db_backup):
    visualizar_calificaciones(calificaciones)
    rut = input("Escriba el rut al estudiante que quiere borrar la calificacion: ")
    for estudiante in calificaciones:
        if rut == estudiante[0]:
            while True:
                materia = input("De que materia quiere borrar la calificacion?(Si desea cancelar escriba 2): ")
                if materia in estudiante[1]:
                    try:
                        indice = int(input("Ingrese la posicion de la calificacion (La primera es 1, la segunda 2 y asi sucesivamente): "))
                        if 1 <= indice <= len(estudiante[1][materia]):
                            db_backup['estudiantes']['calificaciones'].append(estudiante[1][materia][indice - 1])
                            estudiante[1][materia].pop(indice - 1)
                            print(f"Calificacion borrada de {materia} para el estudiante con RUT {rut}")
                            return calificaciones
                        else:
                            print("Indice fuera de rango. Intente de nuevo")
                    except ValueError:
                        print("Entrada no valida. Por favor, ingrese un numero entero")
                elif materia == "2":
                    return calificaciones
                else:
                    print("No es una materia valida")
    else:
        print("RUT no encontrado")

def visualizar_calificaciones(calificaciones):
    for estudiante in calificaciones:
        rut = estudiante[0]
        notas = estudiante[1]

        print(f"Calificaciones para el estudiante con RUT {rut}:")
        for curso, notas_curso in notas.items():
            print(f"  {curso}: {notas_curso if notas_curso else 'No hay calificaciones'}")

