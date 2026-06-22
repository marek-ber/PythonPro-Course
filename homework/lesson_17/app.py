from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Lokalna baza SQLite - najprostsza do zadań szkoleniowych.
# Plik bazy utworzy się automatycznie jako lesson_17.db.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lesson_17.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Zadanie 8 - Model produktu w SQLAlchemy
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"


# Zadanie 10a - Model rejestracji
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Registration {self.email}>"


@app.route("/")
def index():
    return render_template("index.html", title="Strona główna")


# Zadanie 1 - Strona "O mnie"
@app.route("/me")
def me():
    return "Marek Berny"


# Zadanie 2 - Prosty kalkulator
@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    suma = num1 + num2
    return f"Wynik to: {suma}"


# Zadania 3, 4, 5 - Lista filmów, dynamiczny tytuł, kolorowanie listy
@app.route("/movies")
def movies():
    favorite_movies = [
        "Władca Pierścieni",
        "Avengers",
        "Wiedźmin",
        "Gladiator",
        "Matrix",
    ]
    return render_template(
        "movies.html",
        movies=favorite_movies,
        page_title="Moje ulubione filmy",
    )


# Zadanie 6 - Słownik w szablonie
@app.route("/book")
def book():
    book_data = {
        "title": "Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
    }
    return render_template("book.html", book=book_data, page_title="Moja książka")


# Zadanie 7 - Prosta galeria
@app.route("/gallery")
def gallery():
    images = [
        {
            "url": "https://picsum.photos/id/1015/500/300",
            "caption": "Góry i jezioro",
        },
        {
            "url": "https://picsum.photos/id/1025/500/300",
            "caption": "Pies",
        },
        {
            "url": "https://picsum.photos/id/1035/500/300",
            "caption": "Wodospad",
        },
    ]
    return render_template("gallery.html", images=images, page_title="Galeria")


# Zadanie 9 - Wyświetlanie produktów
@app.route("/products")
def products():
    all_products = Product.query.all()
    return render_template(
        "products.html",
        products=all_products,
        page_title="Lista produktów",
    )


# Zadanie 10b-d - Formularz rejestracji GET/POST
@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            error = "Uzupełnij imię i email."
        else:
            registration = Registration(name=name, email=email)
            db.session.add(registration)

            try:
                db.session.commit()
                return redirect(url_for("thank_you"))
            except IntegrityError:
                db.session.rollback()
                error = "Ten email jest już zarejestrowany."

    return render_template("register.html", error=error, page_title="Rejestracja")


@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html", page_title="Dziękujemy")


# Pomocnicza ścieżka do jednorazowego utworzenia tabel i przykładowych produktów.
@app.route("/init-db")
def init_db():
    db.create_all()

    if Product.query.count() == 0:
        products_to_add = [
            Product(name="Laptop", price=3499.99),
            Product(name="Klawiatura", price=249.99),
            Product(name="Mysz", price=129.99),
        ]
        db.session.add_all(products_to_add)
        db.session.commit()

    return "Baza danych została utworzona, a przykładowe produkty dodane."


if __name__ == "__main__":
    app.run(debug=True)
