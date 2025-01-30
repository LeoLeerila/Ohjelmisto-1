import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='leo',
    password='Leerila',
    autocommit=True
)

def etsi(ICAO):
    sql = f'SELECT name, municipality FROM airport WHERE ident = "{ICAO}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

kayttajanICAO = input("Syötä lentokentän ICAO koodi: ")

print(etsi(kayttajanICAO)[0])

