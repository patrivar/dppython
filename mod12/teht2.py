# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä
# vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan
# dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat
# rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat
# Kelvin-asteet muunnettua Celsius-asteiksi.


# laita sivun api key 'API key' tilalle aaltosulkeiden väliin
# 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'

import requests

def saa(kaupunki):
    API_key = ''
    temp_unit = 'metric'

    units = f'http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=5&appid={API_key}'
    response1 = requests.get(units).json()
    lat = response1[0]['lat']
    lon = response1[0]['lon']
    print(f"Latitude: {lat}, Longitude: {lon}")
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}&units={temp_unit}'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe")
        print(e)
        return

    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}")
        return

    response_body = requests.get(url).json()

    if len(response_body) < 1:
        print("Ei tuloksia")
        return

    print(response_body)



saa(input("Kaupunki:"))
