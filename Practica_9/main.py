from minimaxAlum import *

ganador = 0
jugador = int(input("Introduzca el 1er jugador: 1 AI, 2 Tú: "))
modo = input("¿Desea jugar con el teclado numérico? y/n: ")
busqueda = input("Tipo de búsqueda: 1 Minimax 2 Poda_ab: ")

if jugador != 1:
    jugador = -1

juego = nodoInicial()
while juego.vacias > 0 and not ganador:
    if jugador == 1:
        if busqueda == "1":
            juego = minimax(juego)
        else:
            juego = poda_ab(juego)
    else:
        juego = jugadaAdversario(juego, modo)
    print(juego)
    if terminal(juego):
        ganador = utilidad(juego)
    jugador = opuesto(jugador)

match ganador:
    case 0:
        print("EMPATE")
    case 100:
        print("GANA MAX (IA)")
    case -100:
        print("GANA MIN (JUGADOR)")
