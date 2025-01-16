luvut = []
while 1:
    luku = input("Syötä luku: ")
    if luku == "":
        break
    luvut.append(int(luku))

luvut = sorted(luvut)
print(f"pienin luku: {luvut[0]}\nsuurin luku: {luvut[-1]}")