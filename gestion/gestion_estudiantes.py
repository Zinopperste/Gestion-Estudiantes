"""Lista estudiantes"""
listaEstudiantes = []

def agregar_estudiante (lista):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    lista.append(nombre_estudiante)
    print(f"El estudiante {nombre_estudiante} a sido agregado con exito")

agregar_estudiante(listaEstudiantes)
print(listaEstudiantes)