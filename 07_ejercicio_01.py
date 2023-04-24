#Ingresar un numero
#Mostrar si el numero ingresado es par o impar
#Deberemos utilizar la estructura de control SI

#Debemos usar una variable booleana antes de imprimir 
#si es par o impar

num = int(input("Ingrese el número: --> "))

par = num % 2 == 0

if par :
    # operaciones por verdadero
    print("El número ", num, " es par")
else :
    # operaciones por falso
    print("El número ", num, " es impar")


#--------------------------------------------------------

numero = int(input("Ingrese el número: "))

if numero % 2 == 0 : 
    par = True
else:
    par = False


if par :
    print("El número ", numero, " es par.")
else :
    print("El número ", numero, " es impar.")

