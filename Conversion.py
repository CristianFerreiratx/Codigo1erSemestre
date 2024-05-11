import math

def decimal_to_binary(decimal):
    q = decimal
    binary_list = []
    while q >= 1:
        a = q % 2
        binary_list.append(a)
        q = q // 2
    binary_list.reverse()
    binary_string = "".join(str(digit) for digit in binary_list)
    return binary_string

def decimal_to_hexadecimal(decimal):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    hex_chars = "0123456789ABCDEF"
    power = len(hexadecimal) - 1
    for digit in hexadecimal:
        decimal += hex_chars.index(digit.upper()) * (16 ** power)
        power -= 1
    return decimal

# Función principal
def convert_number():
    print("Seleccione el sistema de número de entrada:")
    print("1. Binario")
    print("2. Decimal")
    print("3. Hexadecimal")
    from_option = input("Ingrese el número correspondiente a su elección: ")

    if from_option == "1":
        from_system = "binario"
    elif from_option == "2":
        from_system = "decimal"
    elif from_option == "3":
        from_system = "hexadecimal"
    else:
        print("Opción no válida.")
        return

    print("Seleccione el sistema de número de salida:")
    print("1. Binario")
    print("2. Decimal")
    print("3. Hexadecimal")
    to_option = input("Ingrese el número correspondiente a su elección: ")

    if to_option == "1":
        to_system = "binario"
    elif to_option == "2":
        to_system = "decimal"
    elif to_option == "3":
        to_system = "hexadecimal"
    else:
        print("Opción no válida.")
        return

    number = input(f"Ingrese el número en sistema {from_system} que desea convertir: ")

    if from_system == "decimal":
        decimal = int(number)
        if to_system == "binary":
            result = decimal_to_binary(decimal)
        elif to_system == "hexadecimal":
            result = decimal_to_hexadecimal(decimal)
    elif from_system == "binario":
        binary = number
        if to_system == "decimal":
            result = binary_to_decimal(binary)
        elif to_system == "hexadecimal":
            decimal = binary_to_decimal(binary)
            result = decimal_to_hexadecimal(decimal)
    elif from_system == "hexadecimal":
        hexadecimal = number.upper()
        if to_system == "decimal":
            result = hexadecimal_to_decimal(hexadecimal)
        elif to_system == "binary":
            decimal = hexadecimal_to_decimal(hexadecimal)
            result = decimal_to_binary(decimal)

    print(f"El resultado de convertir {number} de {from_system} a {to_system} es: {result}")

# Ejecutar la función principal
convert_number()
2