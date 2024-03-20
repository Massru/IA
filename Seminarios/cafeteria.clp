(deftemplate Personal
    (slot DNI)
    (slot nombre)
    (slot turno (allowed-values mañana tarde ambos))
    (slot ventas)
    (slot encargado (allowed-values si no))
)

(deftemplate Producto
    (slot identificador)
    (slot nombre)
    (slot stock_cafeteria)
    (slot stock_almacen)
    (slot precio)
    (slot maximo (default 30))
)

(deftemplate Venta
    (slot personal)
    (slot producto)
    (slot unidades)
    (slot pago (allowed-values tarjeta efectivo bono))
)

(defrule AsignarVenta
    (declare (salience 1))
    ?pers <- (Personal (DNI ?dni)(nombre ?nombre)(ventas ?ventas))
    ?prod <- (Producto (identificador ?id)(nombre ?nomprod)(stock_cafeteria ?stock_c)(precio ?precio))
    ?v <- (Venta (personal ?dni)(producto ?id)(unidades ?ud)(pago ?pago))
    (test (>= ?stock_c ?ud))
    (test (> ?ud 0))
    =>
    (bind ?aux (+ ?ventas (* ?ud ?precio)))
    (modify ?pers (ventas ?aux))
    (modify ?prod (stock_cafeteria (- ?stock_c ?ud)))
    (retract ?v)
    (printout t ?nombre ": " ?ud " unidades de " ?nomprod ", " (* ?ud ?precio) " euros pagados con " ?pago crlf)
    (printout t ?nombre " acumula un total de " ?aux " euros en la jornada de hoy")
)

(defrule ReponerStock
    ?prod <- (Producto (stock_cafeteria ?stock_c)(stock_almacen ?stock_a)(maximo ?max))
    (test (< ?stock_c 10))
    =>
    (bind ?cantidad (Reposicion ?stock_c ?stock_a ?max))
    (modify ?prod (stock_almacen (- ?stock_a ?cantidad))(stock_cafeteria (+ ?stock_c ?cantidad)))
)

(deffunction Reposicion (?stock_c ?stock_a ?max)
    (if (< (- ?max ?stock_c) ?stock_c) then
        (return (- ?max ?stock_c))
    )else(return (?stock_a))
)

