import random

kuutioidenmaara = int(input("Syötä arpakuutioiden määrä: "))

for i in range(0, kuutioidenmaara):
    print(str(random.randint(1, 6)))