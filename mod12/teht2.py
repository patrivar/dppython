# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä
# vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan
# dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat
# rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat
# Kelvin-asteet muunnettua Celsius-asteiksi.

import json
import requests

def saa(kaupunki):
    # Laita api avaimesi merkkien väliin
    API_key = ''
    temp_unit = 'metric'

    units = f'http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=5&appid={API_key}'
    response1 = requests.get(units).json()
    lat = response1[0]['lat']
    lon = response1[0]['lon']
    print(f"Latitude: {lat}, Longitude: {lon}")
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}&units={temp_unit}&lang=FI'

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

    print(json.dumbs(response_body, indent=2))
    lämpötila = response_body['main']['temp']
    kuvaus = response_body['weather'][0]['description']

    print(f'Lämpötila kohteessa on {lämpötila} astetta ja sää on {kuvaus}.')


saa(input("Kaupunki:"))
