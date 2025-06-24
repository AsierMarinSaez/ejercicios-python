# This Python file uses the following encoding: utf-8
import os, sys

import sample

# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

def test_uno():
    assert sample.uno() == 1

def test_zero():
    assert sample.zero() == 0
def test_saludar():
    assert sample.saludar() == "Hola mundo"