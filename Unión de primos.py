def verificarNumeroFor (numero):
    contador = 0

    for num in range(2, numero + 1):
        primo = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break

        if primo:
            contador += 1

    return contador


def VerificarNumeroWhile(numero):
    contador = 0
    num = 2

    while num <= numero:
        primo = True
        i = 2

        while i <= int(num ** 0.5):
            if num % i == 0:
                primo = False
                break
            i += 1

        if primo:
            contador += 1

        num += 1

    return contador


def cantidadPrimos(cantidad):
    num = 2
    primos = []

    while len(primos) < cantidad:
        primo = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break

        if primo:
            primos.append(num)

        num += 1

    return primos_encontrados


numero_ingresado = int(input("Ingrese un número: "))

# Verificar usando bucle for
cantidad_primos_for = verificar_primo_for(numero_ingresado)
print("Cantidad de primos (bucle for):", cantidad_primos_for)

# Verificar usando bucle while
cantidad_primos_while = verificar_primo_while(numero_ingresado)
print("Cantidad de primos (bucle while):", cantidad_primos_while)

# Obtener una cantidad específica de primos
cantidad = int(input("Ingrese la cantidad de números primos que desea obtener: "))
primos = cantidad_primo(cantidad)
print(f"Los primeros {cantidad} números primos son:", primos)