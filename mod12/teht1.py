# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle
# on näytettävä pelkkä vitsin teksti.

import requests

def vitsi():
    url = 'https://api.chucknorris.io/jokes/random'

    try:
        response = requests.get(url)
    except:
        print("Verkkovirhe")
        return

    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}")
        return

    response_body = requests.get(url).json()

    if len(response_body) < 1:
        print("Ei tuloksia")
        return

    print(response_body['value'])

vitsi()