import random

pisteet = []
pisteidenkokonaismaara = int(input("Syötä arvottavien pisteiden määrä:\n"))
pisteetympyransisalla = 0

i = 0
while i < pisteidenkokonaismaara:
    pisteet.append([random.uniform(-1, 1), random.uniform(-1, 1)])
    i += 1

for x in range(0, pisteidenkokonaismaara):
    if ((pisteet[x][0] * pisteet[x][0]) + (pisteet[x][1] * pisteet[x][1])) < 1:
        pisteetympyransisalla += 1
    print(f"{x} / {pisteidenkokonaismaara}")

print(f"piin likiarvo on: {(4 * pisteetympyransisalla / pisteidenkokonaismaara)}")