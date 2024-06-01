primera_cadena=str(input("Ingrese un texto: "))
segunda_cadena=str(input("Ingrese otro texto: "))
def contador_cadenas(primera_cadena,segunda_cadena):
    contador=0
    contador_pcadena=0
    contador_scadena=0
    contador_2cadenas=0
    for i in range (1,101):
        if i%3==0 and i%5==0:
            print(primera_cadena + segunda_cadena)
            contador_2cadenas=contador_2cadenas+1
        elif i%5==0:
            print(segunda_cadena)
            contador_scadena=contador_scadena+1
        elif i%3==0:
            print(primera_cadena)
            contador_pcadena=contador_pcadena+1
        else:
            print(i)
            contador=contador+1
    return contador,contador_pcadena,contador_scadena,contador_2cadenas
funcion=contador_cadenas(primera_cadena,segunda_cadena)
contador, contador_pcadena, contador_scadena, contador_2cadenas=funcion
print("El numero de veces que se imprimió el numero es",contador)

primera_cadena=str(input("Ingrese un texto: "))
segunda_cadena=str(input("Ingrese otro texto: "))
def vectores_cadenas(primera_cadena,segunda_cadena):
    vector1=list(primera_cadena)
    vector2=list(segunda_cadena)
    return vector1,vector2
vector1, vector2 = vectores_cadenas(primera_cadena, segunda_cadena)
vector1.reverse()
vector2.reverse()

vector_completo=vector1+vector2

for i, contador in enumerate([contador_pcadena, contador_scadena, contador_2cadenas], start=1):
    if contador > 0:
        letra=vector_completo[(contador - 1) % len(vector_completo)]
        if i==1:
            cadena=primera_cadena
        elif i==2:
            cadena=segunda_cadena
        else:
            cadena=primera_cadena + segunda_cadena
        print(f"Según la primera función, el número de veces es {contador} y en el vector se muestra la letra '{letra}' de la cadena '{cadena}'")


