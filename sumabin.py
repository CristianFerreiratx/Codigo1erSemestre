Abinario = input("Ingrese el primer número binario: ")
Bbinario = input("Ingrese el segundo número binario: ")

def ConvertirADecimal(nbinario):
    nbinario= nbinario[::-1]
    ndecimal= 0
    for i in range(len(nbinario)):
        if nbinario[i]=="1":
            ndecimal+=2**i
    return ndecimal

def CovertirABinario(ndecimal):
    if ndecimal==0:
        return "0"
    nbinario= ""
    while ndecimal>0:
        resto= ndecimal%2
        nbinario= str(resto)+ nbinario
        ndecimal//= 2
    return nbinario

Adecimal= ConvertirADecimal(Abinario)
Bdecimal= ConvertirADecimal(Bbinario)
sumadecimal= Adecimal + Bdecimal

resultadoBinario = CovertirABinario(sumadecimal)

print("Resultado de la suma binaria:", resultadoBinario)
