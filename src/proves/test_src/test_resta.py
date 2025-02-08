import pytest


import resta


def test_suma_cero():
    assert resta.resta_enteros(0,0) == 0


def test_suma_positivos():
    assert resta.resta_enteros(5,5) == 0


def test_suma_positivos_negativos():
    assert resta.resta_enteros(-5,5) == -10


def test_suma_nagativo():
    assert resta.resta_enteros(-5,-5) == 0

