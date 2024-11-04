def agregar_info_estudiante(lista_estudiantes, calificaciones, cursos):
    nombre = input("Agrege el nombre del estudiante: ")
    rut = input("Agrege el rut del estudiante: ")
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
            rut_es = input("Agrege el nuevo rut del estudiante: ")
            matricula = input("Agrege la nueva matricula del estudiante: ")

            nuevo_nombre = nombre if nombre else estudiante[0]
            nuevo_rut = rut_es if rut_es else estudiante[1]
            nueva_matricula = matricula if matricula else estudiante[2]

            lista_estudiantes[indice] = (nuevo_nombre, nuevo_rut, nueva_matricula)

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
                    return lista_estudiantes
                elif confirmacion == "NO":
                    return lista_estudiantes
                else:
                    print("Opcion no valida, Escoja entre SI para eliminar y NO para volver atras")
        else:
            print("Estudiante no encontrado")

def visualizar_estudiantes(lista_estudiantes):
    print(f"|{'-'*21}|{'-'*11}|{'-'*16}|")
    print(f"|{'Nombre':<21}|{'RUT':<11}|{'Matricula':<16}|")
    print(f"|{'-'*21}|{'-'*11}|{'-'*16}|")
    for indice in range(len(lista_estudiantes)):
        estudiante = lista_estudiantes[indice]
        print(f"|{estudiante[0]:<21}|{estudiante[1]:<11}|{estudiante[2]:<16}|")
    print(f"|{'-'*21}|{'-'*11}|{'-'*16}|")