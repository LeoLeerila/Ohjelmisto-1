
vuodenajat = ["kevät", "kesä", "syksy", "talvi"]

kayttajanvalinta = int(input("Syötä kuukauden numero: "))

if kayttajanvalinta in range(3, 6):
    print(str(vuodenajat[0]))
elif kayttajanvalinta in range(6, 9):
    print(str(vuodenajat[1]))
elif kayttajanvalinta in range(9, 12):
    print(str(vuodenajat[2]))
elif kayttajanvalinta in range(1, 3) or kayttajanvalinta == 12:
    print(str(vuodenajat[3]))
else:
    print("ei kuukausi")