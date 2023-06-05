#Funciones del sistema

print("La cantidad de caracteres de my_string_variable es:", len("my_string_variable"))


#Inputs

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)

print(age)

#Funcion range()

#La función range() se utiliza como lista de números. El rango (inicio, fin, paso) toma tres parámetros: inicio, fin e incremento. 
# De forma predeterminada, comienza desde 0 y el incremento es 1. La secuencia de rango necesita al menos 1 argumento (fin). 
# Creando secuencias usando rango

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 los argumentos indican el inicio y el final de la secuencia, el paso se establece en el valor predeterminado 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}