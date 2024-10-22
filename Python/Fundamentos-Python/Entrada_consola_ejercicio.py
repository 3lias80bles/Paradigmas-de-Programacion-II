'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 21 de octubre de 2024
Descripción:
Entrada de datos por consola para interactuar con el usuario con valores dinámicos.
'''

#Se piden dos números desde la consola y se realiza un cast de variables para que lo convierta en decimal
numero1_cadena = float(input("Introduce un número decimal: "))
numero2_cadena = float(input("Introduce otro número decimal que no sea cero: "))

#Se realizan las operaciónes basicas de suma, resta, multiplicación y división
suma=numero1_cadena+numero2_cadena
resta=numero1_cadena-numero2_cadena
mult=numero1_cadena*numero2_cadena
div=numero1_cadena/numero2_cadena

#Se imprimen los resultados de cada una de las operaciónes
print(f"El resultado de la suma de {numero1_cadena} y {numero2_cadena} es: {suma}")
print(f"El resultado de la resta de {numero1_cadena} y {numero2_cadena} es: {resta:.3f}")#Esta función sirve para determinar cuantos decimales desea despues del punto
print(f"El resultado de la multiplicación de {numero1_cadena} y {numero2_cadena} es: {mult}")
print(f"El resultado de la división de {numero1_cadena} y {numero2_cadena} es: {div:.3f}")