from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
import numpy as np

visual = {1: "❌", -1: "⭕", 0.0: " "}


@dataclass
class Nodo:
    tablero: np.array
    vacias: int
    N: int

    def __init__(self, tablero):
        self.tablero = tablero
        self.N = self.tablero.shape[0]
        self.vacias = len(np.where(tablero == 0)[0])

    def __str__(self):
        string = f"{' ----+----+----'}\n|"
        for i in range(self.tablero.shape[0]):
            for j in range(self.tablero.shape[1]):
                if self.tablero[i, j] == 0:
                    string += "    |"
                else:
                    string += f" {visual[self.tablero[i, j]]} |"
            if i == 2 and j == 2:
                string += f"\n ----+----+----\n"
            else:
                string += f"\n ----+----+----\n|"
        return f"{string}"


@dataclass
class Jugada:
    x: int
    y: int

    def __str__(self):
        return f"\nFila: ({self.x}, Col: {self.y})"


######
# Se crean todas las posibles jugadas para el for de rango (for jugada in jugadas)
jugadas = []
for i in range(0, 3):
    for j in range(0, 3):
        jugadas.append(Jugada(i, j))
######

""" Funciones complementarias
    * crearNodo
    * nodoInicial
    * opuesto
"""


def crearNodo(tablero):
    return Nodo(tablero)


def nodoInicial():
    tablero_inicial = np.zeros((3, 3))
    return Nodo(tablero_inicial)


def opuesto(jugador):
    return jugador * -1


""" Funciones Búsqueda MiniMax
    * aplicaJugada
    * esValida
    * terminal
    * utilidad
"""


def aplicaJugada(actual: Nodo, jugada: Jugada, jugador: int) -> Nodo:
    """Realiza una copia del nodo recibido como parámetro y aplica la jugada indicada,
    modificando para ello los atributos necesarios. Para esto, se tiene en cuenta qué
    jugador realiza la jugada.

    Args:
        actual (Nodo)
        jugada (Jugada)
        jugador (int)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, puede mantener
        esta excepción.

    Returns:
        Nodo: Contiene la información del nuevo estado del juego.
    """

    nuevo = deepcopy(actual)
    nuevo.tablero[jugada.x, jugada.y] = jugador
    nuevo.vacias -= 1

    #raise NotImplementedError

    return nuevo


def esValida(actual: Nodo, jugada: Jugada) -> bool:
    """Comprueba si dada una Jugada, es posible aplicarla o no.

    Args:
        actual (Nodo)
        jugada (Jugada)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, puede mantener
        esta excepción.

    Returns:
        bool: Devuelve True en caso de que pueda realizarse la Jugada, False en caso contrario
    """

    valido = False
    if jugada.x >= 0 and jugada.x < actual.N and jugada.y >= 0 and jugada.y < actual.N:
        if actual.tablero[jugada.x, jugada.y] == 0:
            valido = True

    return valido

    #raise NotImplementedError


def terminal(actual: Nodo) -> bool:
    """Comprueba si el juego se ha acabado, ya sea porque alguno de los jugadores ha ganado o bien
    porque no sea posible realizar ningún movimiento más.

    Args:
        actual (Nodo)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, puede mantener
        esta excepción.

    Returns:
        bool: Devuelve True en caso de Terminal, False en caso contrario
    """
    acabado = False

    # Comprobamos si hay alguna fila con 3 fichas iguales
    for i in range(actual.N):
        if actual.tablero[i, 0] == actual.tablero[i, 1] == actual.tablero[i, 2] and actual.tablero[i, 0] != 0:
            acabado = True
        
    # Comprobamos si hay alguna columna con 3 fichas iguales
    for i in range(actual.N):
        if actual.tablero[0, i] == actual.tablero[1, i] == actual.tablero[2, i] and actual.tablero[0, i] != 0:
            acabado = True
        
    # Comprobamos si hay alguna diagonal con 3 fichas iguales
    if actual.tablero[0, 0] == actual.tablero[1, 1] == actual.tablero[2, 2] and actual.tablero[0, 0] != 0:
        acabado = True
    if actual.tablero[0, 2] == actual.tablero[1, 1] == actual.tablero[2, 0] and actual.tablero[0, 2] != 0:
        acabado = True
    
    # Comprobamos si hay alguna casilla vacia
    for i in range(actual.N):
        for j in range(actual.N):
            if actual.tablero[i, j] == 0:
                acabado = False
                break
            else:
                acabado = True

    return acabado
    #raise NotImplementedError


def utilidad(nodo: Nodo) -> int:
    """La función de utilidad, también llamada objetivo, asigna un valor numérico al nodo recibido como parámetro.
    Por ejemplo, en un juego de 'Suma cero', se puede establecer que devuelve -100, 0, 100 en función de qué jugador
    gana o bien si hay un empate.

    Args:
        nodo (Nodo)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, puede mantener
        esta excepción.

    Returns:
        int: Valor de utilidad
    """

    gana = 0

    if nodo.tablero[0, 0] == nodo.tablero[1, 1] == nodo.tablero[2, 2] and nodo.tablero[0, 0] != 0:
        gana = nodo.tablero[0, 0]
    if nodo.tablero[0, 2] == nodo.tablero[1, 1] == nodo.tablero[2, 0] and nodo.tablero[0, 2] != 0:
        gana = nodo.tablero[0, 2]
    
    for i in range(nodo.N):
        if nodo.tablero[i, 0] == nodo.tablero[i, 1] == nodo.tablero[i, 2] and nodo.tablero[i, 0] != 0:
            gana = nodo.tablero[i, 0]
    
    for i in range(nodo.N):
        if nodo.tablero[0, i] == nodo.tablero[1, i] == nodo.tablero[2, i] and nodo.tablero[0, i] != 0:
            gana = nodo.tablero[0, i]

    if gana == 1:
        return 100
    elif gana == -1:
        return -100
    else:
        return 0
    
    #raise NotImplementedError