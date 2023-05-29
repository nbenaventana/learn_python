##Ejemplos de listas

frutas = ["manzana", "banana", "kiwi", "naranja"]
print(frutas[0])  # Imprime "manzana"
print(frutas[2])  # Imprime "kiwi"


numeros = [1, 2, 3, 4, 5]
numeros[2] = 10
print(numeros)  # Imprime [1, 2, 10, 4, 5]


##Diferencias con las tuplas
mi_lista = [1, 2, 3]
mi_tupla = (4, 5, 6)

mi_lista[0] = 10  # Las listas son mutables
print(mi_lista)  # Imprime [10, 2, 3]

mi_tupla[0] = 10  # Las tuplas son inmutables, esto generará un error

## Mas ejemplos y forma de acceder a los elementos

mi_tupla = (1, 2, 3)
print(mi_tupla[0])  # Imprime 1
print(mi_tupla[1])  # Imprime 2

## Desempaquetar tuplas

mi_tupla = (1, 2, 3)
a, b, c = mi_tupla
print(a)  # Imprime 1
print(b)  # Imprime 2
print(c)  # Imprime 3

## Concatenacion
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
concatenacion = tupla1 + tupla2
print(concatenacion)  # Imprime (1, 2, 3, 4, 5, 6)

repetida = tupla1 * 3
print(repetida)  # Imprime (1, 2, 3, 1, 2, 3, 1, 2, 3)


## Funciones y metodos para trabajar con tuplas

mi_tupla = (1, 2, 2, 3, 2)
print(len(mi_tupla))  # Imprime 5
print(mi_tupla.count(2))  # Imprime 3
print(mi_tupla.index(3))  # Imprime 3

