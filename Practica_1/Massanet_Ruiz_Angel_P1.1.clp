(deffacts inicio
    (ubicacion A Norte D)
    (ubicacion D Norte G)
    (ubicacion B Norte E)
    (ubicacion E Norte H)
    (ubicacion C Norte F)
    (ubicacion F Norte I)
    (ubicacion A oeste B)
    (ubicacion B oeste C)
    (ubicacion D oeste E)
    (ubicacion E oeste F)
    (ubicacion G oeste H)
    (ubicacion H oeste I)
    )

(defrule inicio
    ?f1 <-(situacion ?x ?y)
    (ubicacion ?x ?u ?y)
=>
    (printout t ?x " esta al " ?u " de " ?y crlf)
    (retract ?f1)
);; inicio

(defrule Sur
    (ubicacion ?x Norte ?y)
    =>
    (assert (ubicacion ?y Sur ?x))
)

(defrule este
    (ubicacion ?x oeste ?y)
    =>
    (assert (ubicacion ?y este ?x))
)

(defrule mas_norte
    (ubicacion ?x Norte ?y)(ubicacion ?y Norte ?z)
    =>
    (assert (ubicacion ?x Norte ?z))
)

(defrule mas_oeste
    (ubicacion ?x oeste ?y)(ubicacion ?y oeste ?z)
    =>
    (assert (ubicacion ?x oeste ?z))
)

(defrule mas_este
    (ubicacion ?x este ?y)(ubicacion ?y este ?z)
    =>
    (assert (ubicacion ?x este ?z))
)

(defrule mas_sur
    (ubicacion ?x Sur ?y)(ubicacion ?y Sur ?z)
    =>
    (assert (ubicacion ?x Sur ?z))
)

(defrule noroeste
    (ubicacion ?x Norte ?y)(ubicacion ?y oeste ?z)
    =>
    (assert (ubicacion ?x noroeste ?z))
)

(defrule noreste
    (ubicacion ?x Norte ?y)(ubicacion ?y este ?z)
    =>
    (assert (ubicacion ?x noreste ?z))
)

(defrule suroeste
    (ubicacion ?x noreste ?y)
    =>
    (assert (ubicacion ?y suroeste ?x))
)

(defrule sureste
    (ubicacion ?x noroeste ?y)
    =>
    (assert (ubicacion ?y sureste ?x))
)

(defrule mas_noreste
    (ubicacion ?x noreste ?y)(ubicacion ?y noreste ?z)
    =>
    (assert (ubicacion ?x noreste ?y))
)

(defrule mas_noroeste
    (ubicacion ?x noroeste ?y)(ubicacion ?y noroeste ?z)
    =>
    (assert (ubicacion ?x noroeste ?z))
)

(defrule mas_suroeste
    (ubicacion ?x suroeste ?y)(ubicacion ?y suroeste ?z)
    =>
    (assert (ubicacion ?x suroeste ?z))
)

(defrule mas_sureste
    (ubicacion ?x sureste ?y)(ubicacion ?y sureste ?z)
    =>
    (assert (ubicacion ?x sureste ?z))
)