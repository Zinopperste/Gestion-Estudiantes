def agregar_info_estudiante(lista_estudiantes, calificaciones, cursos):
    nombre = input("Agrege el nombre del estudiante: ")
    while True:
        rut = input("Agrege el rut del estudiante: ")
        validador = verificador_rut(rut)
        if validador is True:
            break
        elif validador is False:
            print("No es un rut valido")
    matricula = input("Agrege la matricula del estudiante: ")
    estudiante = (nombre, rut, matricula)

    lista_estudiantes.append(estudiante)
    nueva_calificacion = [rut, {}]
    calificaciones.append(nueva_calificacion)
    nuevo_cursos = [rut, []]
    cursos.append(nuevo_cursos)
    print(f"Estudiante {nombre} agregado exitosamente")
    return lista_estudiantes, calificaciones, cursos

def modificar_info_estudiante(lista_estudiantes):
    rut = input("Escriba el rut del estudiante que desea buscar(sin puntos y con guion): ")
    for indice, estudiante in enumerate(lista_estudiantes):
        if estudiante[1] == rut:
            print(f"Estudiante {estudiante[0]} encontrado")
            nombre = input("Agrege el nuevo nombre del estudiante: ")
            matricula = input("Agrege la nueva matricula del estudiante: ")

            nuevo_nombre = nombre if nombre else estudiante[0]
            rut_es = estudiante[1]
            nueva_matricula = matricula if matricula else estudiante[2]

            lista_estudiantes[indice] = (nuevo_nombre, rut_es, nueva_matricula)

            print(f"Informacion del estudiante {estudiante[0]} actualizada")
            return lista_estudiantes
        print("Estudiante no encontrado")
        return lista_estudiantes

def eliminar_info_estudiante(lista_estudiantes, db_backup):
    rut = input("Escriba el rut del estudiante que desea buscar(sin puntos y con guion): ")
    for indice, estudiante in enumerate(lista_estudiantes):
        if estudiante[1] == rut:
            print(f"Estudiante {estudiante[0]} encontrado")
            while True:
                confirmacion = input("Escriba SI en mayusculas si quiere eliminar la informacion y NO en mayusculas si no quiere eliminar: ")
                
                if confirmacion == "SI":
                    backup = lista_estudiantes[indice]
                    db_backup['estudiantes']['info_estudiantes'].append(backup)
                    lista_estudiantes.pop(indice)
                    print("Informacion del estudiante eliminada con exito")
                    return lista_estudiantes
                elif confirmacion == "NO":
                    print("Eliminacion cancelada")
                    return lista_estudiantes
                else:
                    print("Opcion no valida, Escoja entre SI para eliminar y NO para volver atras")
    else:
        print("Estudiante no encontrado")
        return lista_estudiantes

def visualizar_estudiantes(lista_estudiantes):
    print(f"|{'-'*21}|{'-'*11}|{'-'*16}|")
    print(f"|{'Nombre':<21}|{'RUT':<11}|{'Matricula':<16}|")
    print(f"|{'-'*21}|{'-'*11}|{'-'*16}|")
    for indice in range(len(lista_estudiantes)):
        estudiante = lista_estudiantes[indice]
        print(f"|{estudiante[0]:<21}|{estudiante[1]:<11}|{estudiante[2]:<16}|")
    print(f"|{'-'*21}|{'-'*11}|{'-'*16}|")

def verificador_rut(rut):
    if "-" in rut:
        rut = rut.replace("-","")
    else:
        return False
    
    if len(rut) not in range(8, 10):
        return False
    
    verificador = rut[-1]
    rut = rut[:-1]
    suma = 0

    if verificador == "0":
        verificador = 11
    elif verificador != "k" or "K":
        try:
            verificador = int(verificador)
        except ValueError:
            return False
    else:
        verificador = 10

    try:
        if len(rut) == 8:
            suma = suma + (int(rut[0]) * 3)
            suma = suma + (int(rut[1]) * 2)
            suma = suma + (int(rut[2]) * 7)
            suma = suma + (int(rut[3]) * 6)
            suma = suma + (int(rut[4]) * 5)
            suma = suma + (int(rut[5]) * 4)
            suma = suma + (int(rut[6]) * 3)
            suma = suma + (int(rut[7]) * 2)
        else:
            suma = suma + (int(rut[0]) * 2)
            suma = suma + (int(rut[1]) * 7)
            suma = suma + (int(rut[2]) * 6)
            suma = suma + (int(rut[3]) * 5)
            suma = suma + (int(rut[4]) * 4)
            suma = suma + (int(rut[5]) * 3)
            suma = suma + (int(rut[6]) * 2)
    except ValueError:
        return False
    restante = suma%11
    validador = 11 - restante
    if verificador == validador:
        return True
    else:
        return False
