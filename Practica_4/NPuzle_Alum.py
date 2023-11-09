import numpy as np
from dataclasses import dataclass
from copy import deepcopy

operadores = {"8": "ARRIBA", "2": "ABAJO", "4": "IZQUIERDA", "6": "DERECHA"}

@dataclass
class tEstado:
    tablero: np.ndarray
    fila: int
    col: int

    def __init__(self, tablero: np.ndarray):
        self.tablero = tablero
        self.N = self.tablero.shape[0]
        self.fila, self.col = np.where(self.tablero == 0)

    def __repr__(self) -> str:
        return f"{self.tablero}\n Fila: {self.fila}\n Col: {self.col}\n"

    def crearHash(self) -> str:
        return f"{self.tablero.tobytes()}{self.fila}{self.col}"


def estadoInicial() -> tEstado:
    puzle_inicial = np.array([[0, 2, 3], [1, 4, 5], [8, 7, 6]])
    return tEstado(puzle_inicial)


def estadoObjetivo() -> tEstado:
    puzle_final = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    return tEstado(puzle_final)


def coste(operador, estado):
    return 1


def dispOperador(operador):
    print("~" * 10)
    print("Movimiento hacia ", operadores[operador])


def iguales(actual: tEstado, objetivo: tEstado) -> bool:
    return (actual.tablero == objetivo.tablero).all()


def testObjetivo(actual) -> bool:
    objetivo = estadoObjetivo()
    return iguales(actual, objetivo)


def esValido(operador: str, estado) -> bool:
    valido = False
    match operadores[operador]:
        case "ARRIBA":
            if estado.fila != 0:
                valido = True
        case "ABAJO":
            if estado.fila != estado.N-1:
                valido = True
        case "IZQUIERDA":
            if estado.col != 0:
                valido = True
        case "DERECHA":
            if estado.col != estado.N-1:
                valido = True
    return valido


def aplicaOperador(operador: str, estado) -> bool:
    nuevo = deepcopy(estado)
    ficha = 0
    match operadores[operador]:
        case "ARRIBA":
            ficha = nuevo.tablero[nuevo.fila-1, nuevo.col]
            nuevo.tablero[nuevo.fila-1, nuevo.col] = nuevo.tablero[nuevo.fila, nuevo.col]
            nuevo.tablero[nuevo.fila, nuevo.col] = ficha
            nuevo.fila -= 1
        case "ABAJO":
            ficha = nuevo.tablero[nuevo.fila+1, nuevo.col]
            nuevo.tablero[nuevo.fila+1, nuevo.col] = nuevo.tablero[nuevo.fila, nuevo.col]
            nuevo.tablero[nuevo.fila, nuevo.col] = ficha
            nuevo.fila += 1
        case "IZQUIERDA":
            ficha = nuevo.tablero[nuevo.fila, nuevo.col-1]
            nuevo.tablero[nuevo.fila, nuevo.col-1] = nuevo.tablero[nuevo.fila, nuevo.col]
            nuevo.tablero[nuevo.fila, nuevo.col] = ficha
            nuevo.col -= 1
        case "DERECHA":
            ficha = nuevo.tablero[nuevo.fila, nuevo.col+1]
            nuevo.tablero[nuevo.fila, nuevo.col+1] = nuevo.tablero[nuevo.fila, nuevo.col]
            nuevo.tablero[nuevo.fila, nuevo.col] = ficha
            nuevo.col += 1
    return nuevo
