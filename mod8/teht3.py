# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa
# lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin
# koordinaatteihin. Laske etäisyys geopy-kirjaston avulla

import mysql.connector

import math

connection = mysql.connector.connect(
        host='127.0.0.1', #localhost
        port=3306,
        database='flight_game',
        user='flight_game',
        password='flight_game',
        autocommit=True,
        collation='utf8mb4_general_ci',
        )



def lentokenttä1(code1):
    sql = (f"select latitude_deg, longitude_deg from airport where ident = '{code1}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row1 = cursor.fetchone()
    return result_row1

user_input1 = input("Anna ensimmäinen ICAO-koodi:")
x,y = lentokenttä1(user_input1)


def lentokenttä2(code2):
    sql = (f"select latitude_deg, longitude_deg from airport where ident = '{code2}'")

    cursor = connection.cursor()
    cursor.execute(sql)
    result_row2 = cursor.fetchone()
    return result_row2

user_input2 = input("Anna toinen ICAO-koodi:")

z,k = lentokenttä2(user_input2)
e = math.acos(math.sin(x)*math.sin(z)+math.cos(x)*math.cos(z)*math.cos(k-y))*6371
print(f"Kohteilla on {e:.2f}km etäisyyttä toisistaan.")