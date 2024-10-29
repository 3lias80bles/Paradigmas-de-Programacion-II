'''
Nombre: Sergio Elías Robles Ignacio
Fecha: 18 de octubre de 2024
Descripción: En este trabajo se muestra el funcionamiento de los operadores lógicos.
'''

print("*** Expresión booleana (exp1 O exp2) Y (exp3 O exp4) ***")

#Se piden 4 valores de V/F que son de tipo String
exp1 = input("Ingresa valor booleano (V/F): ")
exp2 = input("Ingresa valor booleano (V/F): ")
exp3 = input("Ingresa valor booleano (V/F): ")
exp4 = input("Ingresa valor booleano (V/F): ")

#Se convierten las cadenas a minúsculas y se compara si es igual a "v", esto nos devuelve un booleano (True/False).
exp1 = exp1.lower() == "v"
exp2 = exp2.lower() == "v"
exp3 = exp3.lower() == "v"
exp4 = exp4.lower() == "v"

#Se usa el operador "or" para realizar la primera operación.
exp5 = exp1 or exp2
exp6 = exp3 or exp4

#Se usa el operador "and" para combinar las eoperaciones anteriores y obtener el resultado final.
print(f"El resultado de la expresión booleana es: {exp5 and exp6}")
