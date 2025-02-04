import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='leo',
    password='Leerila',
    autocommit=True
)

def etsi(maakoodi):
    sql = f'SELECT type FROM airport WHERE iso_country = "{maakoodi}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def distinct(maakoodi):
    sql = f'SELECT DISTINCT type FROM airport WHERE iso_country = "{maakoodi}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

maakoodi = input("Syötä maakoodi: ")

kentat = sorted(etsi(maakoodi))
distinctkentat = sorted(distinct(maakoodi))

kenttienmaara = [0]

for i in range(0, len(distinctkentat)):
    for kentta in kentat:
        if kentta == distinctkentat[i]:
            if len(kenttienmaara) - 1 < i:
                kenttienmaara.append(0)
            kenttienmaara[i] += 1

for i in range(0, len(distinctkentat)):
    print(f"{distinctkentat[i]} {kenttienmaara[i]}")

