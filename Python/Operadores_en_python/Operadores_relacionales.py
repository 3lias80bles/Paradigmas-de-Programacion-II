'''
Nombre: Sergio Elias Robles Ignacio
Fecha:18 de Octubre de 2024
Descripción: En este progrma se realizan comparaciones basicas con los operadores relacionales.
'''

# Solicita al usuario ingresar dos números  en este caso son de tipo flotante decimal
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese el segundo número: "))

#Se usa la función de {num1:.2f} para todos los casos esto para saber cuantos decimales tendra el número.
#Se compara si el primer número es mayor que el segundo.
mayor = num1 > num2
print(f"¿El número {num1:.2f} es mayor que {num2:.2f}?: {mayor}")

#Se compara si el primer número es mayor o igual al segundo.
mayor_igual = num1 >= num2
print(f"¿El número {num1:.2f} es mayor o igual que {num2:.2f}?: {mayor_igual}")

#Se compara si el primer número es menor que el segundo.
menor = num1 < num2
print(f"¿El número {num1:.2f} es menor que {num2:.2f}?: {menor}")

#Se compara si el primer número es menor o igual al segundo.
menor_igual = num1 <= num2
print(f"¿El número {num1:.2f} es menor o igual que {num2:.2f}?: {menor_igual}")

#Se compara si el primer número es igual al segundo.
igual = num1 == num2
print(f"¿El número {num1:.2f} es igual que {num2:.2f}?: {igual}")

#Se compara si el primer número es diferente al segundo.
diferente = num1 != num2
print(f"¿El número {num1:.2f} es diferente que {num2:.2f}?: {diferente}")

# Otra manera de imprimir la comparación de diferencia es ponerla directamente en el print.
print(f"¿El número {num1:.2f} es diferente que {num2:.2f}?: {num1 != num2}")
