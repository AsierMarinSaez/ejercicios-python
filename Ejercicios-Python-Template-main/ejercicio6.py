# coding=utf-8
__Author__="Asier Marín Sáez"


# Función que determina si un numero es primo.

def esPrimo(numero):
    if numero < 1:
        return False
    if numero == 1:
        return True

    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1

    if contador == 2:
        return True
    else:
        return False


# Programa principal
def main():
    print("ES PRIMO")
    n=int(input("Introduzca un numero: "))
    print("{0} es primo --> {1}.".format(n,esPrimo(n)))

if __name__== "__main__" :
   main()
