# Funciones
## Función sin parámetros

def generate_full_name ():
    first_name = 'Primer nombre'
    last_name = 'Apellido'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name () # Llamada a una función

def sumar_dos_numeros ():
    num_1 = 2
    num_2 = 3
    total = num_1 + num_2
    print(total)

sumar_dos_numeros()

##Función que devuelve un valor
def generate_full_name ():
    first_name = 'Retorna Un'
    last_name = 'Valor'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())

def sumar_dos_numeros ():
    num_1 = 10
    num_2 = 5
    total = num_1 + num_2
    return total

print(sumar_dos_numeros())

### Devolver un booleano
def es_par (n):
    if n % 2 == 0:
        print('par')
        return True    # return detiene la ejecución de la función, similar a break 
    return False

print(es_par(10)) # True
print(es_par(7)) # False

### Devolver una lista
def buscar_numeros_pares(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(buscar_numeros_pares(10))

## Funciones con parámetros

def greetings (name):
    message = name + ', bienvenido/a a Python!'
    return message

print(greetings('Nombre'))

def add_ten(num):
    ten = 10
    return num + ten

print(add_ten(90))

def square_number(x):
    return x * x

print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area

print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total

print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

## Funciones con 2 o mas parámetros 

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print('Nombre completo: ', generate_full_name('Primer Nombre','Apellido'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Suma de 2 números: ', sum_two_numbers(1, 9))

def calcular_edad (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Edad: ', calcular_edad(2023, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # el valor se cambio a string antes de concatenarle N 
    return weight
print('Peso de un objeto en Newtons: ', weight_of_object(100, 9.81))

## Función con valores predeterminados en parámetros
def generate_full_name (first_name = 'Nombre', last_name = 'Apellido'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('Nelson','Benaventana'))

##Funciones con cantidad de parametros indefinidos
def sum_all_nums(*numeros):
    total = 0
    for num in numeros:
        total += num     # esto es lo mismo que total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
print(sum_all_nums(5,8,2,4,14)) # 33

##Función como parámetro de otra función
def square_number (n):
    return n * n

def cube_number (n):
    return n * n * n

def ejecutar_funcion(f, x):
    return f(x)

print(ejecutar_funcion(square_number, 3)) # 9
print(ejecutar_funcion(cube_number, 4)) # 64