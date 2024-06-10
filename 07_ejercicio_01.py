#Ingresar 2 valores numericos y simbolo (+, - , * o / ) por pantalla y devolver el 
#resultado de la operacion
#Ejemplo:
#Ingresar valor: 
#Ingresar Operacion: 
#Ingresar valor: 
#El resultado es:  12 + 5 = 17


valor1 = float(input("Ingresar valor: "))
operacion = input("Ingresar operación: ")
valor2 = float(input("Ingresar valor: "))
resultado = 0.00
if operacion == "+":
    resultado = valor1 + valor2
elif operacion == "-":
    resultado = valor1 - valor2
elif operacion == "*":
    resultado = valor1 * valor2
elif operacion == "/":
    resultado = valor1 / valor2

print(f"El resultado es: {valor1} {operacion} {valor2} = {resultado}")



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

