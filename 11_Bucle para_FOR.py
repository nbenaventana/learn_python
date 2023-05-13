# Iterar sobre una lista de números
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# Iterar sobre una cadena de texto
texto = "Hola, mundo!"
for caracter in texto:
    print(caracter)

# Iterar sobre un rango de números
for i in range(1, 11):
    print(i)

# Iterar sobre una lista de diccionarios
personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 30},
    {"nombre": "Pedro", "edad": 20}
]
for persona in personas:
    print(persona["nombre"], persona["edad"])
