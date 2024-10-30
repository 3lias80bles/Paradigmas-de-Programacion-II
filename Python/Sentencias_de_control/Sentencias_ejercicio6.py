'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: Este programa determina el precio de un tour que cuenta con dias de descuento.
'''

print("*** Tour turístico Ecoturixtlan ***")
#Se piden los datos de los turistas.
nombre = input("Ingresa el nombre del cliente: ")
num_adul = int(input("Ingresa el número de adultos: "))
num_nis = int(input("Ingresa el número de niños: "))
dia = input("Ingresa el dia de la semana: ")

#Se declaran las variables de los precios de niños y adultos.
child = 100
adulto = 200

dia = dia.lower()#Se convierte a minuscula el dia.

#Se realizan las operaciones para sacar el descuento.
precio = (child * num_nis) + (adulto * num_adul)
descuento = precio - (precio * 0.10)

#Se pregunta si el dia que se ingreso es uno de los dias con descuento.
if dia == "lunes" or dia == "martes" or dia == "jueves":
    print(f"Gracias por tu visita {nombre} este día {dia}. El costo total es de $ {descuento}")#Se imprime en caso de ser dia de descuento.
else:#en caso de no ser dia de descuento se deja el precio original.
    print(f"Gracias por tu visita {nombre} este día {dia}. El costo total es de $ {precio}")