def agregar_sede(sedes):
    nueva_sede = input("Escriba el nombre de la sede que quiere agregar: ")
    sedes = list(sedes)
    sedes.append(nueva_sede)
    sedes = tuple(sedes)
    print("Sede agregada con exito")
    return sedes

def modificar_sede(sedes):
    sede = input("Escriba el nombre de la sede que quiere modificar: ")
    sedes = list(sedes)
    if sede in sedes:
        indice = sede.index(sede)
        nueva_sede = input("Escriba el nuevo nombre de la sede: ")
        sedes.insert(indice, nueva_sede)
        sedes.remove(sede)
        sedes = tuple(sedes)
        print("Sede modificada con exito")
        return sedes
    else:
        print("Sede no encontrada")
        return tuple(sedes)

def eliminar_sede(sedes, db_backup):
    sede = input("Escriba el nombre de la sede a eliminar: ")
    sedes = list(sedes)
    if sede in sedes:
        db_backup['sedes'].append(sede)
        sedes.remove(sede)
        sedes = tuple(sedes)
        print("Sede eliminada con exito")
        return sedes
    else:
        print("Sede no encontrada")
        return tuple(sedes)

def visualizar_sedes(sedes):
    print("Listado de Sedes:")
    print("-------------------")
    
    for sede in sedes:
        print(f"Nombre del Curso: {sede}")
        print("-------------------")