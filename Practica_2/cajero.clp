(defglobal ?*FECHA* = 2023)
(defglobal ?*LIMITE1* = 900)

(deftemplate Usuario
    (slot dni)
    (slot pin)
    (slot dinero)
)

(deftemplate Tarjeta
    (slot pin)
    (slot dni)
    (slot intentos (default 3))
    (slot lim_dinero(default 100))
    (slot expiracion(default 2030))
    (slot validacion (allowed-values Si No)(default No))
)

(deftemplate Cuenta
    (slot dni)
    (slot saldo)
    (slot estado (allowed-values enPantalla dineroEntregado Inicial SuperaLimite SinSaldo))

)

(deffacts inicales
    (Tarjeta (dni 123456)(pin 1212)(lim_dinero 500)(expiracion 2026))
    (Tarjeta (dni 456456)(pin 4545)(lim_dinero 500)(expiracion 2026))
    (Tarjeta (dni 000111)(pin 0011)(intentos 0)(lim_dinero 500)(expiracion 2026))
    (Cuenta (dni 123456)(saldo 5000))
    (Cuenta (dni 456456)(saldo 33))
    (Cuenta (dni 000111)(saldo 30000))
)

(defrule Supera_Intentos
    (declare (salience 1))
    ?t <- (Tarjeta (intentos 0)(dni ?dni))
    (Cuenta (dni ?dni))
    ;(test (eq ?int 0))
    =>
    (retract ?t)
    (printout t "Se han superado el número de intentos" crlf)
    ;(println "...")
)

(defrule Pin_Invalido
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
    ?t <- (Tarjeta (dni ?dni)(pin ?pin)(intentos ?int)(expiracion ?fecha)(validacion No))
    (Cuenta (dni ?dni))
    (test (< ?*FECHA* ?fecha))
    =>
    (modify ?t (validacion Si))
    (printout t "Validacion OK" crlf)
)

(defrule Muestra_Saldo
    (Tarjeta (validacion Si)(dni ?dni))
    ?c <- (Cuenta (dni ?dni)(saldo ?saldo))
    =>
    (modify ?c (estado enPantalla))
    (printout t "Saldo: " ?saldo crlf)
)

(defrule Saldo_NoSuficiente
    (Tarjeta (validacion Si)(dni ?dni))
    (Cuenta (dni ?dni)(saldo 0))
    =>
    (printout t "Sin saldo" crlf)
)

(defrule Comprueba_Limite1

)

(defrule Comprueba_Limite2

)

(defrule Entrega_Dinero

)