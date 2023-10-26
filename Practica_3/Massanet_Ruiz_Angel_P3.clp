(deftemplate Aeronave
    (slot identificador)
    (slot compañia)
    (slot origen)
    (slot destino)
    (slot velocidad)
    (slot peticion (allowed-values Ninguna Despegue Atterizaje Emergencia Rumbo))
    (slot estado (allowed-values enTierra Ascenso Crucero Descenso)(default enTierra))
)

(deftemplate Aerodromo
    (slot identificador)
    (slot ciudad)
    (slot estadoRadar (allowed-values ON OFF))
    (slot visibilidad)
    (slot viento)
)

(deftemplate Piloto
    (slot aeronave)
    (slot estado (allowed-values OK SOS Ejecutando Stand_by)(default Stand_by))
)

(deftemplate Vuelo
    (slot aerodromo1)
    (slot aerodromo2)
    (slot distancia)
    (slot velocidadDespegue (default 240))
    (slot velocidadCrucero (default 700))
)

(deffunction CalculaHoras (?dis ?vel)
    (return (div ?dis ?vel))
)

(deffunction CalculaMinutos (?dis ?vel)
    (bind ?resto(mod ?dis ?vel))
    (bind ?minutos(* (/ ?resto ?vel) 60))
    (return ?minutos)
)

(deffacts iniciales
    (Aeronave (identificador FX001)(compañia Iberia)(origen Cadiz)(destino Barcelona)(velocidad 0)(peticion Despegue)(estado enTierra))
    (Aerodromo (identificador CAD)(ciudad Cadiz)(estadoRadar ON)(visibilidad 10)(viento 50))
    (Aerodromo (identificador BAR)(ciudad Barcelona)(estadoRadar ON)(visibilidad 10)(viento 50))
    (Piloto (aeronave FX001)(estado OK))
    (Vuelo (aerodromo1 CAD)(aerodromo2 BAR)(distancia 2000)(velocidadDespegue 300)(velocidadCrucero 800))
)

(defrule Despegar
    ?a <- (Aeronave (identificador ?id)(compañia ?com)(estado enTierra)(peticion Despegue)(origen ?o)(destino ?d))
    ?p <- (Piloto (estado OK)(aeronave ?id))
    (Aerodromo (identificador ?id2)(ciudad ?o)(estadoRadar ON)(visibilidad ?vis)(viento ?vie))
    (Aerodromo (identificador ?id3)(ciudad ?d))
    (Vuelo (aerodromo1 ?id2)(aerodromo2 ?id3)(velocidadDespegue ?vel))
    (test (> ?vis 5))
    (test (< ?vie 75))
    =>
    (modify ?p (estado Ejecutando))
    (modify ?a (estado Ascenso)(velocidad ?vel)(peticion Ninguna))
    (printout t "La aeronave " ?id " de la compañia " ?com " va a realizar la acción de despegue desde el aeródromo " ?id2 " de " ?o " con destino " ?d crlf)
)

(defrule Excepción
    (Piloto (estado ~OK)(aeronave ?id))
    ?a <- (Aeronave (identificador ?id)(peticion Despegue)(compañia ?com)(destino ?d)(origen ?o))
    (Aerodromo (identificador ?id2)(ciudad ?o))
    (Aerodromo (identificador ?id3)(ciudad ?d))
    (Vuelo (aerodromo1 ?id2)(aerodromo2 ?id3))
    =>
    (modify ?a (peticion Emergencia))
    (printout t "ATENCION El piloto de la aeronave " ?id " de la compañia " ?com " no se encuentra disponible para iniciar el despegue desde el aeródromo " ?id2 " con destino " ?id3 crlf)
)

(defrule Crucero
    ?a <- (Aeronave (estado Ascenso)(origen ?o)(destino ?d)(identificador ?id))
    (Vuelo (aerodromo1 ?id2)(aerodromo2 ?id3)(velocidadCrucero ?vel)(distancia ?dis))
    (Aerodromo (identificador ?id2)(ciudad ?o))
    (Aerodromo (identificador ?id3)(ciudad ?d))
    ?p <- (Piloto (aeronave ?id))
    =>
    (modify ?a (estado Crucero)(velocidad ?vel))
    (modify ?p (estado Stand_by))
    (printout t "El despegue ha sido correcto, se estima una duracion de " (CalculaHoras ?dis ?vel) " horas y " (CalculaMinutos ?dis ?vel) " minutos" crlf)
)
