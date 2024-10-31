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
