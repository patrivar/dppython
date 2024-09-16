import mysql.connector

#connect()-funktio palauttaa tietokantayhteyden, joka sijoitetaan muuttujaan

connection = mysql.connector.connect(
        host='127.0.0.1', #localhost
        port=3306,
        database='flight_game',
        user='flight_game',
        password='flight_game',
        autocommit=True,
        collation='utf8mb4_general_ci',
        )
print(connection)

# luodaan osoitin ja sijoitetaan muuttujaan
cursor = connection.cursor()
# ajetaan SQL-kielinen kysely osoittimen avulla
cursor.execute("SELECT name, iso_Country, continent FROM country") #SQL komennot kirjoitetaan isolla
# fetchone hakee rivi kerrallaan (monikkona)
#result = cursor.fetchone()
#print(result)
# fetchmany palautttaa halutun määrän () rivejä kerrallaan (listana monikkoja)
#result = cursor.fetchmany(3)
#print(result)
# fetchall palauttaa kaikki (loput) rivit listana
rows = cursor.fetchall()
print(rows)

# tulolista käsitellään toistorakenteella

for row in rows:
        print(f"{row[1]}, Maakoodi: {row[2]}, maanosa {row[0]}")
print(f"Tulosrivejä yhteensä: {cursor.rowcount}")