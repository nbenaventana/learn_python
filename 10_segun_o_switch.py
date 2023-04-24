#Estructura de control SEGUN implementada en python
def opcion_1():
    print("Has seleccionado la opción 1")

def opcion_2():
    print("Has seleccionado la opción 2")

def opcion_3():
    print("Has seleccionado la opción 3")

# Solicitar al usuario que ingrese una opción
opcion = int(input("Ingrese una opción (1, 2 o 3): "))

# Crear un diccionario con las opciones
switch = {
    1: opcion_1,
    2: opcion_2,
    3: opcion_3,
}
# Ejecutar la función correspondiente a la opción seleccionada
if opcion in switch:
    switch[opcion]()
else:
    print("Opción inválida")
