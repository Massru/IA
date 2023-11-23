from busquedaAlum import *

Busqueda = input("Selecciona tipo de búsqueda:\n1. A*\n2. A* con Control de estados repetidos\n")

match Busqueda:
    case "1":
        objetivo = busqueda()
    case "2":
        objetivo = busquedaControl()



if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")
