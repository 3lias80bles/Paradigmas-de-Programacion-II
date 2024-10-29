'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 17 de octubre de 2024
Descripción: En este trabajo se muestra el funcionamiento de un operador lógico.
'''

print("** Bonificación Buen Fin **")
#Se solicitan datos, uno de tipo flotante y otro de tipo String.
cantidad_gasto = float(input("Ingresa el valor de tu compra: "))
MSI = input("¿La compra fue a meses sin intereses (Sí/No)? ")

#Verificar si la cantidad gastada es mayor o igual a 500 y asignar un booleano a la variable (True/False).
gasto = cantidad_gasto >= 500
#Se convierte la cadena a minúscula y compara, asigna un booleano a la variable (True/False).
MSI = MSI.lower() == "si"
# "and" verifica si ambos valores son verdaderos para ver si aplica la bonificación.
print(f"¿Aplica para bonificación? {gasto and MSI}")
