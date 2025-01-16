luvut = []
while 1:
    luku = input("Syötä luku: ")
    if luku == "":
        break
    luvut.append(int(luku))

luvut = sorted(luvut)

for i in range(1, 6):
    print(str(luvut[-i]))
