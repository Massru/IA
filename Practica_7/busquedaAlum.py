from __future__ import annotations
from NPuzle_Alum import *
import numpy as np

@dataclass
class Nodo:
    estado: tEstado
    operador: str
    costeCamino: int
    profundidad: int
    valHeuristica: int  # Por el momento se le puede asignar el valor 0.
    padre: Nodo

    def __str__(self) -> str:
        return f'{"- " * 10}\n{self.estado.tablero}, Operador: {operadores[self.operador]}, Heu:{self.valHeuristica}\n{"- " * 10}'

    def hash(self) -> str:
        return self.estado.crearHash()
    
    def __lt__(self, nodo):
        self.valHeuristica + self.costeCamino < nodo.valHeuristica + nodo.costeCamino


def nodoInicial() -> Nodo:
    return Nodo(estadoInicial(), "0", 0, 0, BusquedaHeuristica(estadoInicial()), None)


def dispCamino(nodo):
    lista = []
    aux = nodo
    while aux.padre != None:
        lista.append((aux.estado.tablero, aux.operador))
        aux = aux.padre
    for i in lista[::-1]:
        print("Movimiento hacia: ", operadores[i[1]], "\n", i[0])
        print()


def dispSolucion(nodo):
    dispCamino(nodo)
    print("Profundidad: ", nodo.profundidad)
    print("Coste: ", nodo.costeCamino)


def expandir(nodo) -> list:
    nodos = []

    # Completar el código.
    op = 2
    for op in operadores:  
        if esValido(op, nodo.estado):
            nuevo = aplicaOperador(op, nodo.estado)
            nodos.append(Nodo(nuevo, op, nodo.costeCamino + 1, nodo.profundidad + 1, BusquedaHeuristica(nuevo), nodo))

    return nodos


def busqueda() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    cerrados = {}  # Cerrados es un diccionario para que funcione como una tabla hash
    abiertos.append(raiz)


    while not objetivo and len(abiertos) > 0:

        actual = abiertos[0]
        abiertos.pop(0)

        objetivo = testObjetivo(actual.estado)
        if not objetivo:
            sucesores = expandir(actual)
            abiertos += sucesores
            abiertos.sort()

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo

def busquedaControl() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    cerrados = {}  # Cerrados es un diccionario para que funcione como una tabla hash
    abiertos.append(raiz)

    while not objetivo and len(abiertos) > 0:

        actual = abiertos[0]
        abiertos.pop(0)

        objetivo = testObjetivo(actual.estado)

        if not objetivo and (actual.hash() not in cerrados.keys() or (actual.hash() in cerrados.keys() and actual.valHeuristica < cerrados[actual.hash()])):
            sucesores = expandir(actual)
            abiertos += sucesores
            abiertos.sort()
            cerrados.update({actual.hash(): actual.valHeuristica})


    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo


def BusquedaHeuristica(actual: tEstado) -> int:

    heu = 0

    for i in range(1, actual.N **2):
        fila_obj, col_obj = np.where(estadoObjetivo().tablero == i)
        fila, col = np.where(actual.tablero == i)
        heu += (abs(fila-fila_obj) + abs(col-col_obj))

    return heu