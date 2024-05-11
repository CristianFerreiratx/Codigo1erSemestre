Proceso BoletaDePago
	Definir Bono_Alimentario, Haber, Transporte, Vales,Salario_dom, Total_ingr, Afp, Total_egre, liquid_paga , dias_d, bonoAnt, SMNB, AñoIn, AñoAct, AñosAnt,aps ,apsuno, apsdo2, aps3 Como real
	Definir Nombre, Carnet, TipoEmpresa, Cargo Como Caracter
	Escribir "Ingrese su nombre"
	Leer Nombre
	Escribir "Ingrese su carnet de identidad"
	Leer Carnet
	Escribir "Ingrese de que tipo es la empresa en la que trabaja"
	Leer TipoEmpresa
	Escribir "Ingrese su cargo actual"
	Leer Cargo
    Escribir "Ingrese su Año de ingreso"
	Leer AñoIn
	Escribir "Ingrese el año actual"
	Leer AñoAct
	Escribir "Ingrese su haber"
	Leer Haber
	Escribir "Ingrese Bono Alimentario"
	Leer Bono_Alimentario
	Escribir "Ingresar Bono de Transporte"
	Leer Transporte
	Escribir "Ingrese sus Vales"
	Leer Vales
	Escribir "Ingrese sus dias Domingos trabajados"
	Leer dias_d
	Total_ingr= Haber+Bono_Alimentario+Transporte+Vales+Salario_dom+bonoAnt
    Si Total_ingr > 13000 Entonces
			apsuno= ( Total_ingr -13000) *0.01
		SiNo
			Si Total_ingr > 25000 Entonces
				apsdo2= ( Total_ingr-25000) *0.05
			SiNo
				Si Total_ingr > 35000 Entonces
					aps3= ( Total_ingr-35000) *0.1
				Fin Si
			Fin Si
		Fin Si
	Salario_dom= (dias_d*haber/30) *2
	Si dias_d=0 Entonces
		Salario_dom=0
	Sino Salario_dom= (dias_d*haber/30) *2
	FinSi
	Afp= Total_ingr*12.71/100
	Total_egre= Afp
	SMNB= 2.362
	liquid_paga= Total_ingr-Total_egre
	AñoAnt=AñoAct-AñoIn
	Si AñoAnt>0 y AñoAnt<=2 Entonces
		bonoAnt=0
	SiNo
		Si AñoAnt>2 y AñoAnt<=5 Entonces
			bonoAnt=3*SMNB*0.05
		SiNo
			Si AñoAnt>5 y AñoAnt<=8 Entonces
				bonoAnt=3*SMNB*0.11
			SiNo
				Si  AñoAnt>8 y AñoAnt<=11 Entonces
					bonoAnt=3*SMNB*0.18
				SiNo
					Si AñoAnt>11 y AñoAnt<=15 Entonces
						bonoAnt=3*SMNB*0.26
					SiNo
						Si AñoAnt>15 y AñoAnt<=20 Entonces
							bonoAnt=3*SMNB*0.34
						SiNo
							Si AñoAnt>20 y AñoAnt<=25 Entonces
								bonoAnt=3*SMNB*0.42
							SiNo
								Si AñoAnt>25 Entonces
									bonoAnt=3*SMNB*0.5
								Fin Si
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	
	
	Escribir "___________BOLETA DE PAGO___________"
	
	Escribir "Nomnbre: " Nombre
	Escribir "Ci: " Carnet
	Escribir "Tipo de Empresa: " TipoEmpresa
	Escribir "Cargo: " Cargo
	Escribir "Años de Antiguedad: " AñoAnt
	Escribir "Haber basico: " Haber " Bs"
	Escribir "Bono Antiguedad: " bonoAnt " Bs"
	Escribir "Bonos Total: " Bono_Alimentario+Transporte+bonoAnt " Bs"
	Escribir "Vales: " Vales " Bs"
	Escribir "Salario Dominical: " Salario_dom " Bs"
	Escribir "Total Ingresos: " Total_ingr " Bs"
	Escribir "Aporte solidario nacional: " apsuno+apsdo2+aps3 " Bs"
	Escribir "AFP: " Afp " Bs"
	Escribir "Total egresos: " Total_egre " Bs"
	Escribir "Total liquido pagable: " liquid_paga " Bs"
	
FinProceso