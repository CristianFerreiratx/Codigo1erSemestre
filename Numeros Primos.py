def detPrimo(numero):
    if numero < 2:
        return "no es un número primo"
    for i in range(2, numero):
        if numero % i == 0:
            return "no es un número primo"
    return "si es un número primo"



def VerificarNumeroWhile(numero):
    contador = 0
    num = 2

    while num <= numero:
        primo = 1
        i = 2

        while i <= int(num ** 0.5):
            if num % i == 0:
                primo = 0
                break
            i = i + 1

        if primo:
            contador = contador + 1

        num = num + 1

    return contador


def imprimirPrim(cantidad):
    contador = 0
    num = 2

    while contador < cantidad:
        primo = 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = 0
                break

        if primo:
            print(num)
            contador = contador + 1

        num = num + 1


numIngresado = int(input("Ingrese un número: "))


Primosfor = VerificarNumeroFor(numIngresado)
print("Cantidad de primos (bucle for):", Primosfor)


Primoswhile = VerificarNumeroWhile(numIngresado)
print("Cantidad de primos (bucle while):", Primoswhile)


cantidad = int(input("Ingrese la cantidad de números primos que desea imprimir: "))
imprimirPrim(cantidad)