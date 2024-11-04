import gestion as gt

def menu_principal():
    global db_json
    db_json = gt.cargar_datos_json()
    global db_backup
    db_backup = gt.cargar_backup()
    while True:
        print(
"""
1. Acceder al menu de estudiantes
2. Acceder al menu de cursos
3. Acceder al menu de la universidad
4. Salir
""")
        choice_main = input("Escriba su opcion porfavor: ")
        match choice_main:
            case "1":
                menu_estudiantes()
            case "2":
                menu_cursos()
            case "3":
                menu_universidad()
            case "4":
                gt.guardar_datos(db_json)
                gt.guardar_backup(db_backup)
                break
            case _:
                print("Opcion invalida")

def menu_estudiantes():
    info_estudiantes = gt.info_estudiantes()
    estudiantes = gt.cargar_datos_json_estudiantes()
    while True:
        print(
"""
1. Agregar infromacion de un estudiante
2. Modificar informacion de un estudiante
3. Eliminar informacion de un estudiante
4. Visualizar informacion de todos los estuadiantes
5. Volver atras
""")
        choice_estudiante = input("Escriba su opcion porfavor: ")
        match choice_estudiante:
            case "1":
                calificaciones = gt.datos_calificaciones()
                cursos = gt.info_cursos()
                info_estudiantes, calificaciones, cursos = gt.agregar_info_estudiante(info_estudiantes, calificaciones, cursos)
            case "2":
                info_estudiantes = gt.modificar_info_estudiante(info_estudiantes)
            case "3":
                info_estudiantes = gt.eliminar_info_estudiante(info_estudiantes, db_backup)
            case "4":
                gt.visualizar_estudiantes(info_estudiantes)
            case "5":
                estudiantes = gt.actualizar_info_estudiantes(info_estudiantes, estudiantes)
                estudiantes = gt.actualizar_info_calificaciones(calificaciones, estudiantes)
                estudiantes = gt.actualizar_info_cursos(cursos, estudiantes)
                db_json["info_estudiantes"] = estudiantes
            case _:
                print("Opcion invalida")

def menu_cursos():
    estudiantes = gt.cargar_datos_json_estudiantes()
    cursos = gt.cargar_datos_json_cursos()
    cursos_estudiante = gt.info_cursos()
    calificaciones = gt.datos_calificaciones()
    while True:
        print(
"""
1. Agregar curso
2. Modificar curso
3. Eliminar curso
4. Visualizar los cursos
5. Añadir curso a estudiante
6. Eliminar curso a estudiante
7. Añadir calificacion a estudiante
8. Eliminar calificacion a estudiante
9. Visualizar calificaciones
10. Volver atras
""")
        choice_curso = input("Escriba su opcion porfavor: ")
        match choice_curso:
            case "1":
                cursos = gt.agregar_curso(cursos)
            case "2":
                cursos = gt.modificar_curso(cursos)
            case "3":
                cursos = gt.eliminar_curso(cursos, db_backup)
            case "4":
                gt.visualizar_cursos(cursos)
            case "5":
                cursos_estudiante = gt.agregar_curso_estudiante(cursos, cursos_estudiante)
            case "6":
                cursos_estudiante = gt.eliminar_curso_estudiante(cursos_estudiante, db_backup)
            case "7":
                calificaciones = gt.Agregar_calificaciones(calificaciones)
            case "8":
                calificaciones = gt.eliminar_calificaciones(calificaciones, db_backup)
            case "9":
                gt.visualizar_calificaciones(calificaciones)
            case "10":
                estudiantes = gt.actualizar_info_calificaciones(calificaciones, estudiantes)
                estudiantes = gt.actualizar_info_cursos(cursos_estudiante, estudiantes)
                db_json["cursos"] = cursos
                break
            case _:
                print("Opcion invalida")

def menu_universidad():
    sedes = gt.cargar_datos_json_sedes()
    while True:
        print(
"""
1. Agregar sede de la universidad
2. Modificar sede de la universidad
3. Eliminar sede de la universidad
4. Visualizar sedes de la universidad
5. Volver atras
""")
        choice_universidad = input("Escriba su opcion porfavor: ")
        match choice_universidad:
            case "1":
                sedes = gt.agregar_sede(sedes)
            case "2":
                sedes = gt.modificar_sede(sedes)
            case "3":
                sedes = gt.eliminar_sede(sedes, db_backup)
            case "4":
                gt.visualizar_sedes(sedes)
            case "5":
                db_json["sedes"] = sedes
                break
            case _:
                print("Opcion invalida")

if __name__ == "__main__":
    menu_principal()