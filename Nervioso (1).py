import random
import funcion2 as fn
j1 = random.randint (1,10)
j2 = j1+1
j3 = j1+2
j4 = j1+3
print ("El jugador 1 tiene la carta ", j1)
print ("El jugador 2 tiene la carta ", j2)
print ("El jugador 3 tiene la carta ", j3)
print ("El jugador 4 tiene la carta ", j4)
print (fn.bucle(j1,j2,j3,j4))
cj1 = int(input())
cj2 = int(input())
cj3 = int(input())
cj4 = int(input())
print (fn.ganador(cj1, cj2, cj3, cj4))