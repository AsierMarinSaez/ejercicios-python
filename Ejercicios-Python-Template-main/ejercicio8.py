# coding=utf-8
__Author__="Asier Marín Sáez"

# Función que determina si un numero es primo.
def fibonacci(n):
    vector = []

    if n < 1:
        return vector
    elif n == 1:
        vector.append(1)
        return vector
    elif n == 2:
        vector.append(1)
        vector.append(1)
        return vector
    elif n >= 3:
        vector.append(1)
        vector.append(1)
        i = 2
        while i < n:
            vector.append(vector[i - 1] + vector[i - 2])
            i += 1

    return vector

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero = int(input("Introduzca un número: "))
    print("{0} elementos --> FIBONACCI: {1}.".format(numero, fibonacci(numero)))

if __name__ == "__main__":
    main()