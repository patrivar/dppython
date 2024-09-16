# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa
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
        sql = (f"SELECT type FROM airport WHERE iso_country = '{code}'")
        cursor = connection.cursor()
        cursor.execute(sql)
        result_row = cursor.fetchone()
        print(result_row)
        while cursor.fetchone()!=None:
                print(sql)
                heli = 0
                small = 0
                if type == ('heliport',):
                        heli += 1
                        print(f"{heli}")
                elif type == ('small_airport',):
                        small += 1
                        print(f"{small}")
                print(heli)
                result_row = cursor.fetchone()
                print(result_row)
                return heli, small

user_input = input("Anna maa-koodi: ")
heli, small = fetch_airport_by_iso(user_input)

print(f"{heli} helikopterikenttää ja {small} pientä lentokenttää.")