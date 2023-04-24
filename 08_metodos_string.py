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

print("Cantidad de letras [a] en variable semana: ", semana.count('a'))
print("Cantidad de veces [ta] en variable semana: ", semana.count('ta'))
semana

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
