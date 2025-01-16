import random

def karsinta(numerot):
    karsinnat = []
    for numero in numerot:
        if numero%2 == 0:
            karsinnat.append(numero)
    return karsinnat

numerolista = []
i = 0
while i < 10:
    numerolista.append(random.randint(1, 10))
    i += 1

parilliset = karsinta(numerolista)
print(f"alkuperäinen lista\n{numerolista}\nkarsittu lista\n{parilliset}")