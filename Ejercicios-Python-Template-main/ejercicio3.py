# coding=utf-8
__author__ = "Asier Marín Sáez"

"""
Pide una nota (número). Muestra la calificación según la nota:
0-3: Muy deficiente.
3-5: Insuficiente.
5-6: Suficiente.
6-7: Bien.
7-9: Notable.
9-10: Sobresaliente
Cualquier otra: Incorrecta
"""

# Implemente función obtenerCalificacion
def obtenerCalificaion(nota):
    if nota >= 0 and nota <= 2:
        return "Muy deficiente"
    elif nota == 3 or nota == 4:
        return "Insuficiente"
    elif nota == 5:
        return "Suficiente"
    elif nota == 6:
        return "Bien"
    elif nota == 7 or nota == 8:
        return "Notable"
    elif nota == 9 or nota == 10:
        return "Sobresaliente"
    else:
        return "Incorrecta"

# Programa principal
def main():
    try:
        n = int(input("Introduzca la nota: "))
        print('Calificación: ' + obtenerCalificaion(n))
    except ValueError:
        print("Entrada no válida. Introduzca un número entero.")

if __name__ == "__main__":
    main()
