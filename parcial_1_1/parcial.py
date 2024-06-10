import analisis_ventas


# Pedir al usuario los nombres de los vendedores y sus ventas mensuales
# ...
vendedor1 = input("Nombre vendedor 1: ")

#una forma de hacerlo
lista_ventas_v1 = []
i = 1
while (i < 3):
    venta = int(input("Venta del mes vendedor: "))
    lista_ventas_v1.append(venta) 
    i = i + 1

##otra forma de hacer lo mismo de arriba
for i in range(1,4):
    venta = int(input("Venta del mes vendedor: "))
    lista_ventas_v1.append(venta)


vendedor2 = input("Nombre vendedor 1: ")
ventas_vendedor1 = input("Cargar ventas: ")
ventas_lista_2 = ventas_vendedor1.split()
print(ventas_lista_2)

venta_lista_int_2 = []
for venta in ventas_lista_2:
    venta_lista_int_2.append(int(venta))


vendedor3 = input("Nombre vendedor 1: ")
ventas_vendedor3 = [700,800,600]

# Calcular y mostrar la comisión de cada vendedor
# ...
comision_v1 = analisis_ventas.calcular_comision(lista_ventas_v1)
comision_v2 = analisis_ventas.calcular_comision(venta_lista_int_2)
comision_v3 = analisis_ventas.calcular_comision(ventas_vendedor3)

print("Comision vendedor " + vendedor1 + ":",comision_v1)
print("Comision vendedor " + vendedor2   + ":",comision_v2)
print("Comision vendedor " + vendedor3 + ":",comision_v3)

# Determinar y mostrar el vendedor del mes
# ...

lista_vendedores = [vendedor1,vendedor2,vendedor3]
lista_ventas = [lista_ventas_v1,venta_lista_int_2,ventas_vendedor3]
vendedor_mes = analisis_ventas.vendedor_del_mes(lista_vendedores, lista_ventas)

print("Vendedor del mes: ",vendedor_mes)

