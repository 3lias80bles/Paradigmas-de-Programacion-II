'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: En este trabajo se usa el ciclo while y la sentencia if para realizar una calculadora
'''

#Inicialización de variables.
i=0
opcion=7

#Bucle para el menú principal del cajero.
while opcion!=0:
    print()
    print("*** Calculadora ***")
    print("Suma..............[1]")
    print("Resta.............[2]")
    print("Multiplicación....[3]")
    print("División..........[4]")
    print("División entera...[5]")
    print("Exponenciación....[6]")
    print("Salir.............[0]")
    print()
    #Se solicitar una opción al usuario.
    opcion=int(input("Su opción es: "))

    # Opción para salir del programa.
    if opcion == 0:
        print("Adios...")
    #Se piden dos datos al usuario para realizar cualquiera de las operaciones
    else:
        num_one = float(input("Ingrese un número: "))
        num_two = float(input("Ingrese otro número: "))
        #Opción para suma.
        if opcion == 1:
            resultado = num_one + num_two
            print(f"El resultado de la suma de {num_one} + {num_two} es: {resultado:.3f}")
        #Opción para resta
        elif opcion == 2:
            resultado = num_one - num_two
            print(f"El resultado de la resta de {num_one} - {num_two} es: {resultado:.3f}")
            print()
        #Opción para multiplicación.
        elif opcion == 3:
            resultado = num_one * num_two
            print(f"El resultado de la multiplicación de {num_one} * {num_two} es: {resultado:.3f}")
            print()
        #Opción para división.
        elif opcion == 4:
            if num_two != 0:  #Comprobación para evitar división por cero.
                resultado = num_one / num_two
                print(f"El resultado de la división de {num_one} / {num_two} es: {resultado:.3f}")
            else:
                print("Error: No se puede dividir por cero.")
            print()
        #Opción para división entera.
        elif opcion == 5:
            if num_two != 0:#Comprobación para evitar división por cero.
                resultado = num_one // num_two
                print(f"El resultado de la división entera de {num_one} // {num_two} es: {resultado}")
            else:
                print("Error: No se puede dividir por cero.")
            print()
        #Opción para exponenciación.
        elif opcion == 6:
            resultado = num_one ** num_two
            print(f"El resultado de {num_one} elevado a {num_two} es: {resultado:.3f}")
            print()
        # Opciones no válidas.
        else:
            print()
            print("Seleccione una opción valida.")

