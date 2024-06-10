# Módulo: analisis_ventas.py
def calcular_comision(ventas):
    """Calcula la comisión de un vendedor según sus ventas totales.

    Args:
        ventas: Una lista de enteros representando las ventas mensuales.

    Returns:
        Un entero representando la comisión total.
    """
    comision_total = 0
    for venta in ventas:
        if venta > 5000:
            comision_total += venta * 0.15
        elif venta > 2000:
            comision_total += venta * 0.10
        else:
            comision_total += venta * 0.05
    return comision_total

def vendedor_del_mes(vendedores, ventas):
    """Determina el vendedor con la mayor comisión total.

    Args:
        vendedores: Una lista de strings con los nombres de los vendedores.
        ventas: Una lista de listas de enteros, donde cada sublista
                representa las ventas mensuales de un vendedor.

    Returns:
        Un string con el nombre del vendedor del mes.
    """
    mejor_vendedor = ""
    mejor_comision = 0

    for i in range(len(vendedores)):
        comision = calcular_comision(ventas[i])
        if comision > mejor_comision:
            mejor_vendedor = vendedores[i]
            mejor_comision = comision
    return mejor_vendedor

# --- Código del estudiante ---

import analisis_ventas

# Pedir al usuario los nombres de los vendedores y sus ventas mensuales
# ...

# Calcular y mostrar la comisión de cada vendedor
# ...

# Determinar y mostrar el vendedor del mes
# ...