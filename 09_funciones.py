#Funciones
#Una función es un bloque reutilizable de código o declaraciones de programación diseñadas para realizar una determinada tarea. 
#Para definir o declarar una función, Python proporciona la palabra clave def . La siguiente es la sintaxis para definir una función. 
#El bloque de función de código se ejecuta solo si se llama o invoca la función.

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
