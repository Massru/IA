from copy import deepcopy
from dataclasses import dataclass
import numpy as np
import math
from itertools import product
from random import sample

palos = ["ESPADAS", "OROS", "COPAS", "BASTOS"]
numeros = [list.range(1,13)]
jugadas = (list(product(palos, numeros)))

J1 = sample(jugadas, 24)
J2 = list(set(jugadas) - set(J1))

@dataclass
class Nodo:
    mesa: dict
    cMin: int
    cMax: int

@dataclass
class Jugada:
    palo: str
    num: int


def esValida(nodo, jugada, jugador):
    valida = False
    if jugada.num == 5:
        valida = True
    if jugada.num > 5:
        valida = nodo.mesa[jugada.palo][jugada.num - 1 + 1] == 2
    if jugada.num < 5:
        valida = nodo.mesa[jugada.palo][jugada.num - 1 - 1] == 2
    return valida and nodo.mesa[jugada.palo][jugada.num - 1] == jugador

def aplicaJugada(nodo, jugada, jugador):
    nuevo = deepcopy(nodo)
    nuevo.mesa[jugada.palo][jugada.num - 1] = 2
    if jugador == -1:
        nuevo.cMin -= 1
    if jugador == 1:
        nuevo.cMax -= 1
    return nuevo

def terminal(nodo):
    return nodo.cmin == 0 or nodo.cMax == 0

def utilidad(nodo):
    utilidad = 0
    if nodo.cMin == 0:
        utilidad = -100
    if nodo.cMax == 0:
        utilidad = 100
    return utilidad

def heuristica(nodo):
    return nodo.cMin - nodo.cMax    