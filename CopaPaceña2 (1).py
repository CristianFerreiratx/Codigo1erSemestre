import numpy as np
equipos1 = np.array (["San Antonio Bulo Bulo","The Strongest","Real Tomayapo", "Real Santa Cruz"])
puntaje1 = np.array ([0,1,3])
resultadofinal1 = np.array ([])
for equipo1 in equipos1:
    print (equipo1)
    resultadoparcial1 = np.random.choice(puntaje1 ,6)
    print (resultadoparcial1)
    suma = resultadoparcial1.sum()
    print (suma)
    resultadofinal1 = np.append(resultadofinal1,suma)
print (resultadofinal1)
primerlugar1 = equipos1[np.argmax(resultadofinal1)]
segundolugar1 = equipos1[np.argsort(resultadofinal1)[-2]]
print ("Primer lugar del Grupo A: ", primerlugar1)
print ("Segundo lugar del Grupo A: ", segundolugar1)

equipos2 = np.array (["Aurora","Nacional Potosí","Blooming", "Royal Pari"])
puntaje2 = np.array ([0,1,3])
resultadofinal2 = np.array ([])
for equipo2 in equipos2:
    print (equipo2)
    resultadoparcial2 = np.random.choice(puntaje2 ,6)
    print (resultadoparcial2)
    suma = resultadoparcial2.sum()
    print (suma)
    resultadofinal2 = np.append(resultadofinal2,suma)
print (resultadofinal2)
primerlugar2 = equipos2[np.argmax(resultadofinal2)]
segundolugar2 = equipos2[np.argsort(resultadofinal2)[-2]]
print ("Primer lugar del grupo B: ", primerlugar2)
print ("Segundo lugar del grupo B: ",segundolugar2)

equipos3 = np.array (["Universitario de Vinto","Independiente Petrolero","Guabirá", "Always Ready"])
puntaje3 = np.array ([0,1,3])
resultadofinal3 = np.array ([])
for equipo3 in equipos3:
    print (equipo3)
    resultadoparcial3 = np.random.choice(puntaje3 ,6)
    print (resultadoparcial3)
    suma = resultadoparcial3.sum()
    print (suma)
    resultadofinal3 = np.append(resultadofinal3,suma)
print (resultadofinal3)
primerlugar3 = equipos3[np.argmax(resultadofinal3)]
segundolugar3 = equipos3[np.argsort(resultadofinal3)[-2]]
print ("Primer lugar del grupo C: ", primerlugar3)
print ("Segundo lugar del grupo C: ", segundolugar3)

equipos4 = np.array (["Bolivar","GV San José","Oriente Petrolero", "Jorge Wilstermann"])
puntaje4 = np.array ([0,1,3])
resultadofinal4 = np.array ([])
for equipo4 in equipos4:
    print (equipo4)
    resultadoparcial4 = np.random.choice(puntaje4 ,6)
    print (resultadoparcial4)
    suma = resultadoparcial4.sum()
    print (suma)
    resultadofinal4 = np.append(resultadofinal4,suma)
print (resultadofinal4)
primerlugar4 = equipos4[np.argmax(resultadofinal4)]
segundolugar4 = equipos4[np.argsort(resultadofinal4)[-2]]
print ("Primer lugar del grupo D: ", primerlugar4)
print ("Segundo lugar del grupo D:", segundolugar4)

cuartos1 = np.array ([segundolugar4, primerlugar1])
puntajec1 = np.array ([1,2,3,4,5,6,7,8])
resultadofinalc1=np.array([])
for cuarto1 in cuartos1:
    print (cuarto1)
    resultadoparcialc1 = np.random.choice(puntajec1, 2)
    print (resultadoparcialc1)
    suma = resultadoparcialc1.sum()
    print (suma)
    resultadofinalc1 = np.append(resultadofinalc1,suma)
print (resultadofinalc1)
print ("Cuartos: ", segundolugar4," Vs. ", primerlugar1)
ganadorc1 = cuartos1[np.argsort(resultadofinalc1)[-2]]
print ("Ganador: ", ganadorc1)

