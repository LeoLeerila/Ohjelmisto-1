import random

kuutioidenmaara = int(input("Syötä arpakuutioiden määrä: "))
summa = 0

for i in range(0, kuutioidenmaara):
    summa += random.randint(1, 6)

print(str(summa))