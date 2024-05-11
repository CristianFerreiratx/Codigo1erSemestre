Funcion result <- Operacion (valeatorio,numayor,numenor)
	segun valeatorio Hacer
		1:
			result <- numayor+numenor
			escribir "La maquina quizo hacer suma y el resultado es: " result 
		2:
			result <- numayor-numenor
			escribir "La maquina quizo hacer resta y el resultado es: " result 
		3:
			result <- numayor*numenor
			escribir "La maquina quizo hacer multiplicacion y el resultado es: " result 
		4:
			result <- numayor/numenor
			escribir "La maquina quizo hacer division y el resultado es: " result 
		5:
			result <- numayor^numenor
			escribir "La maquina quizo hacer potencia y el resultado es: " result
	FinSegun
Fin Funcion

Algoritmo CalculadoraKaizenRefactorizado
	definir num1, num2, sum, rest,mult, div, poten1, poten2, rais1,rais2, numayor, numenor, result, ValorOperacion  como real
	definir valeatorio como entero
	escribir "Ingresar dos numeros"
	leer num1, num2
	si num1 > num2 Entonces
		numayor <- num1
		numenor <- num2 
	SiNo
		numayor <- num2
		numenor <- num1 
	FinSi
	valeatorio <- ALEATORIO (1,5)
	ValorOperacion=Operacion(valeatorio,numayor,numenor)
	escribir "El valor total es: " ValorOperacion
FinAlgoritmo
