# coding=utf-8
__author__ = "Asier Marín Sáez"

# Genera la serie de Fibonacci
def fibonacci(n):
    vector = []

    if n < 1:
        return vector
    elif n == 1:
        vector.append(1)
    elif n == 2:
        vector.append(1)
        vector.append(1)
    else:
        vector.append(1)
        vector.append(1)
        for i in range(2, n):
            vector.append(vector[i - 1] + vector[i - 2])

    return vector

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero = int(input("Introduzca un número: "))
    print("{0} elementos --> FIBONACCI: {1}.".format(numero, fibonacci(numero)))

if __name__ == "__main__":
    main()
