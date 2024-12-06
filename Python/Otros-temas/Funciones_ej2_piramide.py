'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 14 de Noviembre
Descripción: Ejercicio de mostrar piramides usando funciones.
'''

#funciones para las diferentes piramides, las funciones solo recibe el tamaño e imprime
def piramide1(tama):
    print("*** Pirámide 1 ***")
    for i in range(1, tama + 1):
        espacios = " " * (tama - i)
        asteriscos = "*" * i
        print(f"{asteriscos}{espacios}")
    print()

def piramide2(tama):
    print("*** Pirámide 2 ***")
    for i in range(1, tama + 1):
        asteriscos = "*" * ((tama - i) + 1)
        espacios = " " * i
        print(f"{asteriscos}{espacios}")
    print()

def piramide3(tama):
    print("*** Pirámide 3 ***")
    for i in range(1, tama + 1):
        espacios = " " * (tama - i)
        asteriscos = "*" * (2 * i - 1)
        print(f"{espacios}{asteriscos}")
    print()

def piramide4(tama):
    print("*** Pirámide 4 ***")
    for i in range(1, tama + 1):
        espacios = " " * (tama - i)
        asteriscos = "*" * i
        print(f"{espacios}{asteriscos}")
    print()

def piramide_extra(tama):
    print("*** Pirámide Extra ***")
    for i in range(1, tama + 1):
        asteriscos = "*" * ((tama - i) + 1)
        espacios = " " * (i - 1)
        print(f"{espacios}{asteriscos}")

# Se solicita el tamaño de la pirámide.
tama = int(input("Ingresa el número de filas de la pirámide: "))
print()

# Se llaman a las funciones para imprimir las pirámides.
piramide1(tama)
piramide2(tama)
piramide3(tama)
piramide4(tama)
piramide_extra(tama)


