cadena = input("Ingrese una cadena de texto: ")

# Obtener la primera letra de la primera palabra 
# y verificar si es una vocal
primera_palabra = cadena.split()[0]

primera_letra = primera_palabra[0].lower()

if primera_letra in ['a', 'e', 'i', 'o', 'u']:
    print("La primera letra de la primera palabra es una vocal")
else:
    print("La primera letra de la primera palabra no es una vocal")


numero = float(input("Ingresar un numero: "))
if (numero >= 10 and numero <= 99 or (numero <= -10 >= -99)):
    print("El numero ", numero, " es de 2 digitos")




    