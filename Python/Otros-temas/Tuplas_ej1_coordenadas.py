'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 13 de Noviembre
Descripción: Ejercicio de coordenadas usando tuplas y funciones.
'''

#Inicialización de variables.
i=0
opcion=7
coordenadas = []

def menu ():
    print()
    print("*** Rectas a partir de puntos (coordenadas) en el plano cartesiano ***")
    print("Ver coordenadas almacenadas..............................................[1]")
    print("Agregar coordenada (x,y).................................................[2]")
    print("Calcular la pendiente y la ecuación de la recta entre dos coordenadas....[3]")
    print("Eliminar coordenada (x,y)................................................[4]")
    print("Salir....................................................................[0]")
    print()

#funciones de operaciones.
def ver(coordenadas):
    if len(coordenadas):
        print("Coordenadas almacenadas:")
        j = 1
        for coord in coordenadas:
            x, y = coord
            print(f"{j}: ({x}, {y})")
            j += 1
    else:
        print("No hay coordenadas para mostrar.")


def agregar(coordenadas):
        x = float(input("Ingrese la coordenada x: "))
        y = float(input("Ingrese la coordenada y: "))
        coordenadas.append((x, y))
        print(f"Coordenada ({x}, {y}) agregada.")

def calcular(coordenadas):
    if len(coordenadas) < 2:
        print("Debe haber al menos dos coordenadas para calcular la recta.")
        return
    else:
        if len(coordenadas):
            print("Coordenadas almacenadas:")
            j = 1
            for coord in coordenadas:
                x, y = coord
                print(f"[{j}]....({x}, {y})")
                j += 1
        else:
            print("No hay coordenadas para mostrar.")

        indice1 = int(input("Seleccione el índice de la primera coordenada: "))
        indice2 = int(input("Seleccione el índice de la segunda coordenada: "))

        if indice1 < 1 or indice2 < 1 or indice1 >= len(coordenadas) or indice2 >= len(coordenadas):
            print("Favor de ingresar un indice valido..")
            return

        x1, y1 = coordenadas[indice1-1]
        x2, y2 = coordenadas[indice2-1]

        print(f"Ha seleccionado las coordenadas ({x1}, {y1}) y ({x2}, {y2}).")

        pendiente = (y2 - y1) / (x2 - x1)
        intercepto = y1 - pendiente * x1

        print(f"La pendiente entre la coordenada ({x1}, {y1}) y la ({x2}, {y2}) es {pendiente:.2f}.")
        print(f"La ecuación de la recta es: y = {pendiente:.2f}x + {intercepto:.2f}")

def eliminar(coordenadas):
    if len(coordenadas):
        print("*** Coordenadas actuales ***")
        for i in range(len(coordenadas)):
            print(f"[{i + 1}]....{coordenadas[i]}")
        elim = int(input("Ingrese el indice del video a eliminar: "))
        if 1 <= elim <= len(coordenadas):
            eliminado = coordenadas.pop(elim - 1)
            print(f"El video '{eliminado}' ha sido eliminado.")
        else:
            print("Favor de ingresar un indice de coordenadas valido.")
    else:
        print("No hay coordenadas para eliminar.")


#Bucle para el menú principal de la calculadora.
while opcion!=0:
    menu()
    #Se solicitar una opción al usuario.
    opcion=int(input("Su opción es: "))

    # Opción para salir del programa.
    if opcion == 0:
        print("Adios...")

    #Ver coordenadas almacenadas.
    elif opcion == 1:
        ver(coordenadas)

    #Agregar coordenada (x,y).
    elif opcion == 2:
        agregar(coordenadas)

    #Calcular la pendiente y la ecuación de la recta entre dos coordenadas.
    elif opcion == 3:
        calcular(coordenadas)

    #Eliminar coordenada (x,y).
    elif opcion == 4:
        eliminar(coordenadas)

    # Opciones no válidas.
    else:
        print()
        print("Seleccione una opción valida.")

