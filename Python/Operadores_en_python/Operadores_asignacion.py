'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 17 de Octubre de 2024
Descripción: En este programa se realizan diferentes asignaciones que podemos realizar en Python.
'''

# Asignación múltiple
print("*** Asignación múltiple ***")
# En este caso asignamos valores a más de un número,
# para realizar esta acción se separan con una coma las
# variables donde se almacenarán los valores junto con los mismos valores.
num1, num2 = 7, 10
# Imprimimos esos valores.
print(num1)
print(num2)

# Se asignan valores enteros y cadenas con la misma estructura, separados por comas.
num3, cad, num4 = 7, "hello", 10
# Imprimimos esos valores.
print(num3)
print(cad)
print(num4)

# También se pueden realizar operaciones y asignarlas de la misma forma que en el ejemplo anterior.
suma, resta = num1 + num2, num3 - num4
# Imprimimos esos valores.
print(suma)
print(resta)

print()
# Asignación en cadena
print("*** Asignación en cadena ***")
# Aquí se asigna el valor de 12 a 3 diferentes variables.
num5 = num6 = num7 = 12
# Se imprimen los 3 números, en este caso los 3 son 12.
print(num5)
print(num6)
print(num7)

print()
# Intercambio de variables
print("*** Intercambio de variables ***")
num8 = int(input("Ingresa un número: "))
num9 = int(input("Ingresa otro número: "))
print("Valores iniciales - Primer número:", num8, "Segundo número:", num9)

# Se hace un intercambio de variables.
# Asignando los valores a sus mismos valores pero invertidos
# esto nos evita estar usando una variable auxiliar.
num8, num9 = num9, num8
print("Valores finales - Primer número:", num8, "Segundo número:", num9)

print()
# Múltiples valores de entrada
print("*** Múltiples valores de entrada ***")
# Se asignan dos valores al mismo tiempo que se ingresan.
num10, num11 = int(input("Ingrese un número: ")), int(input("Ingrese otro número: "))
# Se imprimen los valores.
print(num10, num11)
