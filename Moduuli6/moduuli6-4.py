import random

def summa(numerot):
    kaikki = 0
    for numero in numerot:
        kaikki += numero
    return kaikki

numerolista = []
i = 0
while i < 10:
    numerolista.append(random.randint(1, 10))
    i += 1

valmis = summa(numerolista)
print(str(valmis))