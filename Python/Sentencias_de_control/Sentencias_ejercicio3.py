'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: En este trabajo se usa la sentencia if elif else para controlar el descuento de productos
'''

print("*** Descuentos por ser miebros de *la cona* *** ")
cantidad=float(input("Ingresa la cantidad comprada: "))
membr=input("¿Cuenta con membresía? ")

membr = membr.lower() == "si"#Se convierte el dato a minuscula, compara y regresa un booleano (True/False)

#Si el usuario es miembro y la cantidad es menor a 1000
if membr and cantidad<1000:
    #Se aplica el descuentro del 5%...
    desc = cantidad-(cantidad * 0.05)
    print("Tu descuento es del 5%")
    print(f"Tu total es de ${desc:.2f}")#Se imprime el descuento con dos decimales
#Si el usuario es miembro y la cantidad es mayor a 1000
elif membr and cantidad>=1000:
    #Se aplica el descuentro del 5%...
    desc = cantidad-(cantidad * 0.08)
    print("Tu descuento es del 8%")
    print(f"Tu total es de ${desc:.2f}")#Se imprime el descuento con dos decimales
#Si el usuario es miembro de la tienda
else:
    print()
    desc = cantidad# la cantidad no se modifica al no tener membresia
    print("Se te invita a ser miembro de la tienda para obtener un descuento de hasta el 8%.")
    print(f"Tu total es de ${desc:.2f}")#Se imprime el costo total
