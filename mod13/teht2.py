#Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen
# ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kentta/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, request

app = Flask(__name__)
@app.route('/kentta/<icao>')
def haekenttä(icao):
    try:

        tilakoodi = 200
        vastaus = {
        }

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)