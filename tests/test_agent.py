import pytest

from agente_ucv.agent import (
    explicar_concepto,
    calcular_promedio
)

def test_explicar_concepto_exitoso():
    res = explicar_concepto("api")
    assert res["status"] == "success"

def test_explicar_concepto_nuevo_reto():
    res = explicar_concepto("devops")
    assert res["status"] == "success"

def test_explicar_concepto_no_existente():
    res = explicar_concepto("blockchain")
    assert res["status"] == "not_found"

def test_explicar_concepto_validacion_entrada():
    res = explicar_concepto(" ")
    assert res["status"] == "error"

def test_calcular_promedio_exitoso():
    res = calcular_promedio("12,16,20")
    assert res["promedio"] == pytest.approx(16)

def test_calcular_promedio_con_decimales():
    res = calcular_promedio("11.5,14.5")
    assert res["promedio"] == pytest.approx(13)

def test_calcular_promedio_fuera_de_rango():
    res = calcular_promedio("21,15,-5")
    assert res["status"] == "error"

def test_calcular_promedio_error_formato():
    res = calcular_promedio("once,doce")
    assert res["status"] == "error"