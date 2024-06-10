## Metodos del tipo String
# capitalize(): 
    #convierte la primer letra de una oración a mayuscula.
semana = 'esta es la cuarta semana de python.'
semana_mayuscula = semana.upper()
print(semana_mayuscula)
print(semana.capitalize())
print("Variable semana sin el metodo: ",semana)

# count():
    # retorna la cantidad de ocurrencias de una sub-cadena dentro
    # de una cadena

print("Cantidad de letras [a] en variable semana: ", 
      semana.count('a'))
print("Cantidad de veces [ta] en variable semana: ", 
      semana.count('ta'))

#Busca la subcadena indicada desde la posición 9
print("Cantidad de letras [a] : ", semana.count('a',9))

#Busca la subcadena indicada desde la posición 9 hasta la posición 15
print("Cantidad de letras [a] : ", semana.count('a',9,15))

cadena = input("Ingrese una cadena: ")
cadena_invertida = cadena[::-1].lower().replace(" ","")
print("Cadena regular: ", cadena)

print("Cadena invertida: ", cadena_invertida[::-1])

if cadena.lower() == cadena_invertida:
    print(cadena, " es palindromo")


#Metodo split

cadena = "Esta cadena tiene 5 palabras"
palabras = cadena.split()
print("Palabras de la cadena: ", palabras)
# Imprime:  ['Esta', 'cadena', 'tiene', '5', 'palabras']


#Metodos y funcione varias de cadenas
caracter = "A"
caracter.islower() #Retorna verdadero (True) si el caracter es una letra en minuscula
caracter.isupper() #Retorna verdadero (True) si el caracter es una letra en mayusculas
caracter.isnumeric() #Retorna verdadero (True) si el caracter es un número

cadena.count() #Retorna la cantidad de caracteres que tiene la cadena
cadena.isdecimal() #Retorna verdadero (True) si la cedena es un valor numerico con decimales
len(cadena) #Retorna la longitud de una cadena
