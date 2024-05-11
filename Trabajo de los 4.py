#ANTONIO
def VerificarNumeroFor(numero):
    contador = 0

    for num in range(2, numero + 1):
        primo = 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = 0
                break

        if primo:
            contador = contador + 1

    return contador


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
#ANDRES
def detPrimo(numero):
    if numero < 2:
        return "no es un número primo"
    for i in range(2, numero):
        if numero % i == 0:
            return "no es un número primo"
    return "si es un número primo"

numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
    resultado = detPrimo(i)
    if resultado == "si es un número primo":
        print(i, "Es un número primo")
    else:
        print(i, "no es un número primo")
#CRISTIAN
numero=int(input("Ingrese un numero: "))
def deterPrim(numero):
    if numero<2:
        return "no esun numero primo"
    for i in range (2,numero):
        if (numero % i==0):
            return "no es un numero primo"
    return "si es un numero primo"

resultadoDet=deterPrim(numero)
for i in range (1,numero+1,1):
    return print (resultadoDet)
#ROSALIA
def detPrimo(numero):
    if numero < 2:
        return False
    i = 2
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 1
    return True

numero = int(input("Ingrese un número: "))

if detPrimo(numero):
    print(numero, "Es un número primo")
else:
    print(numero, "no es un número primo")