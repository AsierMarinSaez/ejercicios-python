# coding=utf-8
__author__ = "Asier Marín Sáez"

# Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)
def esMayorEdad(edad):
    return edad >= 18

# Programa principal
def main():
    nombre = "Mariano"
    edad = 0

    try:
        edad = int(input(f"Introduzca su edad, {nombre}: "))
        if esMayorEdad(edad):
            print(f"{nombre}, usted es mayor de edad y puede conducir.")
        else:
            print(f"{nombre}, todavía eres menor de edad.")
    except ValueError:
        print("Por favor, introduzca un número válido para la edad.")

if __name__ == "__main__":
    main()
