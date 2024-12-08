'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: En este trabajo se usan listas y funciones para realizar una playlist de videos.
'''

#Inicialización de variables.
i=0
opcion=7
playlist = []

def menu ():
    print()
    print("*** Playlist de videos de YouTube ***")
    print("Ver playlist por videos añadidos...................[1]")
    print("Ver playlist por orden ascendente (A-Z)............[2]")
    print("Ver playlist por orden descendente (Z-A)...........[3]")
    print("Añadir video de YouTube a la playlist..............[4]")
    print("Añadir varios videos de YouTube a la playlist......[5]")
    print("Eliminar video de la playlist......................[6]")
    print("Salir..............................................[0]")
    print()


#funciones de operaciones.
def por_ingreso():
    if len(playlist):
        print("*** Playlist actual ***")
        for i in range(len(playlist)):
            print(f"[{i + 1}]....{playlist[i]}")
    else:
        print("No hay videos para mostrar.")

def acendente():
    playlist.sort()
    if len(playlist):
        print("*** Playlist actual por orden ascendente (A-Z) ***")
        for i in range(len(playlist)):
            print(f"[{i + 1}]....{playlist[i]}")
    else:
        print("No hay videos para mostrar.")
    print()

def decendente():
    print("*** Playlist actual por orden descendente (Z-A) ***")
    if len(playlist):
        playlist.sort(reverse=True)
        for i in range(len(playlist)):
            print(f"[{i + 1}]....{playlist[i]}")
    else:
        print("No hay videos para mostrar.")
    print()

def agregar():
    nuevo = input("Ingrese el nombre del video a agregar a la playlist: ")
    playlist.append(nuevo)
    print("Video agregado exitosamente.")
    print()

def agregar_muchos():
    cantidad = int(input("Ingrese la cantidad de videos a agregar: "))
    for i in range(cantidad):
        nuevo = input(f"Ingrese el nombre del video {i + 1}: ")
        playlist.append(nuevo)
    print("Videos agregados exitosamente.")
    print()

def eliminar():
    if len(playlist):
        print("*** Playlist actual ***")
        for i in range(len(playlist)):
            print(f"[{i + 1}]....{playlist[i]}")
        elim = int(input("Ingrese el indice del video a eliminar: "))
        if 1 <= elim <= len(playlist):
            eliminado = playlist.pop(elim - 1)
            print(f"El video '{eliminado}' ha sido eliminado.")
        else:
            print("Favor de ingresar un indice de video valido.")
    else:
        print("No hay videos para eliminar.")


#Bucle para el menú principal de la calculadora.
while opcion!=0:
    menu()
    #Se solicitar una opción al usuario.
    opcion=int(input("Su opción es: "))

    # Opción para salir del programa.
    if opcion == 0:
        print("Adios...")
    #Ver playlist por videos añadidos
    elif opcion == 1:
        por_ingreso()

    #Ver playlist por orden ascendente (A-Z)
    elif opcion == 2:
        acendente()

    #Ver playlist por orden descendente (Z-A)
    elif opcion == 3:
        decendente()

    #Añadir video de YouTube a la playlist.
    elif opcion == 4:
        agregar()

    #Añadir varios videos de YouTube a la playlist.
    elif opcion == 5:
        agregar_muchos()

    #Eliminar video de la playlist.
    elif opcion == 6:
        eliminar()

    # Opciones no válidas.
    else:
        print()
        print("Seleccione una opción valida.")

