ventas_por_producto = {}
ventas_por_producto1 = {}

producto = "Producto 1"
cantidad = 10
precio = 100

ventas_por_producto[producto] = [cantidad, precio]

if producto in ventas_por_producto:
    ventas_por_producto[producto].append([cantidad, precio])
else:
    ventas_por_producto[producto] = [cantidad, precio]

print(ventas_por_producto)
print(ventas_por_producto1)
