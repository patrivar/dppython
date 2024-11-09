# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31
# vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava
# muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, jsonify

app = Flask(__name__)

def laske(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:luku>', methods=['GET'])
def alkuluku(luku):
    tulos = laske(luku)
    vastaus = {
        "Number": luku,
        "isPrime": tulos
    }
    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)