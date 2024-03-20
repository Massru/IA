import numpy as np
from copy import deepcopy
from dataclasses import dataclass

operadores = {"1": "mis_der", "2": "mis_izq", "3": "can_izq", "4": "can_der", "5": "2can_der", "6": "2can_izq", "7": "2mis_der", "8": "2mis_izq", "9": "2_der", "10": "2_izq"}

@dataclass
class tEstado:
    can_izq: int
    can_der: int
    mis_izq: int
    mis_der: int
    bote: int

def esValido(op, e):
    valido = True
    match op:
        case("mis_der"):
            valido = e.bote == -1 and (e.mis_izq -1 >= 0) and (e.mis_izq - 1 >= e.can.izq) and (e.mis_der + 1 >= e.can_der) and (e.mis_der + 1 <= 3)


def aplicaOperador(op, e):
    nuevo = deepcopy(e)
    match op:
        case("mis_der"):
            nuevo.mis_izq -= 1
            nuevo.mis_der += 1
            nuevo.bote *= -1


def testObjetivo(e):
    return e.bote == 1 and e.mis_der == 3 and e.can_der == 3