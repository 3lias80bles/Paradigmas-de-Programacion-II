'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: En este trabajo se usa el ciclo while y la sentencia if para realizar una calculadora
'''
#Inicialización de variables.
i = 0
opcion = 5

#Bucle para el menú principal del cajero.
while opcion!=0:
    print()
    print("*** Programa que calcula el área y perímetro ***")
    print("Calcular el área de un rectángulo............[1]")
    print("Calcular el perímetro de un rectángulo.......[2]")
    print("Calcular el área de un círculo...............[3]")
    print("Calcular el perímetro de un círculo..........[4]")
    print("Salir........................................[0]")
    print()
    #Se solicitar una opción al usuario.
    opcion=int(input("Su opción es: "))

# Opción para salir del programa.
    if opcion == 0:
        print("Saliendo...")

    #Opción para el área de un rectangulo.
    elif opcion == 1:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        #Se valida que sea un número positivo.
        if base < 0 or altura < 0:
            print()
            print("Favor de ingresar un número positivo")
        else:
            print()
            print(f"El área es: {base*altura:.3f}")
            print("-------------------------")

    #Opción para el perímetro de un rectangulo
    elif opcion == 2:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        #Se valida que sea un número positivo.
        if base < 0 or altura < 0:
            print()
            print("Favor de ingresar un número positivo")
        else:
            print()
            print(f"El perímetro es: {(2*base)+ (2*altura):.3f}")
            print("-------------------------")

    #Opción para el área de un circulo.
    elif opcion == 3:
        radio = float(input("Ingrese el radio: "))
        #Se valida que sea un número positivo.
        if radio < 0:
            print()
            print("Favor de ingresar un número positivo")
        else:
            print()
            print(f"El área es: {3.1416*(radio*radio):.3f}")
            print("-------------------------")

    #Opción para perímetro de un circulo.
    elif opcion == 4:
        radio = float(input("Ingrese el radio: "))
        #Se valida que sea un número positivo.
        if radio < 0:
            print()
            print("Favor de ingresar un número positivo")
        else:
            print()
            print(f"El perímetro es: {2 * 3.1416 * radio:.3f}")
            print("-------------------------")

    # Opciones no válidas.
    else:
        print()
        print("Seleccione una opción valida.")
