import random

def noppa(tahko):
    return random.randint(1, tahko)

tahkojenmaara = int(input("Syötä nopan tahkojen määrä: "))

i = 0
while i != tahkojenmaara:
    i = noppa(tahkojenmaara)
    print(str(i))