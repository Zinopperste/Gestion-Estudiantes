import os
import gestion as gt
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
            os.system("cls")
            gt.menu_estudiantes()

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