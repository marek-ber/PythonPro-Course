# Zadanie 3 – Przekaż listę do szablonu
# W pliku app.py stwórz listę swoich ulubionych filmów. Następnie stwórz nową ścieżkę
# /movies i szablon movies.html. Przekaż listę filmów do szablonu i wyświetl ją jako listę
# nieuporządkowaną (
# ) w HTML.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/movies')
def movies():
    film_list = ["Władca Pierścieni", "Avengers", "Wiedźmin"]
    return render_template('movies.html', movies=film_list, page_title="Moje ulubione filmy")

if __name__ == '__main__':
    app.run(debug=True)

    # Zadanie 4 – Dynamiczny tytuł strony
# Zmodyfikuj zadanie 3. Oprócz listy filmów, przekaż do szablonu movies.html również
# zmienną page_title z wartością "Moje ulubione filmy". Użyj tej zmiennej w znaczniku movies.html