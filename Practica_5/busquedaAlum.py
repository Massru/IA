from __future__ import annotations
from NPuzle_Alum import *


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


def nodoInicial() -> Nodo:
    return Nodo(estadoInicial(), "0", 0, 0, 0, None)


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
    coste = 0
    profundidad = 0
    op = 2
    for op in operadores:  
        if esValido(op, nodo.estado):
            nuevo = aplicaOperador(op, nodo.estado)
            nodos.append(Nodo(nuevo, op, nodo.costeCamino + 1, nodo.profundidad + 1, 0, nodo))

    return nodos


def busquedaAnchura() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    cerrados = {}  # Cerrados es un diccionario para que funcione como una tabla hash
    abiertos.append(raiz)
    nodosExplorados = 0

    while not objetivo and len(abiertos) > 0:

        actual = abiertos[0]
        abiertos.pop(0)

        objetivo = testObjetivo(actual.estado)
        if not objetivo:
            sucesores = expandir(actual)
            abiertos += sucesores
            nodosExplorados += 1


    if objetivo:
        dispSolucion(actual)
        print("Nodos explorados: ", nodosExplorados)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo


def busquedaAnchuraControl() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    cerrados = {}  # Cerrados es un diccionario para que funcione como una tabla hash
    abiertos.append(raiz)
    nodosExplorados = 0

    while not objetivo and len(abiertos) > 0:

        actual = abiertos[0]
        abiertos.pop(0)

        objetivo = testObjetivo(actual.estado)

        if not objetivo and actual.hash() not in cerrados.keys():
            sucesores = expandir(actual)
            abiertos += sucesores
            nodosExplorados += 1
            cerrados.update({actual.hash(): actual})


    if objetivo:
        dispSolucion(actual)
        print("Nodos explorados: ", nodosExplorados)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo


def busquedaProfundidadControl() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    cerrados = {}  # Cerrados es un diccionario para que funcione como una tabla hash
    abiertos.append(raiz)
    nodosExplorados = 0

    while not objetivo and len(abiertos) > 0:

        actual = abiertos[0]
        abiertos.pop(0)

        objetivo = testObjetivo(actual.estado)

        if not objetivo and actual.hash() not in cerrados.keys():
            sucesores = expandir(actual)
            abiertos = sucesores + abiertos
            nodosExplorados += 1
            cerrados.update({actual.hash(): actual})

    if objetivo:
        dispSolucion(actual)
        print("Nodos explorados: ", nodosExplorados)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo


def busquedaProfundidadLimitada(pr) -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    cerrados = {}  # Cerrados es un diccionario para que funcione como una tabla hash
    abiertos.append(raiz)
    nodosExplorados = 0

    while not objetivo and len(abiertos) > 0:

        actual = abiertos[0]
        abiertos.pop(0)

        objetivo = testObjetivo(actual.estado)

        if not objetivo and actual.hash() not in cerrados.keys() and actual.profundidad < pr:
            sucesores = expandir(actual)
            abiertos = sucesores + abiertos
            nodosExplorados += 1

        cerrados.update({actual.hash(): actual})

    if objetivo:
        dispSolucion(actual)
        print("Nodos explorados: ", nodosExplorados)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo


def busquedaProfundidadLimitadaIterativa() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    cerrados = {}  # Cerrados es un diccionario para que funcione como una tabla hash
    pr = 0
    nodosExplorados = 0

    while not objetivo:

        abiertos.append(raiz)

        while not objetivo and len(abiertos) > 0:

            actual = abiertos[0]
            abiertos.pop(0)

            objetivo = testObjetivo(actual.estado)

            if not objetivo and actual.hash() not in cerrados.keys() and actual.profundidad < pr:
                sucesores = expandir(actual)
                abiertos = sucesores + abiertos
                nodosExplorados += 1

            cerrados.update({actual.hash(): actual})
        
        pr += 1
        cerrados.clear()

    if objetivo:
        dispSolucion(actual)
        print("Nodos explorados: ", nodosExplorados)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo
