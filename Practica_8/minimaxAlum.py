from tictactoeAlum import *


def PSEUDOminimax(nodo):
    mejorJugada = -1
    puntos = -2
    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, 1)
            util = utilidad(intento)
            if util > puntos:
                puntos = util
                mejorJugada = jugada
    nodo = aplicaJugada(nodo, mejorJugada, 1)
    return nodo


def jugadaAdversario(nodo):
    valida = False
    jugada = None
    while not valida:
        fila = int(input("Fila: ")) - 1
        col = int(input("Col: ")) - 1
        jugada = Jugada(fila, col)
        valida = esValida(nodo, jugada)
        if not valida:
            print("\n Intenta otra posicion del tablero \n")
    nodo = aplicaJugada(nodo, jugada, -1)
    return nodo


def minimax(nodo):
    jugador = 1
    mejorJugada = jugadas[0]
    max = -10000
    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, jugador)
            max_actual = valorMin(intento)
            if max_actual > max:
                max = max_actual
                mejorJugada = jugada
    nodo = aplicaJugada(nodo, mejorJugada, jugador)
    return nodo


def valorMin(nodo):
    valor_min = np.inf
    jugador = -1
    if terminal(nodo):
        valor_min = utilidad(nodo)
    else:
        for jugada in jugadas:
            if esValida(nodo, jugada):
                valor_min = min(valor_min, valorMax(aplicaJugada(nodo, jugada, jugador)))
    return valor_min   


def valorMax(nodo):
    valor_max = -np.inf
    jugador = 1
    if terminal(nodo):
        valor_max = utilidad(nodo)
    else:
        for jugada in jugadas:
            if esValida(nodo, jugada):
                valor_max = max(valor_max, valorMin(aplicaJugada(nodo, jugada, jugador)))
    return valor_max