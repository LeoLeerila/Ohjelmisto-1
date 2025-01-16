kayttaja = "python"
salasana = "rules"
yritykset = 5

while 1:
    if yritykset == 0:
        print("Pääsy evätty")
        break
    
    inputkayttaja = input("Syötä käyttäjätunnus: ")
    inputsalasana = input("Syötä salasana: ")

    if kayttaja == inputkayttaja and salasana == inputsalasana:
        print("Tervetuloa")
        break
    else:
        print("Käyttäjätunnus tai salasana väärin")
        yritykset -= 1