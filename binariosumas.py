def sumaBinaria(binario1, binario2):
    carry = 0
    suma = ''

    # Asegurarse de que los números tienen la misma longitud
    while len(binario1) < len(binario2):
        binario1 = '0' + binario1
    while len(binario2) < len(binario1):
        binario2 = '0' + binario2

    # Sumar dígito a dígito, empezando por el final
    for i in range(len(binario1) - 1, -1, -1):
        bit1 = int(binario1[i])
        bit2 = int(binario2[i])
        
        sumaBits = bit1 + bit2 + carry

        # Si la suma de los bits es 0 o 1, no hay acarreo
        # Si la suma de los bits es 2 o 3, hay acarreo
        if sumaBits == 0 or sumaBits == 1:
            suma = str(sumaBits) + suma
            carry = 0
        elif sumaBits == 2 or sumaBits == 3:
            suma = str(sumaBits - 2) + suma
            carry = 1

    # Si hay un acarreo final, agregarlo al resultado
    if carry == 1:
        suma = '1' + suma

    return suma

# Ejemplo de uso
binario1 = '110010'
binario2 = '110100'
print('Resultado:', sumaBinaria(binario1, binario2))

