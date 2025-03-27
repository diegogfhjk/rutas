import pytest
from app.base_conocimiento import CONEXIONES
from app.algoritmo_a_star import a_star, heuristica_nula

def test_ruta_existente():
    ruta, costo = a_star("PuntoA", "PuntoB", CONEXIONES, heuristica_nula)
    assert ruta is not None
    assert costo < float("inf")

def test_ruta_inexistente():
    ruta, costo = a_star("X", "Y", CONEXIONES, heuristica_nula)
    assert ruta is None
    assert costo == float("inf")