'''
Nombre: Sergio Elias Robles Ignacio
Fecha:17 de Octubre de 2024
Descripción:
'''

print("ingrese un número: ")
num1=int(input("ingrese número 1: "))
num2=int(input("ingrese número 2:"))


suma=num1 + num2
resta=num1 - num2
mult=num1 * num2
div=num1 / num2
modulo=num1 % num2
n=num1**num2
r=num1//num2

print(f"El resultado de la suma del número {num1} y {num2} es: {suma}")
print(f"El resultado de la resta del número {num1} y {num2} es: {resta}")
print(f"El resultado de la multiplicación del número {num1} y {num2} es: {mult}")
print(f"El resultado de la división del número {num1} y {num2} es: {div:.3f}")
print(f"El resultado del módulo del número {num1} y {num2} es: {modulo}")
print(f"El resultado de la potencia del número {num1} y {num2} es: {n}")
print(f"El resultado de la division entera del número {num1} y {num2} es: {r}")