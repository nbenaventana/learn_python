# Módulo: cajero.py
def validar_pin(pin_correcto):
    """Solicita al usuario su PIN y verifica si es correcto.

    Args:
        pin_correcto: Un entero representando el PIN correcto.

    Returns:
        True si el PIN es correcto, False en caso contrario.
    """
    intentos = 3
    while intentos > 0:
        pin_ingresado = int(input("Ingrese su PIN: "))
        if pin_ingresado == pin_correcto:
            return True
        else:
            intentos -= 1
            print("PIN incorrecto. Intentos restantes:", intentos)
    return False

def mostrar_saldo(saldo):
    """Muestra el saldo actual de la cuenta.

    Args:
        saldo: Un entero representando el saldo.
    """
    print("Su saldo actual es:", saldo)

# --- Código del estudiante ---

import cajero

# Establecer un PIN correcto y un saldo inicial
# ...

# Solicitar al usuario su PIN
# ...

# Si el PIN es correcto, mostrar un menú con opciones (consultar saldo, retirar, etc.)
# ...
