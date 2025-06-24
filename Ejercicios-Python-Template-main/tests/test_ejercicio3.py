# This Python file uses the following encoding: utf-8
__Author__="Jose Gaspar Sanchez Garcia"
import os, sys

# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

import ejercicio3 as t

def test_obtenerCalificacion():
    assert t.obtenerCalificaion(0) == "Muy deficiente"
    assert t.obtenerCalificaion(1) == "Muy deficiente"
    assert t.obtenerCalificaion(2) == "Muy deficiente"
    assert t.obtenerCalificaion(3) == "Insuficiente"
    assert t.obtenerCalificaion(4) == "Insuficiente"
    assert t.obtenerCalificaion(5) == "Suficiente"
    assert t.obtenerCalificaion(6) == "Bien"
    assert t.obtenerCalificaion(7) == "Notable"
    assert t.obtenerCalificaion(8) == "Notable"
    assert t.obtenerCalificaion(9) == "Sobresaliente"
    assert t.obtenerCalificaion(10) == "Sobresaliente"
    assert t.obtenerCalificaion(-1) == "Incorrecta"
    assert t.obtenerCalificaion(11) == "Incorrecta"
