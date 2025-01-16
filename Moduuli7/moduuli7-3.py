
def lisaaicao():
    icao = input("syötä ICAO koodi joka lisätään: ")
    if icao == "":
        return
    else:
        lentokentannimi = input(f"lisää lentokentälle {icao} nimi: ")
        return [icao, lentokentannimi]
    

def haeicao():
    icao = input("hae lentokenttän nimi ICAO koodilla: ")
    if icao == "":
        return
    else:
        for i in range(0, len(icaolista)):
            if icaolista[i][0] == icao:
                print(icaolista[i][1])
        return

icaolista = []


while 1:
    kayttajanvalinta = input("asdasdas")
    if kayttajanvalinta == "" or kayttajanvalinta[0] == "L" or kayttajanvalinta[0] == "l":
        break
    elif kayttajanvalinta[0] == "U" or kayttajanvalinta[0] == "u":
        icaolista.append(lisaaicao())
    elif kayttajanvalinta[0] == "H" or kayttajanvalinta[0] == "h":
        haeicao()
    else:
        print("operaatio ei ole mahdollinen")

