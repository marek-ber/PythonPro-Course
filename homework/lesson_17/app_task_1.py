# Zadanie 1 – Strona "O mnie"
# Stwórz nową ścieżkę /me w swojej aplikacji. Kiedy użytkownik wejdzie na ten adres, funkcja
# powinna zwrócić Twoje imię i nazwisko

from flask import Flask

app = Flask(__name__)

@app.get('/me')
def my_profile():
    return "Marek Berny"


if __name__ == "__main__":
    app.run(debug=True)