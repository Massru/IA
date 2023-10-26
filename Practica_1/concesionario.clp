(deftemplate modelo
	(slot modelo)
	(slot precio)
	(slot tamMaletero (allowed-values Pequeno Mediano Grande))
	(slot caballos)
	(slot abs (allowed-values Si No))
	(slot consumo)
)

(deftemplate formulario
	(slot maxPrecio (default 13000))
	(slot tamMaletero (default Grande) (allowed-values Pequeno Mediano Grande))
	(slot minCaballos (default 80))
	(slot abs (default Si) (allowed-values Si No))
	(slot maxConsumo (default 8,0))
)

(deffacts iniciales
	(modelo (modelo 1) (precio 12000) (tamMaletero Pequeno) (caballos 65) (abs No) (consumo 4.7))
	(modelo (modelo 2) (precio 12500) (tamMaletero Pequeno) (caballos 80) (abs Si) (consumo 4.9))
	(modelo (modelo 3) (precio 13000) (tamMaletero Mediano) (caballos 100) (abs Si) (consumo 7.8))
	(modelo (modelo 4) (precio 14000) (tamMaletero Grande) (caballos 125) (abs Si) (consumo 6.0))
	(modelo (modelo 5) (precio 15000) (tamMaletero Pequeno) (caballos 147) (abs Si) (consumo 8.5))
)

(defrule buscamodelo
	(formulario (maxPrecio ?maxPrecio) (tamMaletero ?tamMaletero) (minCaballos ?minCaballos) (abs ?abs) (maxConsumo ?maxConsumo))
	(modelo (modelo ?modelo) (precio ?precio) (tamMaletero ?tamMaletero) (caballos ?caballos) (abs ?abs) (consumo ?consumo))
	(test (<= ?precio ?maxPrecio))
	(test (>= ?caballos ?minCaballos))
	(test (<= ?consumo ?maxConsumo))
	=>
	(printout t "Modelo recomendado: " ?modelo crlf)
)
