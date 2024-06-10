# Leer un archivo
with open("archivo.txt", "r") as file:
    contenido = file.read()
    print(contenido)

# Leer un archivo línea por línea
with open("archivo.txt", "r") as file:
    linea = file.readline() #lee solo la linea
    #Va recorriendo y leyendo todas las lineas de a una
    for linea in file:
        print(linea, end="")

# Escribir un archivo
with open("archivo.txt", "w") as file:
    file.write("Esta es una línea de texto\n")
    file.write("Otra línea de texto")

