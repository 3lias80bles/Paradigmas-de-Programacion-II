
import random  # Se importa la librería random para números aleatorios.

# Inicialización de variables.
num_intento = 1  # Contador de intentos
num_adivinar = random.randint(1, 100)  # Se genera el número a adivinar antes del bucle

# Abre el archivo en modo de escritura para registrar el historial.
with open("historial_adivinador.txt", "a") as archivo_historial:
    archivo_historial.write("*** Nuevo Juego ***\n")
    archivo_historial.write(f"Número a adivinar: {num_adivinar}\n")

    # Bucle para el juego, solo tenemos 5 intentos.
    while num_intento <= 5:
        print()
        print("*** Juego del adivinador ***")
        # Se solicita un número y marca el número de intentos.
        try:
            numero = int(input(f"Número de intento {num_intento}. Ingresa un número (1-100): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        # Escribe el intento en el archivo.
        archivo_historial.write(f"Intento {num_intento}: {numero}\n")

        # Verifica si el número ingresado es menor, mayor o igual al número a adivinar.
        if numero < num_adivinar:
            print("El número a adivinar es mayor.")
        elif numero > num_adivinar:
            print("El número a adivinar es menor.")
        else:
            print(f"¡Felicidades! Adivinaste en {num_intento} intentos.")
            archivo_historial.write(f"Resultado: Ganaste en {num_intento} intentos.\n\n")
            break  # Se rompe el bucle al adivinar correctamente.

        num_intento += 1  # Se incrementa el contador.

    # Si el contador pasa de los 5 intentos imprime y guarda lo siguiente.
    if num_intento > 5:
        print(f"Perdiste. El número era {num_adivinar}.")
        archivo_historial.write(f"Resultado: Perdiste. El número era {num_adivinar}.\n\n")
