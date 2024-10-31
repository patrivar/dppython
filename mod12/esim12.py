import requests

def share_show(search_term):
    # HTTP GET https://www.tvmaze.com/search/shows?q=emmerdale
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    #response = requests.get('https://api.tvmaze.com/search/shows?q=emmerdale')
    # print(response)
    #response_body = response.json()

    # Käsitellään mahdolliset virheet verkkoyhteydessä
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe")
        # print(e)
        return

    # testataan, että http status koodi OK
    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}")
        return

    response_body = requests.get(url).json()

    if len(response_body) < 1:
        print("Ei tuloksia")
        return
    # Näytetään vain ensimmäisen hakutuloksen nimi
    #print(response_body[0]['show']['name'])

    # iteroidaan response_body (http-vastauksen runko) silmukalla
    print("Kaikki Hakutulokset\n---------------")
    for item in response_body:
        print(item['show']['name'])
        print(f"TV-ohjelman tyyppi: {item['show']['type']}")
        for genre in item['show']['genres']:
            print(genre)
        print('---')

share_show(input("Anna TV-hakusana: "))