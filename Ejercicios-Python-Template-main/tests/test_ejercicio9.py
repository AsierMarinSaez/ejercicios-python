# This Python file uses the following encoding: utf-8
__Author__="Jose Gaspar Sanchez Garcia"
import os, sys
import random
# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

import ejercicio9 as t

def test_suma():
        assert t.suma(4,3) == 7
        assert t.suma(-4,3) ==-1
def test_resta():
    assert t.resta(13,3) == 10
    assert t.resta(-13,3) == -16
    assert t.resta(-13,-3) == -10
    assert t.resta(13,-3) == 16
def test_multiplica() :
    assert t.multiplica(3,5) == 15
    assert t.multiplica(-3,5) == -15
    assert t.multiplica(-3,-5) == 15
    assert t.multiplica(3,0) == 0
    assert t.multiplica(3,1) == 3
def test_divide() :
    assert t.divide(5,5) == 1
    assert t.divide(30,5) == 6
    assert t.divide(30,1) == 30

    
    
    
    
    
    