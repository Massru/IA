from tictactoeAlum import *

LIMITE = 3

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


def jugadaAdversario(nodo, modo):
    valida = False
    jugada = None
    while not valida:
        if modo == "n":
            fila = int(input("Fila: ")) - 1
            col = int(input("Col: ")) - 1
        if modo == "y":
            jugada = int(input("Posicion: "))
            match jugada:
                case 1:
                    fila = 3
                    col = 1
                case 2:
                    fila = 3
                    col = 2
                case 3:
                    fila = 3
                    col = 3
                case 4:
                    fila = 2
                    col = 1
                case 5:
                    fila = 2
                    col = 2
                case 6:
                    fila = 2
                    col = 3
                case 7:
                    fila = 1
                    col = 1
                case 8:
                    fila = 1
                    col = 2
                case 9:
                    fila = 1
                    col = 3
            fila -= 1
            col -= 1
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


def poda_ab(nodo):
    jugador: int = 1
    prof: int = 0
    v: int
    jugada: Jugada
    mejorJugada: Jugada = jugadas[0]
    intento: Nodo
    alfa = -np.inf
    beta = np.inf

    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, jugador)            
            v = valorMin_ab(intento, prof + 1, alfa, beta)
            if v > alfa:
                alfa = v
                mejorJugada = jugada
    nodo = aplicaJugada(nodo, mejorJugada, jugador)
    return nodo


def valorMin_ab(nodo, prof, alfa, beta):
    vmin: int
    i: int
    jugada: Jugada
    intento: Nodo

    if terminal(nodo):
        vmin = utilidad(nodo)
    else:
        if prof == LIMITE:
            vmin = heuristica(nodo)
        else:
            i = 0
            while(i<len(jugadas) and alfa < beta):
                jugada = jugadas[i]
                if esValida(nodo, jugada):
                    intento = aplicaJugada(nodo, jugada, -1)
                    beta = min(beta, valorMax_ab(intento, prof + 1, alfa, beta))
                i += 1
            vmin = beta
    return vmin


def valorMax_ab(nodo, prof, alfa, beta):
    vmax: int
    i: int
    jugada: Jugada
    intento: Nodo

    if terminal(nodo):
        vmax = utilidad(nodo)
    else:
        if prof == LIMITE:
            vmax = heuristica(nodo)
        else:
            i = 0
            while(i<len(jugadas) and alfa < beta):
                jugada = jugadas[i]
                if esValida(nodo, jugada):
                    intento = aplicaJugada(nodo, jugada, 1)
                    alfa = max(alfa, valorMin_ab(intento, prof + 1, alfa, beta))
                i += 1
            vmax = alfa
    return vmax