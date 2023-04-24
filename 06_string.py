# Comentario de una linea
letra = 'P'                # un string de un solo caracter
print(letra)               # P
print(len(letra))          # 1
saludos = 'Hello, World!'  # String puede ser formado con comillas simples o dobles, "Hello, World!"
print(saludos)             # Hello, World!
print(len(saludos))        # 13
oracion = "Espero que aprendan y disfruten estas clases de Python"
print(oracion)


# String multilinea
string_varias_lineas = '''Python es un lenguaje de programación 
interpretado, 
de alto nivel y multipropósito. Fue creado en 1991 por Guido van Rossum 
en los Países Bajos y se ha convertido en uno de los lenguajes de 
programación más populares en todo el mundo.'''

print(string_varias_lineas)

# Otra forma de hacer lo mismo
string_varias_lineas_comilla_doble = """Python es un lenguaje de programación interpretado, 
de alto nivel y multipropósito. Fue creado en 1991 por Guido van Rossum 
en los Países Bajos y se ha convertido en uno de los lenguajes de 
programación más populares en todo el mundo."""

print(string_varias_lineas_comilla_doble)

# Concatenacion de String
first_name = 'Nelson'
last_name = 'Benaventana'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) 

# Chequeando la cantidad de caracteres de un string 
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15

cadena = "Una palabra"
print(cadena[0])

