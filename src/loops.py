# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    # TU CÓDIGO AQUÍ
    resultado = []
    for i in range(1, n + 1):
        resultado.append(i)
    return resultado

def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    Ejemplo: tabla_multiplicar(3) -> [3, 6, 9, ..., 30]
    """
    # TU CÓDIGO AQUÍ
    resultado = []
    for i in range(1, 11):
        resultado.append(n * i)
    return resultado


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    Ejemplo: suma_digitos(123) -> 6
    """
    # TU CÓDIGO AQUÍ
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    """
    # TU CÓDIGO AQUÍ
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    # TU CÓDIGO AQUÍ
    resultado = []
    a, b = 0, 1

    for _ in range(n):
        resultado.append(a)
        a, b = b, a + b

    return resultado
