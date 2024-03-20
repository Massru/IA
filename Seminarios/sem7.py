from copy import deepcopy
from dataclasses import dataclass
import numpy as np
import math

operadores = {"1": "DOWNLEFT", "3": "DOWNRIGHT", "7": "UPLEFT", "9": "UPRIGHT"}

@dataclass
class tEstado:
    e: np.ndarray
    f: int
    c: int

def esValido(op, e):
    valido = False
    match operadores(op):
        case "DOWNLEFT":
            f, c = e.shape
            valido = (e.f < f-1 and e.c < c-1 and e.e[e.f+1, e.c+1] != -1)
        case "DOWNRIGHT":
            pass
        case "UPLEFT":
            valido = (e.f > 0 and e.c > 0 and e.e[e.f-1,e.c-1] != -1)
        case "UPRIGHT":
            pass

def aplicaOperador(op, e):
    nuevo = deepcopy(e)
    match operadores(op):
        case "UPLEFT":
            nuevo.f -= 1
            nuevo.c -= 1
        case "UPRIGHT":
            pass
        case "DOWNLEFT":
            pass
        case "DOWNRIGHT":
            pass
    
    if nuevo.e[nuevo.f, nuevo.c] == 2:
        nuevo.e[nuevo.f, nuevo.c] = 3
    nuevo.e[nuevo.f, nuevo.c] = 1
    nuevo.e[e.f, e.c] = 0

def testObjetivo(op, e):
    f, c = np.where(e.e == 2)
    if len(f) == 0 and len(c) == 0:
        return True
    
    f, c = np.where(e.e == 3)

def heuristica(e):
    f, c = np.where(e.e == 2)
    return math.sqrt((f - e.f) ** 2 + (c - e.c) ** 2)
