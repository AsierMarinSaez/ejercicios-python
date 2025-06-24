# coding=utf-8
__author__ = "Asier Marín Sáez"

import random

# Función que determina si un número es par
def esPar(numero):
    return numero % 2 == 0

# Función que determina si un número es impar
def esImpar(numero):
    return numero % 2 != 0

# Genera una lista de números pares
def generarPares(valores, inicio):
    pares = []
    numero = inicio
    if esImpar(numero):
        numero += 1  # Ajustar al siguiente par si es impar
    while len(pares) < valores:
        pares.append(numero)
        numero += 2
    return pares

# Genera una lista de números impares
def generarImpares(valores, inicio):
    impares = []
    numero = inicio
    if esPar(numero):
        numero += 1  # Ajustar al siguiente impar si es par
    while len(impares) < valores:
        impares.append(numero)
        numero += 2
    return impares

# Programa principal
def main():
    print("Par e impar")
    n = int(input("Introduzca un número: "))
    print("{0} es par --> {1}".format(n, esPar(n)))

    m = int(input("Introduzca el número de valores: "))
    i = int(input("Introduzca el número inicial: "))

    x = generarPares(m, i)
    y = generarImpares(m, i)

    print("Impares: ", y)
    print("Pares: ", x)

if __name__ == "__main__":
    main()
