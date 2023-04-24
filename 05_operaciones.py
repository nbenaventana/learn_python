# Operaciones aritmeticas en Python
# Enteros
print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print('Division: ', 4 / 2)# Division en Python devuelve decimal
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)# Retorna entero sin resto
print('Modulus: ', 3 % 2) # Retorna el resto de la division
print('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2) # esto es 3 al cuadrado

# Decimales
print('Floating Number, PI constant: ', 3.14)
print('Floating Number, gravity acceleration: ', 9.81)

# Declarando variables al principio primero

a = 3 # a es el nombre de la variable y 3 es un tipo de dato entero.
b = 2 # b es el nombre de la variable y 2 es un tipo de dato entero.

# Operaciones aritmeticas y asignacion de resultado a variables
suma = a + b
diferencia = a - b
producto = a * b
division = a / b
resto = a % b
division_entero = a // b
exponente = a ** b

print(suma) # si no etiquetamos el print con alguna cadena, nunca sabremos de dónde viene el resultado
print('a + b = ', suma)
print('a - b = ', diferencia)
print('a * b = ', producto)
print('a / b = ', division)
print('a % b = ', resto)
print('a // b = ', division_entero)
print('a ** b = ', exponente)


# Calculando el area de un circulo
radio = 10

area_circulo = 3.14 * radio ** 2
print('Area de un circulo: ', area_circulo)

pi = 3.14
area_circulo = pi * radio ** 2

# Calculando el area de un rectangulo
longitud = 10
ancho = 20
area_rectangulo = longitud * ancho
print('Area del rectangulo: ', area_rectangulo)

# Calculo del peso de un objeto
masa = 75
acel_gravedad = 9.81
peso = masa * acel_gravedad
print("Peso :", peso, ' N')

#Logica valores booleanos
print("3 > 2: ", 3 > 2)     
print(3 >= 2)    
print(3 < 2)     
print(2 < 3)
print(2 <= 3)    
print(3 == 2)    
print(3 != 2)    
print(len('mango') == len('manzana'))  # False
print(len('mango') != len('manzana'))  # True
print(len('mango') < len('manzana'))   # True
print(len('pera') != len('kiwi'))      # False
print(len('pera') == len('kiwi'))      # True
print(len('tomate') == len('batata'))  # True
print(len('python') > len('dragon'))   # False

# Comparaciones booleanas
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Otra forma de comparacion 
print('1 is 1', 1 is 1)                   # True 
print('1 is not 2', 1 is not 2)           # True 
print('A in Alaska', 'A' in 'Alaska') # True 
print('B in Absorcion', 'B' in 'Absorcion') # False
print('codeando' in 'codeando para todos') # True 
print('a in anuario:', 'a' in 'anuario')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - 
print(3 > 2 and 4 < 3) # False - 
print(3 < 2 and 4 < 3) # False - 
print(3 > 2 or 4 > 3)  # True - 
print(3 > 2 or 4 < 3)  # True - 
print(3 < 2 or 4 < 3)  # False - 
print(not 3 > 2)     # False - 
print(not True)      # False - 
print(not False)     # True
print(not not True)  # True
print(not not False) # False