import pytest


import resta


def test_suma_cero():
  assert resta.resta_enteros(0,0) == 0


def test_suma_positivos():
  assert resta.resta_enteros(5,5) == 0


def test_suma_positivos_negativos():
  assert resta.resta_enteros(-5,5) == -100


def test_suma_nagativo():
  assert resta.resta_enteros(-5,-5) == 0


def test_suma_excepcion_sumando1():
   with pytest.raises(TypeError):
       resta.resta_enteros(5.0,5) == 0


def test_suma_excepcion_sumando2():
   with pytest.raises(TypeError):
       resta.resta_enteros(5.0,'a') == 7


def test_suma_excepcion_sumandos():
   with pytest.raises(TypeError):
       resta.resta_enteros(True,'a') == 5
