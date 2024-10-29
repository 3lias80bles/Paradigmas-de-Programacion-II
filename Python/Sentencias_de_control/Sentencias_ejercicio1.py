'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 23 de Octubre de 2024
Descripción: Ejercicio para ver el funcionamiento del if_elif_else
'''
print("*** Programa que determina cuál de dos números es menor ***")

#Se solicita al usuario que ingrese dos números, se convierten a tipo float.
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))

#Se compara el primer número con el segundo.
if num1 < num2:  #Si num1 es menor que num2:
    print(f"El número {num1} es menor que {num2}")  #Se imprime num1<num2
elif num1 > num2:  #Entonces, si num1 es mayor que num2 se imprime:
    print(f"El número {num2} es menor que {num1}")  #Se imprime num2<num1
else:  #Si no, entonces num1 y num2 son iguales:
    print(f"El número {num2} es igual a {num1}")  #Se imprime num1==num2
