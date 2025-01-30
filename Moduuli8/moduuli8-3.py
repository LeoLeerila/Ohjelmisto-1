import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='leo',
    password='Leerila',
    autocommit=True
)

def etsi(ICAO):
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{ICAO}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

koordinaatit1 = etsi(input("Syötä ensimmäisen lentokentän ICAO koodi: "))[0]
koordinaatit2 = etsi(input("Syötä toisen lentokentän ICAO koodi: "))[0]

print(f"{(distance.distance(koordinaatit1, koordinaatit2).km)} km")
