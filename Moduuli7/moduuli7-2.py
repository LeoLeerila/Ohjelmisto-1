
def tarkistanimi(tarkistettavanimi):
    if tarkistettavanimi in nimilista:
        print("Aiemmin syötetty")
    else:
        print("Uusi nimi")
        nimilista.append(tarkistettavanimi)

nimilista = []

while 1:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    tarkistanimi(nimi)

nimilista.sort()
for i in nimilista:
    print(i)