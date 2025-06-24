![Logotipos ME-GVA CEICE-FP CV-FSE](/imagenes/Logotipos.png)
# Puesta en Producción Segura: Fundamentos de programación.
## Ejercicios de Programación con Python
### Profesor José Gaspar Sánchez García.
Alumno:

#### Elementos básicos:
* [Ejercicio 1](ejercicio1.py). Mostrar en pantalla *Hola mundo*.
* [Ejercicio 2](ejercicio2.py). Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.
* [Ejercicio 2b](ejercicio2b.py). Implemente el *Ejercicio 2* utilizando una función *esMayorEdad(edad) : booleano*.
#### Esctructura de control altenativa:
* [Ejercicio 3](ejercicio3.py). Pide una nota (número). Muestra la calificación según la nota:
    - 0-3: Muy deficiente.
    - 3-5: Insuficiente.
    - 5-6: Suficiente.
    - 6-7: Bien.
    - 7-9: Notable.
    - 9-10: Sobresaliente
    
    Utilice la estructura de control *if-elif-else*.

    Impltemente una función *obtenerCalificacion(nota)*.
* [Ejercicio 4](ejercicio4.py). Escriba un programa que simule el juego **Piedra, papel, tijera** para dos jugadores. Las reglas del juego son las siguientes: 
![Imagen: Juego Piedra, paepel y tijera](https://www.mclibre.org/consultar/python/img/ejercicios/minijuegos/piedra-papel-tijera.svg) 
[mclibre.org](https://www.mclibre.org/consultar/python/img/ejercicios/minijuegos/piedra-papel-tijera.svg)

    Simultáneamente, los dos jugadores muestran una mano en tres posibles posiciones:
    - **Piedra:** se muestra el puño cerrado.
    - **Papel:** se muestra la palma de la mano.
    - **Tijera:** se muestra la palma de la mano con los dedos separados en dos grupos.
    - El jugador que ha sacado **Piedra** gana al jugador que ha sacado *Tijera*.
    - El jugador que ha sacado **Tijera** gana al jugador que ha sacado *Papel*.
    - El jugador que ha sacado **Papel** gana al jugador que ha sacado *Piedra*.

* [Ejercicio 4b](ejercicio4b.py). Reescriba el *Ejercicio4* empleadno formatos en las salidas por pantalla ,**print("{0} {1} {2}... ".format(cero,uno,dos))**.
* [Ejercicio 5](ejercicio5.py). **Par e impar**. Implemente las siguientes funciones:
    - *esPar(numero): booleano*. Comprueba si *numero* es par.
    - *esImpar(numero): booleano*. Comprueba si *numero* es impar.
    - *generarPeres(n, valor_inicial) : [ enteros ]*. Genera un vector de *n* números enteros pares. Si el *valor_inicial* es *impar* entoces el primer elemento del array será su sucesor,
    - *generarInpares(n, valor_inicial) : [ enteros ]*. Genera un vector de *n* números enteros imppares. Si el *valor_inicial* es *par* entoces el primer elemento del array será su sucesor,
* [Ejercicio 6](ejercicio6.py). *esPrimo(numero)*. Escriba una función que devuelva un *booleano* para determinar si un *número* es primo o no. Utilice un bucle **for**. 
* [Ejercicio 7](ejercicio7.py). Realizar la serie de *Fibonacci*. Utiliza bucle **for**.
* [Ejercicio 8](ejercicio8.py). Realizar la serie de *Fibonacci*. Utiliza bucle **while**..
* [Ejercicio 9](ejercicio9.py). Implementar una calculadora con un menú similar al siguiente:

        Menu:
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            0. Salir
        Introduzca opción:
#### Manejo de Cadenas de caracteres:
* [Ejemplo 01](ejemplo01.py). En este ejemplo vamos a estudiar los metodos más importantes que existen para el manejo de ***cadenas*** en *Python*.
    - Convertimos el *"Nombre"* a MAYÚSCULAS.
    - Convertimos todo el *"Nombre"* a minúsculas.
    - Obtener la longitud del *"Nombre"*.
    - Concatena el *Nombre* y los *Apellidos* con *concat()*. Obtén la longitud de la nueva cadena.
    - Del *Nombre completo* extrae la subcadena comprendida entre las posiciones *5* y *10*.
    - Del *Nombre completo* extrae los 3 primeros carácteres.
    - En el *Nombre completo* remplaza ***Pedro*** por *Antonio*. 
#### Web Scraping con Python
* [Ejemplo 02](ejemplo02.py) **Web Scraping** con *Beatiful Soap*.

## Referencias:
### Lenguaje Python
- [W3Schools Python](https://www.w3schools.com/python/).
- [MyPy - static type checker for Python](http://mypy-lang.org/).
- [McLibre - Introducción a Python](https://www.mclibre.org/consultar/python/index.html).
- [Python Básico](https://entrenamiento-python-basico.readthedocs.io/es/3.7/index.html).
- [Pythones.net](https://pythones.net/funcion-print-y-hola-mundo/).
- [Canal Youtube: The PyCoach](https://www.youtube.com/@thepycoach)

### Testing con Pytest
- [Pytest framework](https://docs.pytest.org/).
- [Tutorial de Pytest](https://misovirtual.virtual.uniandes.edu.co/codelabs/tutorial-PyTest/index.html).
- [Probando nuestro código con Pytest](https://old.tacosdedatos.com/pruebas-unitarias-pytest).

