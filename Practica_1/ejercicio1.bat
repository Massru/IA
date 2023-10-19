(clear)
(reset)
(deftemplate persona
    (multislot nombre)  ;para almacenar nombre y apellidos
    (slot dni (type INTEGER))
    (slot profesion (default estudiante))
    (slot nacionalidad (allowed-values Es Fr Po Al In It))
);persona

(deftemplate intelectual_europeo
    (multislot nombre)
    (slot dni)
    (slot idioma)
    (slot nacionalidad)
);intelectual_europeo

(list-deftemplates) ;;para mostrar las plantillas definidas

(deffacts iniciales
    ;;con hechos estructurados
    (persona(nombre Mario Cantero Cansino)
            (dni 122333)
            (profesion escritor)
            (nacionalidad Es))
    (persona (nombre Juana Bodega Gallego) (dni 3334444))
    ;;con hechos no estructurados
    (ciudad Gertrudis Cadiz)
    (ciudad Filoberto Sevilla)
);;iniciales

(facts);; visualiza los hechos actuales

(reset)

(assert (ciudad Juana Cadiz))
(assert (persona (nombre Alicia Mata Rueda) (dni 1234)))
(assert (intelectual_europeo (nombre Victor Hugo) (idioma frances)))

(assert (persona(nombre Mateo Duran barbera)
                (dni 333221)))