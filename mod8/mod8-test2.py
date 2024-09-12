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
    print(result_row)
    return result_row

fetch_airport_by_icao("ZYTH")