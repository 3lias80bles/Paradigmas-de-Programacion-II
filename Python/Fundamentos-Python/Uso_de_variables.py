'''
Sergio Elias Robles Ignacio
10 de octubre de 2024.
Descripción:
En este archivo se ejemplifica el uso de variables en Python.
'''

# Notas:
# En Python to do es un objeto.
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal

# Toda variable requiere un valor inicial
semestre = 4        # es una variable que apunta a un objeto de tipo int con valor de 4
print(semestre)     # imprime el valor de la variable
semestre = 5        # la variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia
print(semestre)

# Se crean varias variables para ejemplificar su uso
nombre = "Sergio"  # variable de tipo String
altura = 1.62       # variable de tipo Float
edad = 20          # variable de tipo Int

# Se imprimen las variables, añadiendo información adicional para comprender lo que se imprime
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "m.")
print("Edad: ", edad, "años.")

# Se modifican los valores de las variables y se mandan a imprimir
altura = 1.63
edad = 19
print()
print("Valores modificados:")
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "m.")
print("Edad: ", edad, "años.")

# En Python, las variables son dinámicas, por lo que pueden almacenar otro tipo de dato en cualquier momento
edad = "diecinueve"      # edad antes tenía el valor de 20 (Int)
print()
print("Edad (con otro tipo de dato):", edad)

# Reglas para los nombres de las variables en Python:
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guion bajo
# - La variable no puede iniciar con números
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.

# Buenas prácticas
# - Utilizar minúsculas para las palabras
# - Separar las palabras con el guion bajo
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e.

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "25 de abril de 2004"
clase = "Paradigmas de programación II"
horas_estudio = 8
nombre = "Sergio"
es_estudiante = True

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas
f = "25 de abril de 2004"
fechanacimiento = "25 de abril de 2004"
# class = "Paradigmas de programación II"
# 8horas_estudio = 8
Nombre = "S e r g i o"
NOMBRE = "SERGIO"


# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE', son distintas
print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)
