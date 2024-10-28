'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 17 de Octubre de 2024
Descripción: En este ejercicio se muestran los operadores aritméticos: +, -, *, /, %, ** y //.
'''

print("*** Operadores aritméticos ***")
num1 = int(input("Ingrese un número: "))  # Se solicitan datos de consola en este caso enteros.
num2 = int(input("Ingrese otro número:"))

# En una variable llamada suma asignamos la suma del primer número y el segundo.
suma = num1 + num2
# En una variable llamada resta asignamos la resta del primer número y el segundo.
resta = num1 - num2
# En una variable llamada mult asignamos la multiplicación del primer número y el segundo.
mult = num1 * num2
# En una variable llamada div asignamos la división del primer número y el segundo.
div = num1 / num2
# En una variable llamada modulo, asignamos el módulo del primer número respecto al segundo número.
modulo = num1 % num2
# En una variable llamada potencia asignamos el primer número elevado a la potencia del segundo número.
potencia = num1 ** num2
# En una variable llamada div_entera asignamos la división entera del primer número y el segundo.
div_entera = num1 // num2

'''
Estas operaciones pueden realizarse de diversas formas. Una opción es almacenar
todos los resultados en una misma variable o realizar la operación directamente en la impresión.
'''

# Se imprimen los resultados de las operaciones anteriores.
print(f"El resultado de la suma del número {num1} y {num2} es: {suma}")
print(f"El resultado de la resta del número {num1} y {num2} es: {resta}")
print(f"El resultado de la multiplicación del número {num1} y {num2} es: {mult}")
print(f"El resultado de la división del número {num1} y {num2} es: {div:.3f}")
print(f"El resultado del número {num1} con módulo {num2} es: {modulo}")
print(f"El resultado de la potencia del número {num1} elevado a {num2} es: {potencia}")
print(f"El resultado de la división entera del número {num1} y {num2} es: {div_entera}")
