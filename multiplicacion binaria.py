a=input("Ingrese el primer número binario: ")
b=input("Ingrese el segundo número binario: ")
def multiplicacion(a, b):
    n=len(b)
    p=0
    for j in range(n):
        if b[j]=="1":
            p+=a<<(n-j-1)
    return bin(p)[2:]

resultado=multiplicacion(int(a, 2), b)
print("Resultado de la multiplicación: ", resultado)