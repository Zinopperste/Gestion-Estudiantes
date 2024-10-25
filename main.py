import os

while True:
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE LA UNIVERSIDAD APLAPLAC - SEDE CONCEPCIÓN")
    options = input(
"""
Menú:
1) Gestión de Estudiantes
2) Gestión de Cursos
3) Gestión Universidad
""")

    match options:
        
#Menú para la gestión de los estudiantes
        case "1":
            os.system("cls")
            print("GESTIÓN DE ESTUDIANTES")
            options = input(
"""
1) Añadir Datos Personales Estudiante
2) Actualizar Datos Personales del Estudiante
3) Visualizar Lista de Estudiantes
""")
            match options:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                
#Menú para la gestion de los cursos y calificaciónes
        case "2":
            os.system("cls")
            print("GESTIÓN DE CURSOS")
            options = input(
"""
1) Añadir Cursos a Estudiantes
2) Añadir Calificación a Estudiantes
3) Añadir Nuevo Curso
""")
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
1) Eliminar Datos del Estudiante
2) Actualizar Calificaciones del Estudiante
3) Recuperar Datos del Estudiante
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