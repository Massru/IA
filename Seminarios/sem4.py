from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

operadores = {"1": "IZQUIERDA", "2": "DERECHA"}

dataclass
class tEstado:
    # Atributos
    tablero: list
    ladrones: int
    banca: int
    N: int

    def __init__(self, tablero):
        self.tablero = tablero
        self.ladrones = 0
        self.banca = 0
        self.N = len(tablero)

    def __str__(self) -> str:
        return f"{self.tablero}\nLadrones: {self.ladrones}\nBanca: {self.banca}"
    

def aplicaOperador(operador, estado) -> tEstado:
    nuevo = deepcopy(estado)
    match operadores[operador]:
        case "IZQUIERDA":
            nuevo.ladrones += estado.tablero(0)
            nuevo.banca += estado.tablero(-1)
            nuevo.tablero.pop(0)
            nuevo.tablero.pop(estado.N - 1)
        case "DERECHA":
            nuevo.ladrones += estado.tablero(-1)
            nuevo.banca += estado.tablero(-2)
            nuevo.tablero.pop(estado.N - 1)
            nuevo.tablero.pop(estado.N - 2)
    nuevo.N -= 2
    return nuevo

def esValido(operador, estado) -> bool:
    return estado.N > 1

def testObjetivo(estado) -> bool:
    return (estado.ladrones > estado.banca) and estado.N < 2

def estadoInicial() -> tEstado:
    inicial = {4,3,2,5,7,1,8,6}
    return tEstado(inicial)
