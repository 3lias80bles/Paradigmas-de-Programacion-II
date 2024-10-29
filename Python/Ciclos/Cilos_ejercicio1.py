'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 24 de Octubre de 2024
Descripción: Ejercicio del ciclo while que imprime una suma de 1 a n
'''

print("*** Programa que calcula la suma acumulativa ***")
num = int(input("Ingrese el número final: "))  #Se pide un número entero.
i = 1  #Se inicializa el contador en 1.
suma = 0  #Se inicializa la suma en 0.

while i <= num:  #Un ciclo desde 1 hasta n.
    suma = suma + i  #Se acumula el valor de i en la variable suma.
    i = i + 1  #Se incrementa el contador de 1 en 1.

print()
print(f"La suma de 1 hasta {num} es: {suma}")  #Se imprime la suma acumulativa desde 1 hasta n.
