#Estructura de control SEGUN implementada en python
def opcion_1(n):
    print("Has seleccionado la opción 1")

def opcion_2(n):
    print("Has seleccionado la opción 2")

def opcion_3(n):
    print("Has seleccionado la opción 3")

def multiplicar_por_tres(numero):
    resu =  numero * 3
    print("El resultado es ", resu)

# Solicitar al usuario que ingrese una opción
opcion = int(input("Ingrese una opción (1, 2 o 3): "))

numero = 5

# Crear un diccionario con las opciones
switch = {
    1: opcion_1,
    2: opcion_2,
    3: opcion_3,
    4: multiplicar_por_tres
}
# Ejecutar la función correspondiente a la opción seleccionada
if opcion in switch:
    switch[opcion](numero)
else:
    print("Opción inválida")
