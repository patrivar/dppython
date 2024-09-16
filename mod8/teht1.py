# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia
# vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

connection = mysql.connector.connect(
        host='127.0.0.1', #localhost
        port=3306,
        database='flight_game',
        user='flight_game',
        password='flight_game',
        autocommit=True,
        collation='utf8mb4_general_ci',
        )

def fetch_airport_by_icao(code):
    sql = (f"SELECT name, municipality "
           f"FROM airport WHERE ident='{code}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    return result_row

user_input = input("Anna ICAO-koodi: ")
airport = fetch_airport_by_icao(user_input)

if airport:
    print(f"Haettu lentokenttä: {airport[0]}, {airport[1]}.")
else:
    print("Lentokenttää ei löydetty annetulla koodilla.")