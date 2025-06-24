# This Python file uses the following encoding: utf-8
__Author__="Jose Gaspar Sanchez Garcia"
import os, sys
import random
# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

import ejercicio8 as t

def test_fibonacci():
    esperado = [1,1,2,3,5,8,13,21,34,55]
    assert t.fibonacci(10) == esperado
    esperado = []
    assert t.fibonacci(0) == esperado
    esperado = []
    assert t.fibonacci(-1) == esperado
    esperado = [1]
    assert t.fibonacci(1) == esperado
    esperado = [1,1]
    assert t.fibonacci(2) == esperado
    esperado = [1,1,2]
    assert t.fibonacci(3) == esperado
    
    
    
    
    
    