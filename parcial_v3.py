# Módulo: generador_contrasenas.py
import random

def generar_contrasena(longitud):
    """Genera una contraseña aleatoria de la longitud especificada.

    Args:
        longitud: Un entero representando la longitud deseada de la contraseña.

    Returns:
        Un string con la contraseña generada.
    """
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};':\"\\|,.<>/?"
    contrasena = ""
    for _ in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena

# --- Código del estudiante ---

import generador_contrasenas

# Solicitar al usuario la longitud deseada de la contraseña
# ...

# Generar y mostrar la contraseña
# ...