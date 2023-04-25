
opcion_antiguedad = int(input("Antigüedad: 1- 1 año o menos, 2 - 2 años o mas: "))
sueldo = float(input("Ingrese sueldo: $ "))

def menor_doce_meses(sueldo_basico):
    sueldo_mas_plus = sueldo_basico * 1.05
    print("El sueldo final es $ ", sueldo_mas_plus)

def mayor_doce_menor_24(sueldo_basico):
    sueldo_mas_plus = sueldo_basico * 1.07
    print("El sueldo final es $ ", sueldo_mas_plus)


switch = {
    1: menor_doce_meses,
    2: mayor_doce_menor_24
}

if opcion_antiguedad in switch :
    switch[opcion_antiguedad](sueldo)
else:
    print("La opcion de antigüedad no es valida.")



