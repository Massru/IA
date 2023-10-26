(deftemplate Valvula
    (slot nombre)
    (slot estado (allowed-values abierta cerrada)(default cerrada))
    (slot presion (default 0))
    (slot T1 (default 0))
    (slot T2 (default 0))
)

(deffacts iniciales
    (Valvula (nombre Entrada)(T1 101)(T2 35)(presion 1))
    (Valvula (nombre Salida)(T1 101)(T2 155)(presion 5))
    (Valvula (nombre Pasillo1)(T1 99)(T2 37)(estado cerrada))
)

(defrule R1
    ?v <- (Valvula (estado abierta)(presion 5))
    =>
    (modify ?v (estado cerrada)(presion 0))
)

(defrule R2
    ?v <- (Valvula (estado cerrada)(presion ?pr)(T1 ?t))
    (test (< ?pr 10))
    (test (> ?t 35))
    =>
    (aumento (?pr ?t))
    (modify ?v (estado abierta)(presion ?pr)(T1 ?t))
)

(deffunction aumento (?presion ?t1)
    (while (> ?t1 35)
        (bind ?presion (+ ?presion 1))
        (bind ?t1 (- ?t1 5)))
)

(defrule R3
    ?v1 <- (Valvula (nombre ?n1)(T1 ?t1)(T2 ?t2))
    ?v2 <- (Valvula (nombre ?n2)(T1 ?t1_2)(T2 ?t2))
    (test (!= ?n1 ?n2))
    (test (< ?t1 ?t1_2))
    =>
    (decremento (?t1 ?t1_2))
    (modify ?v1 (estado abierta))
    (modify ?v2 (estado abierta)(T1 ?t1_2))
)

(deffunction decremento (?t1 ?t2)
    (while (> ?t2 ?t1)
    (bind ?t2 (- ?t2 ?t1)))
)