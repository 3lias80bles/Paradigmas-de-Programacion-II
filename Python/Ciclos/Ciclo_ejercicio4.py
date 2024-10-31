'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: En este trabajo se usa el ciclo while y la sentencia if para realizar un cajero de banco
'''

#Inicialización de variables.
i=0
opcion=7
saldo =0.0#El saldo inicializa sempre en 0.

#Bucle para el menú principal del cajero.
while opcion!=4:
    print()
    print("*** Bienvenido a tu cuenta de Banco Azteca ***")
    print("Consultar tu saldo................[1]")
    print("Ingresar dinero...................[2]")
    print("Retirar dinero....................[3]")
    print("Salir.............................[4]")
    print()
    #Se solicitar una opción al usuario.
    opcion=int(input("Su opción es: "))

    #Opción para salir del programa.
    if opcion == 4:
        print()
        print("Adios...")
    #Opción para consultar saldo.
    elif opcion==1:
        print()
        print(f"Tu saldo actual es: ${saldo:.2f}")
    #Opción para ingresar dinero a la cuenta.
    elif opcion == 2:
        print()
        cantidad = float(input("Ingrese la cantidad a depositar: $"))
        #Se valida que la cantidad ingresada sea positiva.
        if cantidad <0:
            print()
            print("Favor de ingresar un número positivo")
        #Se suma el la cantidad ingresada al saldo.
        else:
            saldo += cantidad
            print()
            print(f"Has depositado: ${cantidad:.2f}")
            print(f"Tu nuevo saldo es: ${saldo:.2f}")
    #Opción para retirar dinero de la cuenta.
    elif opcion == 3:
        print()
        retiro = float(input("Ingrese la cantidad a retirar: $"))
        #Se valida que la cantidad a retirar sea positiva.
        if retiro <0:
            print()
            print("Favor de ingresar un número positivo")
        #Se valida que haya suficiente saldo para el retiro.
        elif retiro >saldo:
            print()
            print("No cuenta con esa cantidad para retirar")
            print(f"Tu saldo actual es: ${saldo:.2f}")
        #Se resta la cantidad retirada al saldo.
        else:
            print()
            saldo -= retiro
            print(f"Has retirado: ${retiro:.2f}")
            print(f"Tu nuevo saldo es: ${saldo:.2f}")
    #Opciones no válidas.
    else:
        print()
        print("Seleccione una opción valida.")
