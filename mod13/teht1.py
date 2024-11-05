# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31
# vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava
# muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, request

app = Flask(__name__)
@app.route('/laske/<numero>')
def is_prime_number(teksti):
    args = request.args


    result = True
    for i in range(2, num):
        if num % i == 0:
            return False
    return result

user_input = int(input("Anna kokeiltava luku joka on suurempi kuin 1: "))
result = is_prime_number(user_input)
if result == True:
    print(f"Luku {user_input} on alkuluku")
else:
    print(f"Luku {user_input} ei ole alkuluku")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)