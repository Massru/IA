(defglobal ?*FECHA* = 2023)
(defglobal ?*LIMITE1* = 900)

(deftemplate Usuario
    (slot dni)
    (slot pin)
    (slot dinero (default 0))
)

(deftemplate Tarjeta
    (slot pin)
    (slot dni)
    (slot intentos (default 3))
    (slot limite(default 100))
    (slot anno(default 2030))
    (slot validacion (allowed-values Si No)(default No))
)

(deftemplate Cuenta
    (slot dni)
    (slot saldo)
    (slot estado (allowed-values enPantalla dineroEntregado Inicial SuperaLimite SinSaldo)(default Inicial))

)

(deffacts inicales
    (Tarjeta (dni 123456)(pin 1212)(limite 500)(anno 2026))
    (Tarjeta (dni 456456)(pin 4545)(limite 500)(anno 2026))
    (Tarjeta (dni 000111)(pin 0011)(intentos 0)(limite 500)(anno 2026))
    (Cuenta (dni 123456)(saldo 5000))
    (Cuenta (dni 456456)(saldo 33))
    (Cuenta (dni 000111)(saldo 30000))
)

(defrule Supera_Intentos
    (declare (salience 2))
    ?t <- (Tarjeta (intentos 0)(dni ?dni))
    (Cuenta (dni ?dni))
    ;(test (eq ?int 0))
    =>
    (retract ?t)
    (printout t "Se han superado el número de intentos" crlf)
    ;(println "...")
)

(defrule Pin_Invalido
    (declare (salience 1))
    ?u <- (Usuario (dni ?dni)(pin ?pin))
    ?t <- (Tarjeta (dni ?dni)(pin ?pin2)(intentos ?int))
    (Cuenta (dni ?dni))
    (test (neq ?pin ?pin2))
    =>
    (modify ?t (intentos (- ?int 1)))
    (printout t "Pin Inválido" crlf)
    (retract ?u)
)

(defrule Valida_Tarjeta
    ?u <- (Usuario (dni ?dni)(pin ?pin))
    ?t <- (Tarjeta (dni ?dni)(pin ?pin)(intentos ?int)(anno ?fecha)(validacion No))
    (Cuenta (dni ?dni))
    (test (< ?*FECHA* ?fecha))
    =>
    (modify ?t (validacion Si))
    (printout t "Validacion OK" crlf)
)

(defrule Muestra_Saldo
    (Usuario (dni ?dni))
    (Tarjeta (validacion Si)(dni ?dni))
    ?c <- (Cuenta (dni ?dni)(saldo ?saldo))
    =>
    (modify ?c (estado enPantalla))
    (printout t "Saldo: " ?saldo crlf)
)

(defrule Saldo_NoSuficiente
    ?u <- (Usuario (dni ?dni)(dinero ?dinero))
    (Tarjeta (validacion Si)(dni ?dni))
    (Cuenta (dni ?dni)(saldo ?saldo))
    (test (> ?dinero ?saldo))
    =>
    (printout t "Saldo Insuficiente" crlf)
    (retract ?u)
)

(defrule Comprueba_Limite1
    ?u <- (Usuario (dni ?dni)(dinero ?dinero))
    (Tarjeta (validacion Si)(dni ?dni))
    (test (< ?*LIMITE1* ?dinero))
    =>
    (printout t "El dinero supera el límite del banco" crlf)
    (retract ?u)
)

(defrule Comprueba_Limite2
    ?u <- (Usuario (dni ?dni)(dinero ?dinero))
    (Cuenta (saldo ?saldo)(dni ?dni))
    (Tarjeta (limite ?limite)(dni ?dni)(validacion Si))
    (test (< ?limite ?dinero))
    =>
    (printout t "El dinero supera el límite de la tarjeta" crlf)
    (retract ?u)
)

(defrule Entrega_Dinero
    (declare (salience -1))
    (Usuario (dni ?dni)(dinero ?dinero))
    ?c <- (Cuenta (dni ?dni)(saldo ?saldo))
    (Tarjeta (validacion Si))
    =>
    quitarDinero (?saldo ?dinero)
    (modify ?c (estado dineroEntregado)(saldo (diferencia ?saldo ?dinero)))
)

(deffunction decremento (?a)
    (- ?a 1)
)

(deffunction diferencia (?a ?b)
    (- ?a ?b)
)