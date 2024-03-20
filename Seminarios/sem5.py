import numpy as np
from copy import deepcopy
from dataclasses import dataclass

@dataclass
class tEstado:
    M: np.ndarray
    f: list
    c: list
    N: list

    def __init__(self, tablero, filas, cols):
        self.M = tablero
        self.f = filas
        self.c = cols
        self.N = self.M.shape[0] #shape[0] -> longitud de filas, [1] -> columnas

    def __str__(self):
        v = {-1: "⬛", 0: "⬜", 1: "🟥", 2: "🟩", 3: "🟦"}
        str = ""
        for i in range(self.N):
            for j in range(self.N):
                str += f"{v[self.M[i, j]]}"
            str += '\n'
        return str
    

def testObjetivo(actual):
    objetivo = estadoObjetivo()
    return (actual.M == objetivo.M).all()

operadores = {
    "1": "ARRIBA_A",
    "2": "ABAJO_A",
    "3": "IZQUIERDA_A",
    "4": "DERECHA_A",
    "5": "ARRIBA_B",
    "6": "ABAJO_B",
    "7": "IZQUIERDA_B",
    "8": "DERECHA_B",
    "9": "ARRIBA_C",
    "10": "ARRIBA_C",
    "11": "IZQUIERDA_C",
    "12": "DERECHA_C"
}

def esValido(op, estado):
    valido = True
    match operadores[op]:
        case "ARRIBA_A":
            valido = (
                estado.f[0] > 1
                and estado.M[estado.f[0]-1, estado.c[0]-1] == 0
                and estado.M[estado.f[0]-2, estado.c[0]] == 0       #Las filas y columnas se calculan a partir del centro
                and estado.M[estado.f[0]-1, estado.c[0]+1] == 0
            )
        case "ABAJO_A":
            valido = (
                estado.f[0] < estado.N - 1
                and estado.M[estado.f[0]+1,estado.c[0]-1] == 0
                and estado.M[estado.f[0]+2,estado.c[0]] == 0
                and estado.M[estado.f[0]+1,estado.c[0]+1] == 0
            )
        case "IZQUIERDA_A":
            valido = (
                estado.c[0] > 1
                and estado.M[estado.f[0]-1,estado.c[0]-1] == 0
                and estado.M[estado.f[0],estado.c[0]-2] == 0
                and estado.M[estado.f[0]+1,estado.c[0]-1] == 0
            )
        case "DERECHA_A":
            valido = (
                estado.c[0] < estado.N - 1
                and estado.M[estado.f[0]-1,estado.c[0]+1] == 0
                and estado.M[estado.f[0],estado.c[0]+2] == 0
                and estado.M[estado.f[0]+1,estado.c[0]+1] == 0
            )

#PRECONDICION EL OPERADOR ES VALIDO
def aplicaOperador(op, estado):
    nuevo = deepcopy(estado)
    match operadores[op]:
        case "ARRIBA_A":
            nuevo.M[estado.f[0]-1, estado.c[0]-1] = 1
            nuevo.M[estado.f[0]-2, estado.c[0]] = 1
            nuevo.M[estado.f[0]-1, estado.c[0]+1] = 1
            nuevo.M[estado.f[0], estado.c[0]-1] = 0
            nuevo.M[estado.f[0]+1, estado.c[0]] = 0
            nuevo.M[estado.f[0], estado.c[0]+1] = 0
            nuevo.f[0] -= 1
        case "ABAJO_A":
            nuevo.M[estado.f[0]+1, estado.c[0]-1] = 1
            nuevo.M[estado.f[0]+2, estado.c[0]] = 1
            nuevo.M[estado.f[0]+1, estado.c[0]+1] = 1
            nuevo.M[estado.f[0], estado.c[0]-1] = 0
            nuevo.M[estado.f[0]-1, estado.c[0]] = 0
            nuevo.M[estado.f[0], estado.c[0]+1] = 0
            nuevo.f[0] += 1            
        case "IZQUIERDA_A":
            nuevo.M[estado.f[0]-1, estado.c[0]-1] = 1
            nuevo.M[estado.f[0], estado.c[0]-2] = 1
            nuevo.M[estado.f[0]+1, estado.c[0]-1] = 1
            nuevo.M[estado.f[0]-1, estado.c[0]] = 0
            nuevo.M[estado.f[0], estado.c[0]+1] = 0
            nuevo.M[estado.f[0]+1, estado.c[0]] = 0
            nuevo.c[0] -= 1
        case "DERECHA_A":
            nuevo.M[estado.f[0]-1, estado.c[0]+1] = 1
            nuevo.M[estado.f[0], estado.c[0]+2] = 1
            nuevo.M[estado.f[0]+1, estado.c[0]+1] = 1
            nuevo.M[estado.f[0]-1, estado.c[0]] = 0
            nuevo.M[estado.f[0], estado.c[0]-1] = 0
            nuevo.M[estado.f[0]+1, estado.c[0]] = 0
            nuevo.c[0] += 1