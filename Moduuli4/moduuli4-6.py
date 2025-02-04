import random

pisteidenkokonaismaara = int(input("Syötä arvottavien pisteiden määrä:\n"))
pisteetympyransisalla = 0

for x in range(0, pisteidenkokonaismaara):
    if ((random.uniform(-1, 1)**2) + (random.uniform(-1, 1)**2)) < 1:
        pisteetympyransisalla += 1
    #print(f"{x} / {pisteidenkokonaismaara}")

print(f"piin likiarvo on: {(4 * pisteetympyransisalla / pisteidenkokonaismaara)}")