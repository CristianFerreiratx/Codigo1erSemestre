import random
huevos=["Dr Rua", "Pepito", "Papa", "Yacyree", "Filipino", "Tony"]
contraseñarandom=[]
for lista in huevos:
    listaletras = list(lista)
    contraseñarandom.append(random.choice(listaletras))
    
contraseñarandom = ''.join(contraseñarandom)

print(contraseñarandom)