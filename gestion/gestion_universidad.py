def agregar_sede(sedes):
    nueva_sede = input("Escriba el nombre del curso que quiere agregar: ")
    sedes = list(sedes)
    sedes.append(nueva_sede)
    sedes = tuple(sedes)
    return sedes

def modificar_sede(sedes):
    sede = input("Cual sede quiere modificar?: ")
    sedes = list(sedes)
    if sede in sedes:
        indice = sede.index(sede)
        nueva_sede = input("Como se llamara la sede?: ")
        sedes.insert(indice, nueva_sede)
        sedes = tuple(sedes)
        return sedes
    else:
        sedes = tuple(sedes)
        print("Sede no encontrada")

def eliminar_sede(sedes, db_backup):
    sede = input("Cual sede quiere modificar?: ")
    sedes = list(sedes)
    if sede in sedes:
        db_backup['sedes'].append(sede)
        sedes.remove(sede)
        sedes = tuple(sedes)
        return sedes
    else:
        sedes = tuple(sedes)
        print("Sede no encontrada")

def visualizar_sedes(sedes):
    print("Listado de Sedes:")
    print("-------------------")
    
    for sede in sedes:
        print(f"Nombre del Curso: {sede}")
        print("-------------------")