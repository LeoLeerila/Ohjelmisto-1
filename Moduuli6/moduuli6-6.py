import math

def hintalaskuri(pizza):
    pintaala = int(pizza[0]) * math.pi
    return int(pizza[1]) / pintaala

pizza1 = input("Syötä ensimmäisen pizzan halkaisija (cm) ja hinta:\n").split(" ")
pizza2 = input("Syötä toisen pizza halkaisija (cm) ja hinta:\n").split(" ")

pizza1 = hintalaskuri(pizza1)
pizza2 = hintalaskuri(pizza2)

print(f"Ensimmäisen pizzan yksikköhinta: {pizza1}\nToisen pizzan yksikkö hinta: {pizza2}")

if pizza1 < pizza2:
    print("Ensimmäinen pizza on halvempi")
elif pizza1 > pizza2:
    print("Toinen pizza on halvempi")
else:
    print("pizzat ovat saman hintaisia")