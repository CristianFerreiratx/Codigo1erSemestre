import random
print("Fecha:  1")
print(" ")
print("bolivar:  3")
print("palestino:  0")
print("flamengo:  1")
print("millonario:  1")
print (" ")
def resultadoDeFecha(fecha):
    bolivartol=3
    palestinatol=0
    flamengotol=1
    millonariotol=1

    for contador in range(2, fecha+1): 
        print ()
        print("Fecha: ",contador)
        print ()
        bolivarale=random.choice([0,1,3])
        print("Bolívar: ",bolivarale)
        bolivartol += bolivarale

        palestinaale=random.choice([0,1,3])
        print("Palestina: ",palestinaale)
        palestinatol += palestinaale

        flamengoale=random.choice([0,1,3])
        print("Flamengo: ",flamengoale)
        flamengotol += flamengoale

        millonarioale=random.choice([0,1,3])
        print("Millonario: ",millonarioale)
        millonariotol += millonarioale
    print("------Suma de puntos------")
    print("Puntos totales de Bolívar: ",bolivartol)
    print("Puntos totales de Palestina: ",palestinatol)
    print("Puntos totales de Flamengo: ",flamengotol)
    print("Puntos totales de Millonario: ",millonariotol)

    return bolivartol, palestinatol, flamengotol, millonariotol

def puesto(bolivartol, palestinatol, flamengotol, millonariotol):
    if bolivartol > palestinatol and bolivartol > flamengotol and bolivartol > millonariotol:
        print("Bolívar tiene el puesto 1°")
    elif palestinatol > bolivartol and palestinatol > flamengotol and palestinatol > millonariotol:
        print("Palestina tiene el puesto 1°")
    elif flamengotol > bolivartol and flamengotol > palestinatol and flamengotol > millonariotol:
        print("Flamengo tiene el puesto 1°")
    else:
        print("Millonario tiene el puesto 1°")

def puesto2(bolivartol, palestinatol, flamengotol, millonariotol):
    if bolivartol < palestinatol and bolivartol > flamengotol and bolivartol > millonariotol:
        print("Bolívar tiene el puesto 2°")
    elif palestinatol < bolivartol and palestinatol > flamengotol and palestinatol > millonariotol:
        print("Palestina tiene el puesto 2°")
    elif flamengotol < bolivartol and flamengotol > palestinatol and flamengotol > millonariotol:
        print("Flamengo tiene el puesto 2°")
    else:
        print("Millonario tiene el puesto 2°")

totalDePuntos = resultadoDeFecha(6)
print ("------Tabla de posiciones------")
puesto1=puesto(*totalDePuntos)
puesto2=puesto2(*totalDePuntos)

print("Los dos primeros puesto son los que clasifican a la siguiente fase")