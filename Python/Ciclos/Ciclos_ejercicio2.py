'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 24 de Octubre de 2024
Descripción: Ejercicio del ciclo while que imprime una suma de un número inicial hasta un número final.
'''

print("*** Programa que calcula la suma acumulativa ***")
num_ini=int(input("Ingrese el número inicial: "))#Se pide un número entero inicial.
num_fin=int(input("Ingrese el número final: "))#Se pide un número entero final.
i=num_ini#Se inicializa el contador con el número inicial.
suma=0#Se inicializa la suma en 0.
while i<=num_fin:#Un ciclo desde número inicial hasta número final.
    suma=suma+i#Se acumula el valor de i en la variable suma.
    i=i+1#Se incrementa el contador de 1 en 1.
print()
print(f"La suma de {num_ini} hasta {num_fin} es: {suma}")#Se imprime la suma acumulativa desde el número inicial hasta el número final.