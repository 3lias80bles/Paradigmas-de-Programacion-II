'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 19 de enero de 2024
Descripción: Implementación del juego de piedra, papel, tijera, lagarto o Spock con archivos.
'''

import random  # Se importa la librería random para números aleatorios.

# Diccionario para determinar el resultado basado en las opciones.
reglas = {
    "Piedra": {"Piedra": "Empate", "Papel": "CPU", "Tijera": "Jugador", "Lagarto": "Jugador", "Spock": "CPU"},
    "Papel": {"Piedra": "Jugador", "Papel": "Empate", "Tijera": "CPU", "Lagarto": "CPU", "Spock": "Jugador"},
    "Tijera": {"Piedra": "CPU", "Papel": "Jugador", "Tijera": "Empate", "Lagarto": "Jugador", "Spock": "CPU"},
    "Lagarto": {"Piedra": "CPU", "Papel": "Jugador", "Tijera": "CPU", "Lagarto": "Empate", "Spock": "Jugador"},
    "Spock": {"Piedra": "Jugador", "Papel": "CPU", "Tijera": "Jugador", "Lagarto": "CPU", "Spock": "Empate"}
}

# Inicialización de variables.
victorias_jugador = 0
victorias_cpu = 0
empates = 0

# Función para mostrar las reglas del juego.
def mostrar_reglas():
    print("\n*** Reglas del juego ***")
    print("- Tijera corta Papel.")
    print("- Papel cubre Piedra.")
    print("- Piedra aplasta Lagarto.")
    print("- Lagarto envenena Spock.")
    print("- Spock rompe Tijera.")
    print("- Tijera decapita Lagarto.")
    print("- Lagarto devora Papel.")
    print("- Papel desautoriza Spock.")
    print("- Spock vaporiza Piedra.")
    print("- Piedra aplasta Tijera.")
    print()

# Función para registrar el historial de jugadas en un archivo.
def registrar_historial(jugador, cpu, resultado,victorias_jugador,empates,victorias_cpu):
    try:
        with open("historial_jugadas.txt", "a") as archivo:
            archivo.write(f"Victorias del jugador: {victorias_jugador}, empates: {empates}, victorias de la CPU: {victorias_cpu}\n")
            archivo.write(f"Jugador: {jugador}, CPU: {cpu}, Resultado: {resultado}\n")
    except Exception as e:
        print(f"Error al registrar el historial: {e}")

# Bucle para el menú principal del juego.
while True:
    try:
        print()
        print("*** Juego de piedra, papel, tijera, lagarto o Spock ***")
        # Se muestran las estadísticas del juego.
        print(f"Victorias del jugador: {victorias_jugador}, empates: {empates}, victorias de la CPU: {victorias_cpu}.")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        print("4. Lagarto")
        print("5. Spock")
        print("6. Ver reglas del juego")
        print("0. Salir")
        print()

        # Se solicita una opción al usuario.
        opcion = int(input("Su opción es: "))
        if opcion == 0:
            print("Fin del juego...")
            break
        elif opcion == 6:
            mostrar_reglas()
            continue
        elif opcion < 0 or opcion > 6:  # Verifica que la opción sea válida.
            print("Opción no válida. Intente nuevamente.")
            continue

        # Convierte la opción del jugador a texto.
        if opcion == 1:
            opcion_jugador = "Piedra"
        elif opcion == 2:
            opcion_jugador = "Papel"
        elif opcion == 3:
            opcion_jugador = "Tijera"
        elif opcion == 4:
            opcion_jugador = "Lagarto"
        else:
            opcion_jugador = "Spock"

        # Genera una opción aleatoria para la CPU.
        opcion_CPU_numero = random.randint(1, 5)
        if opcion_CPU_numero == 1:
            opcion_CPU = "Piedra"
        elif opcion_CPU_numero == 2:
            opcion_CPU = "Papel"
        elif opcion_CPU_numero == 3:
            opcion_CPU = "Tijera"
        elif opcion_CPU_numero == 4:
            opcion_CPU = "Lagarto"
        else:
            opcion_CPU = "Spock"

        # Determina el resultado del juego.
        resultado = reglas[opcion_jugador][opcion_CPU]
        if resultado == "Empate":
            empates += 1
        elif resultado == "Jugador":
            victorias_jugador += 1
        else:
            victorias_cpu += 1

        # Registra el resultado en el historial de jugadas.
        registrar_historial(opcion_jugador, opcion_CPU, resultado,victorias_jugador, empates, victorias_cpu)

        # Imprime el resultado del juego.
        print(f"Jugador: {opcion_jugador}, CPU: {opcion_CPU}. Resultado: {resultado}.")
    except Exception as e:
        print(f"Favor de ingresar un número  {e}")
