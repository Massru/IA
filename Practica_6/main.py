from busquedaAlum import *


busqueda = input("Selecciona tipo de búsqueda:\n1. Voraz\n2. Voraz con Control de estados repetidos\n")

match busqueda:
    case "1":
        objetivo = busquedaVoraz()
    case "2":
        objetivo = busquedaVorazControl()


if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")
