import gestion as gt
import os
import msvcrt

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
                msvcrt.getch()

def menu_estudiantes():
    info_estudiantes = db_json["estudiantes"]["info_estudiantes"]
    estudiantes = db_json["estudiantes"]
    calificaciones = db_json["estudiantes"]["calificaciones"]
    cursos = db_json["estudiantes"]["cursos"]
    while True:
        os.system('cls')
        print(
"""
1. Agregar infromacion de un estudiante
2. Modificar informacion de un estudiante
3. Eliminar informacion de un estudiante
4. Visualizar informacion de todos los estuadiantes
5. Volver atras
""")
        choice_estudiante = input("Escriba su opcion porfavor: ")
        os.system('cls')
        match choice_estudiante:
            case "1":
                info_estudiantes, calificaciones, cursos = gt.agregar_info_estudiante(info_estudiantes, calificaciones, cursos)
                msvcrt.getch()
                os.system('cls')
            case "2":
                gt.visualizar_estudiantes(info_estudiantes)
                msvcrt.getch()
                os.system('cls')
                info_estudiantes = gt.modificar_info_estudiante(info_estudiantes)
                msvcrt.getch()
                os.system('cls')
            case "3":
                gt.visualizar_estudiantes(info_estudiantes)
                msvcrt.getch()
                os.system('cls')
                info_estudiantes = gt.eliminar_info_estudiante(info_estudiantes, db_backup)
                msvcrt.getch()
                os.system('cls')
            case "4":
                gt.visualizar_estudiantes(info_estudiantes)
                msvcrt.getch()
                os.system('cls')
            case "5":
                estudiantes = gt.actualizar_info_estudiantes(info_estudiantes, estudiantes)
                estudiantes = gt.actualizar_info_calificaciones(calificaciones, estudiantes)
                estudiantes = gt.actualizar_info_cursos(cursos, estudiantes)
                db_json["info_estudiantes"] = estudiantes
                break
            case _:
                print("Opcion invalida")
                msvcrt.getch()

def menu_cursos():
    estudiantes = db_json["estudiantes"]
    cursos = db_json["cursos"]
    cursos_estudiante = db_json["estudiantes"]["cursos"]
    calificaciones = db_json["estudiantes"]["calificaciones"]
    while True:
        os.system('cls')
        print(
"""
1. Agregar curso
2. Modificar curso
3. Eliminar curso
4. Visualizar los cursos
5. Añadir curso a estudiante
6. Eliminar curso a estudiante
7. Visualizar cursos de estudiantes
8. Añadir calificacion a estudiante
9. Eliminar calificacion a estudiante
10. Visualizar calificaciones
11. Volver atras
""")
        choice_curso = input("Escriba su opcion porfavor: ")
        os.system('cls')
        match choice_curso:
            case "1":
                cursos = gt.agregar_curso(cursos)
                msvcrt.getch()
                os.system('cls')
            case "2":
                gt.visualizar_cursos(cursos)
                msvcrt.getch()
                os.system('cls')
                cursos = gt.modificar_curso(cursos)
                msvcrt.getch()
                os.system('cls')
            case "3":
                gt.visualizar_cursos(cursos)
                msvcrt.getch()
                os.system('cls')
                cursos = gt.eliminar_curso(cursos, db_backup)
                msvcrt.getch()
                os.system('cls')
            case "4":
                gt.visualizar_cursos(cursos)
                msvcrt.getch()
                os.system('cls')
            case "5":
                cursos_estudiante = gt.agregar_curso_estudiante(cursos, cursos_estudiante)
                msvcrt.getch()
                os.system('cls')
            case "6":
                cursos_estudiante = gt.eliminar_curso_estudiante(cursos_estudiante, db_backup)
                msvcrt.getch()
                os.system('cls')
            case "7":
                gt.visualizar_cursos_estudiantes(cursos_estudiante)
                msvcrt.getch()
                os.system('cls')
            case "8":
                gt.visualizar_calificaciones(calificaciones)
                msvcrt.getch()
                os.system('cls')
                calificaciones = gt.Agregar_calificaciones(calificaciones)
                msvcrt.getch()
                os.system('cls')
            case "9":
                gt.visualizar_calificaciones(calificaciones)
                msvcrt.getch()
                os.system('cls')
                calificaciones = gt.eliminar_calificaciones(calificaciones, db_backup)
                msvcrt.getch()
                os.system('cls')
            case "10":
                gt.visualizar_calificaciones(calificaciones)
                msvcrt.getch()
                os.system('cls')
            case "11":
                estudiantes = gt.actualizar_info_calificaciones(calificaciones, estudiantes)
                estudiantes = gt.actualizar_info_cursos(cursos_estudiante, estudiantes)
                db_json["cursos"] = cursos
                break
            case _:
                print("Opcion invalida")
                msvcrt.getch()

def menu_universidad():
    sedes = db_json["sedes"]
    while True:
        os.system('cls')
        print(
"""
1. Agregar sede de la universidad
2. Modificar sede de la universidad
3. Eliminar sede de la universidad
4. Visualizar sedes de la universidad
5. Volver atras
""")
        choice_universidad = input("Escriba su opcion porfavor: ")
        os.system('cls')
        match choice_universidad:
            case "1":
                sedes = gt.agregar_sede(sedes)
                msvcrt.getch()
                os.system('cls')
            case "2":
                gt.visualizar_sedes(sedes)
                msvcrt.getch()
                os.system('cls')
                sedes = gt.modificar_sede(sedes)
                msvcrt.getch()
                os.system('cls')
            case "3":
                gt.visualizar_sedes(sedes)
                msvcrt.getch()
                os.system('cls')
                sedes = gt.eliminar_sede(sedes, db_backup)
                msvcrt.getch()
                os.system('cls')
            case "4":
                gt.visualizar_sedes(sedes)
                msvcrt.getch()
                os.system('cls')
            case "5":
                db_json["sedes"] = sedes
                break
            case _:
                print("Opcion invalida")

if __name__ == "__main__":
    menu_principal()