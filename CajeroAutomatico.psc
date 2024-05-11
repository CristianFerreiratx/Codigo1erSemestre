Algoritmo CajeroAutomatico
	definir resp como entero
	DEFINIR PIN Como Entero
	definir menu como entero
	definir depos como real
	definir saldin como real 
	definir transac como real 
	escribir "¿Usted tiene tarjeta?"
	escribir "1. Sí"
	escribir "2. No"
	leer Resp 
	segun resp hacer
		1:
			escribir "Escriba su número de PIN"
			PIN <- ALEATORIO (1000,9999) 
			escribir PIN
			escribir "MENÚ"
			escribir "1. Deposito"
			escribir "2. Retiro"
			escribir "3. Ver Saldo"
			escribir "4. Salir"
			leer menu
			segun menu hacer
				1:
					saldin <- ALEATORIO (0, 100000)
					escribir "Su saldo actual es de: " saldin
					escribir "Escribe el deposito que desea hacer"
					leer depos
					si depos >0 Entonces
						saldof <- saldin+depos 
						escribir "Su saldo final es: " saldof
					SiNo
						escribir "No se puede realizar esta deposito"
					FinSi
				2:
					saldin <- ALEATORIO (0, 100000)
					escribir "Su saldo actual es de: " saldin
					escribir "Escribe el retiro que usted desea hacer"
					leer transac 
					si transac > 0 Entonces
						saldof <- saldin - transac
						escribir "Su saldo final es de: " saldof
					SiNo
						escribir "No se puede este retiro"
					FinSi
				3: 
					saldin <- ALEATORIO (0, 100000)
					escribir "Su saldo actual es de: " saldin
				4:
					escribir "Gracias por usar el cajera, hasta luego"
			FinSegun
		2:
			escribir "Disculpe, usted no puede ingresar"
	FinSegun
	
FinAlgoritmo
