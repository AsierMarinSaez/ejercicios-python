# This Python file uses the following encoding: utf-8
__Author__="Jose Gaspar Sanchez Garcia"
import os, sys
import random
# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

import ejercicio5 as t

def test_esPar():
    assert t.esPar(1) == False
    assert t.esPar(4) == True

def test_esImpar():
    assert t.esImpar(10) == False
    assert t.esImpar(15) == True

def test_generarImpares():
    # Este puede no ser un buen caso de prueba por la forma en que esta construído.
    inicio=random.randint(-10000,10000)
    n=random.randint(0,100000);
    impares=t.generarImpares(n,inicio);
    assert len(impares) == n
    if inicio % 2 ==0 :
        assert impares[0] == inicio+1
    # Comprobamos la generación de impares
    esperado=[1, 3, 5, 7, 9]
    assert t.generarImpares(5,1) == esperado
    esperado=[3, 5, 7, 9, 11]
    assert t.generarImpares(5,2) == esperado

def test_generarPares():
    # Este puede no ser un buen caso de prueba por la forma en que esta construído.
    inicio=random.randint(-10000,10000)
    n=random.randint(0,100000);
    pares=t.generarPares(n,inicio);
    assert len(pares) == n
    if inicio % 2 ==1 :
        assert pares[0] == inicio+1
    # Comprobamos la generación de pares
    esperado=[2, 4, 6, 8, 10]
    assert t.generarPares(5,1) == esperado
    esperado=[4, 6, 8, 10, 12]
    assert t.generarPares(5,4) == esperado

