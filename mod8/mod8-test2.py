import mysql.connector

#connect()-funktio palauttaa tietokantayhteyden, joka sijoitetaan muuttujaan

connection = mysql.connector.connect(
        host='127.0.0.1', #localhost
        port=3306,
        database='flight_game',
        user='flight_game@localhost',
        password='flight_game',
        autocommit=True,
        collation='utf8mb4_general_ci',
        )

def fetch_airport_by_icao(code):
    sql = (f"SELECT name, municipality "
           f"FROM airport WHERE ident='{code}'")
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    #print(result_row)
    # palauttaa monikon, paitsi jos tyhjä tulosjoukku niin -> None
    return result_row

user_input = input("Anna ICAO-koodi: ")
airport = fetch_airport_by_icao(user_input)     # Käytä koodia ZYTH tai EFHK jos et muista muita

# jos airport-muuttujassa on jotain muuta kuin None/False/0
if airport: # != None:  # Antaa None jos koodia ei ole olemassa
    print(f"Haettu lentokenttä: {airport[0]}, {airport[1]}.")
else:
    print("Lentokenttää ei löydetty annetulla koodilla.")

# EXTRA: Tiedon lisäys
def add_airport(icao,name, municipality):
    sql = (f"INSERT INTO airport (id,ident, name, municipality)"
           f"VALUES (999, '{icao}', {name}, {municipality})")
    cursor = connection.cursor
    cursor.execute(sql)

icao = input("Anna uusi ICAO: ")
name = input("Anna uusi kenntän nimi: ")
municipality = input("Anna uusi paikkakunta: ")
add_airport(icao, name, municipality)
