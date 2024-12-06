'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 13 de Noviembre
Descripción: Ejercicio de una calculadora usando funciones.
'''

def menu ():
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
#funciones de operaciones.
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def mult(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def div_entera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: No se puede dividir por cero."

def calcular_exp(a, b):
    return a ** b

# Inicialización de variables.
opcion = 7

#Bucle para el menú principal de la calculadora.
while opcion != 0:
    #Se manda a llamar al menú, no manda nada
    menu()

    #Se solicita una opción al usuario.
    opcion = int(input("Su opción es: "))

    #Opción para salir del programa.
    if opcion == 0:
        print("Adiós...")
    #Se piden dos datos al usuario para realizar cualquiera de las operaciones
    else:
        num_one = float(input("Ingrese un número: "))
        num_two = float(input("Ingrese otro número: "))
        #Se revisa la opcion y se manda a llamar a la función correspondiente
        if opcion == 1:
            #La función suma envia los dos números ingresados y lo que regresa lo guarda en resultado.
            resultado = suma(num_one, num_two)
        elif opcion == 2:
            # La función resta envia los dos números ingresados y lo que regresa lo guarda en resultado.
            resultado = resta(num_one, num_two)
        elif opcion == 3:
            # La función mult envia los dos números ingresados y lo que regresa lo guarda en resultado.
            resultado = mult(num_one, num_two)
        elif opcion == 4:
            # La función división envia los dos números ingresados y lo que regresa lo guarda en resultado.
            resultado = division(num_one, num_two)
        elif opcion == 5:
            # La función div_entera envia los dos números ingresados y lo que regresa lo guarda en resultado.
            resultado = div_entera(num_one, num_two)
        elif opcion == 6:
            # La función calcular_exp envia los dos números ingresados y lo que regresa lo guarda en resultado.
            resultado = calcular_exp(num_one, num_two)
        else:
            resultado = "Seleccione una opción valida."

        #imprime el resultado
        print(f"Resultado: {resultado:.3f}")
        print()