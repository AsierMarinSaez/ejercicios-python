# This Python file uses the following encoding: utf-8
__Author__="Jose Gaspar Sanchez Garcia"
import os, sys
import random
# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

import ejercicio6 as t

def test_esPrimo():
    assert t.esPrimo(1) == True
    assert t.esPrimo(2) == True
    assert t.esPrimo(3) == True
    assert t.esPrimo(4) == False
    assert t.esPrimo(5) == True
    assert t.esPrimo(6) == False
    assert t.esPrimo(7) == True
    assert t.esPrimo(8) == False
    assert t.esPrimo(9) == False
    assert t.esPrimo(10) == False
    assert t.esPrimo(11) == True
    assert t.esPrimo(12) == False
    assert t.esPrimo(13) == True
    