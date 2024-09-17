
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
        heli = 0
        small = 0
        big = 0
        null = 0
        sql = (f"SELECT type FROM airport WHERE iso_country = '{code}'")
        cursor = connection.cursor()
        cursor.execute(sql)
        result_row = cursor.fetchall()
        for i in range(len(cursor.fetchall())):
            print(result_row)
            if result_row[i] == "heliport":
                heli += 1
            elif result_row[i] == "small":
                small += 1
            elif result_row[i] == "big":
                big += 1
            else:
                null += 1
        return heli, small, big, null

user_input = input("Anna maa-koodi: ")
print(fetch_airport_by_iso(user_input))
