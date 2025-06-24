# This Python file uses the following encoding: utf-8
__Author__="Jose Gaspar Sanchez Garcia"
import os, sys

# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

import ejercicio4b as t

def test_obtenerCalificacion():
    assert t.quienGana("piedra","piedra") == 0
    assert t.quienGana("papel","papel") == 0
    assert t.quienGana("tijera","tijera") == 0

    assert t.quienGana("piedra","papel") == 2
    assert t.quienGana("piedra","tijera") == 1
    
    assert t.quienGana("papel","piedra") == 1
    assert t.quienGana("papel","tijera") == 2

    assert t.quienGana("tijera","papel") == 1
    assert t.quienGana("tijera","piedra") == 2

