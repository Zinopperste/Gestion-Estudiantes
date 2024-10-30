import os
import gestion as gt

def menu_estudiantes():
    listaEstudiantes = gt.cargar_datos()
    while True:
        os.system("cls")
        print("GESTIÓN DE ESTUDIANTES")
        option = input(
"""
1) Añadir Datos Personales Estudiante
2) Actualizar Datos Personales del Estudiante
3) Visualizar Lista de Estudiantes
4) Eliminar Datos del Estudiante
5) Guardar y Salir
""")
        match option:
            case "1":
                listaEstudiantes = gt.agregar_estudiante(listaEstudiantes)
            case "2":
                listaEstudiantes = gt.modificar_datos_estudiante(listaEstudiantes)
            case "3":
                gt.visualizar_estudiantes(listaEstudiantes)
                input("Presione una tecla para continuar ")
            case "4":
                listaEstudiantes = gt.eliminar_estudiante(listaEstudiantes)
            case "5":
                gt.guardar_datos(listaEstudiantes)
                break


while True:
    os.system("cls")
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE LA UNIVERSIDAD APLAPLAC - SEDE CONCEPCIÓN")
    options = input(
"""
Menú:
1) Gestión de Estudiantes
2) Gestión de Cursos
3) Gestión Universidad
4) Salir del Sistema
""")

    match options:
        
#Menú para la gestión de los estudiantes
        case "1":
            menu_estudiantes()

#Menú para la gestion de los cursos y calificaciónes
        case "2":
            os.system("cls")
            match options:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
        
#Menú para la gestión de la universidad 
        case "3":
            os.system("cls")
            print("GESTIÓN DE LA UNIVERSIDAD")
            options = input(
"""
?) Recuperar Datos del Estudiante
""")
            match options:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
        
#Salir del sistema
        case "4":
            os.system("cls")
            print("SALISTE DEL SISTEMA DE GESTIÓN")
            break
        
#En el caso que coloque una opción incorrecta 
        case _:
            print("Elige una de las opciones válidas")