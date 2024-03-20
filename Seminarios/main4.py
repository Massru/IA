from sem4 import *

actual = estadoInicial()

while not testObjetivo(actual) and actual.N > 1:
    oper = input(f"Introduzca una operacion {operadores} ")
    if esValido(oper, actual):
        actual = aplicaOperador(oper, actual)
    print(actual)

if testObjetivo(actual):
    print("Objetivo alcanzado")