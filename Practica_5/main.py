from busquedaAlum import *

busqueda = input("Selecciona tipo de búsqueda:\n1. Anchura\n2. Anchura con Control de estados repetidos\n3. Profundidad con Control de estados repetidos\n4. Profundidad Limitada\n5. Profundidad Limitada Iterativa\n")

match busqueda:
    case "1":
        objetivo = busquedaAnchura()
    case "2":
        objetivo = busquedaAnchuraControl()
    case "3":
        objetivo = busquedaProfundidadControl()
    case "4":
        prof = input("Inserte profundidad límite de la búsqueda: ")
        objetivo = busquedaProfundidadLimitada(int(prof))
    case "5":
        objetivo = busquedaProfundidadLimitadaIterativa()

if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")