cuartos2 = np.array ([segundolugar3, primerlugar2])
puntajec2 = np.array ([1,2,3,4,5,6,7,8])
resultadofinalc2=np.array([])
for cuarto2 in cuartos2:
    print (cuarto2)
    resultadoparcialc2 = np.random.choice(puntajec1, 2)
    print (resultadoparcialc2)
    suma = resultadoparcialc2.sum()
    print (suma)
    resultadofinalc2 = np.append(resultadofinalc2,suma)
print (resultadofinalc2)
print ("Cuartos: ", segundolugar3," Vs. ", primerlugar2)
ganadorc2 = cuartos2[np.argsort(resultadofinalc1)[-2]]
print ("Ganador: ",ganadorc2)

cuartos3 = np.array ([segundolugar2, primerlugar3])
puntajec3 = np.array ([1,2,3,4,5,6,7,8])
resultadofinalc3=np.array([])
for cuarto3 in cuartos3:
    print (cuarto3)
    resultadoparcialc3 = np.random.choice(puntajec3, 2)
    print (resultadoparcialc3)
    suma = resultadoparcialc3.sum()
    print (suma)
    resultadofinalc3 = np.append(resultadofinalc3,suma)
print (resultadofinalc3)
ganadorc3 = cuartos3[np.argsort(resultadofinalc3)[-2]]
print ("Ganador: ", ganadorc3)

cuartos4 = np.array ([segundolugar1, primerlugar4])
puntajec4 = np.array ([1,2,3,4,5,6,7,8])
resultadofinalc4=np.array([])
for cuarto4 in cuartos4:
    print (cuarto4)
    resultadoparcialc4 = np.random.choice(puntajec1, 2)
    print (resultadoparcialc4)
    suma = resultadoparcialc4.sum()
    print (suma)
    resultadofinalc4 = np.append(resultadofinalc4,suma)
print (resultadofinalc4)
print ("Cuartos: ", segundolugar1," Vs. ", primerlugar4)
ganadorc4 = cuartos4[np.argsort(resultadofinalc4)[-2]]
print ("Ganador: ",ganadorc4)

semis1 = np.array ([ganadorc1, ganadorc2])
puntajes1 = np.array ([1,2,3,4,5,6,7,8])
resultadofinals1=np.array([])
for semi1 in semis1:
    print (semi1)
    resultadoparcials1 = np.random.choice(puntajec1, 2)
    print (resultadoparcials1)
    suma = resultadoparcials1.sum()
    print (suma)
    resultadofinals1 = np.append(resultadofinals1,suma)
print (resultadofinals1)
print ("Semifinal: ", ganadorc1," Vs. ", ganadorc2)
ganadors1 = semis1[np.argsort(resultadofinalc4)[-2]]
print ("Ganador: ", ganadors1)

semis2 = np.array ([ganadorc3, ganadorc4])
puntajes2 = np.array ([1,2,3,4,5,6,7,8])
resultadofinals2=np.array([])
for semi2 in semis2:
    print (semi2)
    resultadoparcials2 = np.random.choice(puntajec1, 2)
    print (resultadoparcials2)
    suma = resultadoparcials2.sum()
    print (suma)
    resultadofinals2 = np.append(resultadofinals2,suma)
print (resultadofinals2)
print ("Semifinal: ", ganadorc3," Vs. ", ganadorc4)
ganadors2 = semis2[np.argsort(resultadofinalc4)[-2]]
print ("Ganador: ",ganadors2)

final = np.array ([ganadors1, ganadors2])
puntaje = np.array ([1,2,3,4,5,6,7,8])
resultadofinal=np.array([])
for granfinal in final:
    print (granfinal)
    resultadoparcial = np.random.choice(puntajec1, 2)
    print (resultadoparcial)
    suma = resultadoparcial.sum()
    print (suma)
    resultadofinal = np.append(resultadofinal,suma)
print (resultadofinal)
print ("Final: ", ganadors1," Vs. ", ganadors2)
campeon = final[np.argsort(resultadofinalc4)[-2]]
print ("El campeon de la Apertura es: ", campeon)