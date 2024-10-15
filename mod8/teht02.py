
# olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

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


def fetch_airport_by_iso(code):
        sql = (f"SELECT type, count(*) FROM airport WHERE iso_country = '{code}' GROUP BY type")
        cursor = connection.cursor()
        cursor.execute(sql)
        result_row = cursor.fetchall()
        
        return result_row

user_input = input("Anna maa-koodi: ")
ports = (fetch_airport_by_iso(user_input))
for port in ports:
        print(f"Tyyppi: {port[0]}, Määrä: {port[1]}")