__author__ = "Asier Marín Sáez"

"""Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir."""

def main():
    nombre = input("Introduzca su nombre: ")
    try:
        edad = int(input(f"Introduzca su edad {nombre}: "))
        
        # Comprobamos si es mayor de edad - Estructura condicional if - else
        if edad >= 18:
            print(f"{nombre}, usted es mayor de edad y puede conducir.")
        else:
            print(f"{nombre}, todavía eres menor de edad.")
    except ValueError:
        print("Por favor, introduzca un número válido para la edad.")

if __name__ == "__main__":
    main()
