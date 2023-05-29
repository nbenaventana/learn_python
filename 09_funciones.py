#Funciones

def multiplicar_por_dos(numero: float):
    return numero * 2

print("El resuktado de la funcion es: ",multiplicar_por_dos(15))

#Número triangular
def es_numero_triangular(numero):
    suma = 0
    i = 1
    while suma < numero:
        suma += i
        if suma == numero:
            return True
        i += 1
    return False

# Solicitar al usuario ingresar un número
numero = int(input("Ingrese un número: "))

if es_numero_triangular(numero):
    print(numero, "es un número triangular.")
else:
    print(numero, "no es un número triangular.")
