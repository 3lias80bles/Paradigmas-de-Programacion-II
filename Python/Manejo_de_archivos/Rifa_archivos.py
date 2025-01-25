'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 19 de Enero de 2025
Descripción: Rifa de una computadora registrada con archivos
'''

import random

# Función para mostrar el menú.
def menu():
    print("****Rifa de computadora****")
    print()
    print("Ver correos de participantes....................[1]")
    print("Agregar correo de participante..................[2]")
    print("Eliminar correo de participante.................[3]")
    print("Seleccionar ganador.............................[4]")
    print("Ver ganadores registrados.......................[5]")
    print("Salir...........................................[0]")

# Función para mostrar los correos electrónicos registrados en la rifa.
def ver_correos(participantes):
    if participantes:
        print("Correos de los participantes:")
        for i, correo in enumerate(participantes, 1):
            print(f"{i}. {correo}")
    else:
        print("No hay participantes registrados.")

# Función para agregar un nuevo correo al conjunto de participantes.
def agregar_correo(participantes):
    correo = input("Ingrese el correo electrónico del participante: ")
    if correo in participantes:
        print("El correo ya está registrado. Intente con otro.")
    else:
        participantes.add(correo)
        print(f"El correo {correo} se ha registrado correctamente.")

# Función para eliminar un correo del conjunto de participantes.
def eliminar_correo(participantes):
    if participantes:
        ver_correos(participantes)
        correo = input("Ingrese el correo electrónico que desea eliminar: ")
        if correo in participantes:
            participantes.remove(correo)
            print(f"El correo {correo} se ha eliminado correctamente.")
        else:
            print("El correo no está registrado.")
    else:
        print("No hay participantes registrados para eliminar.")

# Función para seleccionar al ganador de la rifa y registrarlo en un archivo.
def seleccionar_ganador(participantes):
    if participantes:
        try:
            lista_participantes = list(participantes)
            ganador = random.choice(lista_participantes)
            print(f"¡El correo ganador es: {ganador}!")

            # Registrar el ganador en un archivo.
            with open("ganadores.txt", "a") as archivo:
                archivo.write(ganador + "\n")

            # Remover al ganador del conjunto de participantes.
            participantes.remove(ganador)
            print("El ganador ha sido registrado y eliminado de los participantes.")
        except Exception as e:
            print(f"Ocurrió un error al seleccionar al ganador: {e}")
    else:
        print("No hay participantes registrados para la rifa.")

# Función para mostrar los ganadores registrados en el archivo.
def ver_ganadores():
    try:
        with open("ganadores.txt", "r") as archivo:
            ganadores = archivo.readlines()
            if ganadores:
                print("Ganadores registrados:")
                for i, ganador in enumerate(ganadores, 1):
                    print(f"{i}. {ganador.strip()}")
            else:
                print("No hay ganadores registrados aún.")
    except FileNotFoundError:
        print("El archivo de ganadores no existe. No hay ganadores registrados aún.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo de ganadores: {e}")

# Bloque principal del programa
participantes = set()

# Ciclo principal que muestra el menú y procesa las opciones del usuario.
opcion = -1
while opcion != 0:
    menu()
    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ver_correos(participantes)
        elif opcion == 2:
            agregar_correo(participantes)
        elif opcion == 3:
            eliminar_correo(participantes)
        elif opcion == 4:
            seleccionar_ganador(participantes)
        elif opcion == 5:
            ver_ganadores()
        elif opcion == 0:
            print("Saliendo.....")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    except ValueError:
        print("Por favor ingrese un número.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
