
def tarkistanimi(tarkistettavanimi):
    if tarkistettavanimi in nimilista:
        print("Aiemmin syötetty")
    else:
        print("Uusi nimi")
        nimilista.add(tarkistettavanimi)

nimilista = set()

while 1:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    tarkistanimi(nimi)

for i in nimilista:
    print(i)