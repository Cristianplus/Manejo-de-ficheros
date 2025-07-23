"""
Ejercicio: Manejo de ficheros
"""

import os

# Definir el nombre del fichero
file_name = "cristianplus.txt"

# Escribir en el fichero
with open(file_name, "w") as file: 
    file.write("Cristian Cordero\n") #Nombre
    file.write("25\n") #Edad
    file.write("JavaScript") #Lenguaje de programación

# Leer el fichero y mostrar su contenido
with open(file_name, "r") as file:
    print(file.read())

# Eliminar el fichero
os.remove(file_name)
