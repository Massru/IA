from NPuzle_Alum import *

actual = estadoInicial()

print(actual.tablero)

while not testObjetivo(actual):
    oper = input(f"Introduzca una operacion {operadores} ")
    if esValido(oper, actual):
        actual = aplicaOperador(oper, actual)
    else:
        print("OPERACION INVALIDA")
    print(actual.tablero)

if testObjetivo(actual):
    print("OBJETIVO ALCANZADO")