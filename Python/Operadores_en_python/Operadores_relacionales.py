'''
Nombre: Sergio Elias Robles Ignacio
Fecha:18 de Octubre de 2024
Descripción:
'''

num1=float(input("ingrese un número: "))
num2=float(input("ingrese el segundo número: "))

mayor=num1>num2
print(f"¿El número {num1:.2f} es mayor que {num2:.2f}?: {mayor}")

mayor_igual=num1>=num2
print(f"¿El número {num1:.2f} es mayor igual que {num2:.2f}?: {mayor_igual}")

menor=num1<num2
print(f"¿El número {num1:.2f} es menor que {num2:.2f}?: {menor}")

menor_igual=num1<=num2
print(f"¿El número {num1:.2f} es menor igual que {num2}?: {mayor_igual}")

igual=num1==num2
print(f"¿El número {num1:.2f} es igual que {num2:.2f}?: {igual}")

diferente=num1!=num2
print(f"¿El número {num1:.2f} es diferente que {num2:.2f}?: {diferente}")

print(f"¿El número {num1:.2f} es diferente  que {num2:.2f}?: {num1!=num2}")