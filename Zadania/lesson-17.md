# **Lekcja 17: Tworzenie pierwszej aplikacji webowej z Flask**

`#lekcja` `#python` `#flask` `#webdev` `#jinja2` `#sql` `#sqlalchemy`

Witaj na kolejnej lekcji! Dzisiaj zrobimy duży krok naprzód i połączymy naszą wiedzę o Pythonie, bazach danych i architekturze klient-serwer, aby stworzyć pierwszą, w pełni funkcjonalną aplikację internetową. Użyjemy do tego celu popularnego i lekkiego frameworka o nazwie **Flask**. Zaczynajmy!

## **1. Czym jest Flask?**

> [!definition]
> 
> Flask to mikroframework do tworzenia aplikacji internetowych w Pythonie. Nazywamy go "mikro", ponieważ nie narzuca on programiście z góry określonej struktury projektu ani nie zawiera wielu wbudowanych narzędzi (jak np. ORM czy system autentykacji). Daje to ogromną elastyczność i pozwala na budowanie aplikacji dokładnie tak, jak tego chcemy, dołączając tylko te biblioteki, których naprawdę potrzebujemy.

Sercem każdej aplikacji we Flasku jest obiekt klasy `Flask`, który zarządza przychodzącymi żądaniami HTTP i kieruje je do odpowiednich funkcji w naszym kodzie.

> [!info]
> 
> Aby rozpocząć pracę z Flask, musimy go najpierw zainstalować. Użyjemy do tego menedżera pakietów pip, który już dobrze znasz.
> 
> ```
> pip install Flask
> ```

Stwórzmy nasz pierwszy, najprostszy program we Flasku. Zapisz poniższy kod w pliku `app.py`:

```python
# Importujemy klasę Flask z biblioteki flask
from flask import Flask

# Tworzymy instancję naszej aplikacji
# __name__ to specjalna zmienna w Pythonie, która przechowuje nazwę bieżącego modułu.
# Flask używa jej, aby wiedzieć, gdzie szukać zasobów, takich jak szablony i pliki statyczne.
app = Flask(__name__)

# Używamy dekoratora @app.route(), aby powiązać adres URL ('/') z funkcją.
# Oznacza to, że gdy ktoś wejdzie na główną stronę naszej aplikacji,
# Flask uruchomi funkcję hello_world().
@app.route('/')
def hello_world():
    # Funkcja zwraca prosty tekst, który zostanie wyświetlony w przeglądarce.
    return 'Hello, World!'

# Ten warunek sprawia, że serwer deweloperski zostanie uruchomiony tylko wtedy,
# gdy skrypt jest wykonywany bezpośrednio (a nie importowany jako moduł).
if __name__ == '__main__':
    # app.run() uruchamia wbudowany serwer deweloperski.
    # debug=True włącza tryb debugowania, który automatycznie restartuje serwer
    # po każdej zmianie w kodzie i wyświetla szczegółowe informacje o błędach.
    app.run(debug=True)
```

Aby uruchomić aplikację, otwórz terminal w folderze z plikiem `app.py` i wpisz: `python app.py`. Następnie wejdź w przeglądarce pod adres `http://127.0.0.1:5000/`. Powinieneś zobaczyć napis "Hello, World!".

```
graph LR
    subgraph "Przeglądarka Użytkownika"
        A["Użytkownik wpisuje adres http://127.0.0.1:5000/"]
    end
    subgraph "Serwer Flask"
        B["Aplikacja Flask"]
        C["Funkcja hello_world()"]
    end
    A -- "Żądanie HTTP GET" --> B
    B -- "Wywołuje funkcję dla ścieżki '/'" --> C
    C -- "Zwraca 'Hello, World!'" --> B
    B -- "Odpowiedź HTTP" --> A
```


![[Screenshot 2025-08-25 at 15.38.04.png]]
## **2. Routing - czyli jak zarządzać adresami URL**

> [!definition]
> 
> Routing (trasowanie, маршрутизация) to mechanizm, który mapuje adresy URL (np. /about, /contact) na konkretne funkcje w naszej aplikacji. Dzięki niemu Flask wie, jaki kod wykonać, gdy użytkownik odwiedza daną podstronę. Za routing odpowiada dekorator @app.route().

Routing pozwala nam tworzyć strukturę naszej aplikacji i rozdzielać zapytania do odpowiednich "endpointów" (punktów końcowych), czyli funkcji, które obsługują te zapytania.

### **Przykład prostego routingu**

Możemy zdefiniować wiele ścieżek, aby stworzyć więcej podstron.

```python
from flask import Flask

app = Flask(__name__)

# Główna strona
@app.route('/')
def index():
    return 'Witaj na stronie głównej!'

# Podstrona "O nas"
@app.route('/about')
def about():
    return 'To jest strona o nas.'

# Podstrona "Kontakt"
@app.route('/contact')
def contact():
    return 'Tutaj znajdziesz nasz kontakt.'

if __name__ == '__main__':
    app.run(debug=True)
    
    
```

```mermaid-code
graph TD
    subgraph "Użytkownik"
        A["Wchodzi na /"]
        B["Wchodzi na /about"]
        C["Wchodzi na /contact"]
    end
    subgraph "Aplikacja Flask"
        D["@app.route('/')"]
        E["@app.route('/about')"]
        F["@app.route('/contact')"]
    end
    A --> D
    D --> G["Funkcja index()"]
    B --> E
    E --> H["Funkcja about()"]
    C --> F
    F --> I["Funkcja contact()"]
````


![[Screenshot 2025-08-25 at 15.39.27.png]]
### **Routing ze zmiennymi**

Często chcemy, aby fragment adresu URL był dynamiczny. Na przykład, aby wyświetlić profil konkretnego użytkownika: `/user/adam` lub `/user/ewa`. Flask pozwala na to w bardzo prosty sposób.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Strona główna. Spróbuj wejść na /user/twoje_imie'

# W nawiasach ostrych < > podajemy nazwę zmiennej.
# Ta nazwa staje się argumentem naszej funkcji.
@app.route('/user/<username>')
def show_user_profile(username):
    # Możemy użyć tej zmiennej wewnątrz funkcji.
    # Używamy f-stringa do wstawienia nazwy użytkownika do odpowiedzi.
    return f'Witaj, {username}!'

# Możemy również określić typ zmiennej, np. <int:post_id>
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Teraz post_id jest liczbą całkowitą, a nie stringiem.
    return f'Wyświetlasz post o ID: {post_id}'

if __name__ == '__main__':
    app.run(debug=True)
```

> [!tip]
> 
> Domyślnie, zmienne w ścieżce są traktowane jako ciągi znaków (stringi). Możemy jednak wymusić konkretny typ, np. int dla liczb całkowitych, float dla liczb zmiennoprzecinkowych, czy path dla ścieżek zawierających ukośniki.

## **3. Szablony Jinja2 - dynamiczne generowanie HTML**

Zwracanie surowego tekstu z funkcji jest proste, ale w prawdziwych aplikacjach chcemy wyświetlać złożone strony HTML. Ręczne tworzenie całego kodu HTML wewnątrz stringów w Pythonie byłoby bardzo niewygodne i nieczytelne.

> [!definition]
> 
> Jinja2 to silnik szablonów dla Pythona. Pozwala tworzyć pliki HTML, w których możemy umieszczać specjalne znaczniki działające jak zmienne, pętle czy instrukcje warunkowe. Flask automatycznie integruje się z Jinja2.

Aby używać szablonów, musimy stworzyć folder o nazwie `templates` w głównym katalogu naszej aplikacji. Flask będzie automatycznie szukał szablonów właśnie tam.

**Struktura projektu:**

```python
/moj_projekt
|-- app.py
|-- /templates
    |-- index.html
    |-- user.html
```

**Plik `app.py`:**

```python
# Musimy zaimportować funkcję render_template
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Tworzymy przykładową listę użytkowników
    users = ['Adam', 'Ewa', 'Karol']
    # render_template szuka pliku index.html w folderze templates
    # i przekazuje do niego zmienną users.
    return render_template('index.html', title='Strona Główna', users=users)

@app.route('/user/<name>')
def user_page(name):
    # Przekazujemy zmienną z URL bezpośrednio do szablonu
    return render_template('user.html', username=name)

if __name__ == '__main__':
    app.run(debug=True)
```

**Plik `templates/index.html`:**

```python
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title> <!-- Zmienna przekazana z Flaska -->
</head>
<body>
    <h1>Witaj na naszej stronie!</h1>
    <h2>Lista użytkowników:</h2>
    <ul>
        <!-- Używamy pętli for, aby iterować po liście users -->
        {% for user in users %}
            <li>{{ user }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Plik `templates/user.html`:**

```python
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Profil użytkownika</title>
</head>
<body>
    <!-- Używamy instrukcji warunkowej if -->
    {% if username == 'Admin' %}
        <h1>Witaj, szefie!</h1>
    {% else %}
        <h1>Profil użytkownika: {{ username }}</h1>
    {% endif %}
</body>
</html>
```

```mermaid-code
graph TD
    A["app.py: funkcja index()"] -- "Przekazuje dane (tytuł, lista)" --> B("render_template")
    B -- "Wczytuje plik" --> C["templates/index.html"]
    B -- "Wypełnia szablon danymi" --> D["Gotowy kod HTML"]
    D -- "Zwraca jako odpowiedź HTTP" --> E["Przeglądarka"]
````


![[Screenshot 2025-11-06 at 17.48.23.png]]



## **4. Bazy danych - praca z PostgreSQL i SQLAlchemy**

Aplikacje internetowe rzadko są statyczne. Zazwyczaj muszą przechowywać dane - użytkowników, posty, produkty itp. Tutaj do gry wchodzą bazy danych.

### **Połączenie z PostgreSQL (surowe zapytania z `psycopg2`)**

Na początku możemy łączyć się z bazą danych i wykonywać surowe zapytania SQL za pomocą biblioteki `psycopg2`.

> [!info]
> 
> Najpierw instalacja:
> 
> ```
> pip install psycopg2-binary
> ```

Poniższy przykład pokazuje, jak połączyć się z bazą i pobrać dane. **Pamiętaj, że w prawdziwej aplikacji dane do połączenia (nazwa użytkownika, hasło) powinny być przechowywane w bezpieczny sposób, np. w zmiennych środowiskowych, a nie na stałe w kodzie!**

```python
import psycopg2
from flask import Flask

app = Flask(__name__)

# Funkcja do nawiązywania połączenia z bazą danych
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="moja_baza",
        user="moj_uzytkownik",
        password="moje_haslo"
    )
    return conn

@app.route('/users')
def list_users():
    conn = get_db_connection()
    # Tworzymy kursor, który pozwala wykonywać polecenia SQL
    cur = conn.cursor()
    # Wykonujemy zapytanie SQL
    cur.execute('SELECT * FROM users;')
    # Pobieramy wszystkie wyniki
    users = cur.fetchall()
    # Zamykamy kursor i połączenie
    cur.close()
    conn.close()
    # Zwracamy wyniki (na razie w prostej formie)
    return str(users)

if __name__ == '__main__':
    app.run(debug=True)
```

Pisanie surowych zapytań SQL ma swoje zalety (pełna kontrola), ale ma też wady: jest podatne na błędy (literówki), trudniejsze w utrzymaniu i przede wszystkim **naraża nas na ataki typu SQL Injection**. Dlatego w większości przypadków używa się ORM.

### **Użycie ORM z SQLAlchemy**

> [!definition]
> 
> SQLAlchemy to potężna biblioteka ORM (Object-Relational Mapping) dla Pythona. Pozwala ona na interakcję z bazą danych za pomocą obiektów Pythona, zamiast pisać surowe zapytania SQL. Klasy w Pythonie mapujemy na tabele w bazie danych, a obiekty tych klas na wiersze w tych tabelach.

Aby ułatwić integrację SQLAlchemy z Flaskiem, użyjemy rozszerzenia `Flask-SQLAlchemy`.

> [!info]
> 
> Instalacja:
> 
> ```
> pip install Flask-SQLAlchemy psycopg2-binary
> ```

Zobaczmy, jak wygląda praca z bazą danych przy użyciu ORM.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfiguracja połączenia z bazą danych
# Format: postgresql://uzytkownik:haslo@host:port/nazwa_bazy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://moj_uzytkownik:moje_haslo@localhost/moja_baza'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Wyłączenie niepotrzebnej funkcji śledzenia

# Inicjalizacja obiektu SQLAlchemy
db = SQLAlchemy(app)

# Definicja modelu (tabeli) za pomocą klasy
# Dziedziczymy po db.Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Metoda __repr__ definiuje, jak obiekt będzie wyglądał po wydrukowaniu
    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def index():
    # Pobieranie wszystkich użytkowników z bazy
    # User.query.all() to odpowiednik "SELECT * FROM user;"
    users = User.query.all()
    return render_template('index.html', users=users)

# Aby stworzyć tabele w bazie danych na podstawie modeli,
# musisz otworzyć terminal Pythona i wykonać:
# from app import db
# db.create_all()
# Zrób to tylko raz!
```

Użycie ORM jest bezpieczniejsze, bardziej czytelne i "pythonowe". Pozwala myśleć w kategoriach obiektów, a nie tabel i zapytań, co znacznie przyspiesza pracę.

## **🧪 Zadania do samodzielnej pracy**

1. ✏️ Zadanie 1 – Strona "O mnie"
    
    Stwórz nową ścieżkę /me w swojej aplikacji. Kiedy użytkownik wejdzie na ten adres, funkcja powinna zwrócić Twoje imię i nazwisko.
    
    (proste)
    
2. ✏️ Zadanie 2 – Prosty kalkulator
    
    Utwórz ścieżkę /add/<int:num1>/<int:num2>. Funkcja przypisana do tej ścieżki powinna przyjąć dwie liczby jako argumenty, zsumować je i zwrócić wynik w formacie "Wynik to: [suma]".
    
    (proste)
    
3. ✏️ Zadanie 3 – Przekaż listę do szablonu
    
    W pliku app.py stwórz listę swoich ulubionych filmów. Następnie stwórz nową ścieżkę /movies i szablon movies.html. Przekaż listę filmów do szablonu i wyświetl ją jako listę nieuporządkowaną (<ul>) w HTML.
    
    (proste)
    
4. ✏️ Zadanie 4 – Dynamiczny tytuł strony
    
    Zmodyfikuj zadanie 3. Oprócz listy filmów, przekaż do szablonu movies.html również zmienną page_title z wartością "Moje ulubione filmy". Użyj tej zmiennej w znaczniku <title> w szablonie.
    
    (proste)
    
5. ✏️ Zadanie 5 – Kolorowanie listy
    
    W szablonie movies.html z zadania 3, użyj pętli for oraz instrukcji if w Jinja2, aby co drugi element listy miał inny kolor tła. Możesz użyć właściwości loop.index w pętli.
    
    (proste)
    
6. 🧠 Zadanie 6 – Słownik w szablonie
    
    Stwórz w app.py słownik opisujący książkę, np. {'title': 'Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937}. Stwórz ścieżkę /book i szablon book.html. Przekaż słownik do szablonu i wyświetl jego zawartość w czytelny sposób, np. używając nagłówków i paragrafów.
    
    (challenge)
    
7. 🧠 Zadanie 7 – Prosta galeria
    
    Stwórz listę słowników, gdzie każdy słownik reprezentuje obrazek i zawiera klucze url (link do obrazka w internecie) i caption (podpis). Stwórz ścieżkę /gallery i szablon gallery.html. Wyświetl wszystkie obrazki wraz z podpisami, używając pętli w Jinja2.
    
    (challenge)
    
8. 🧠 Zadanie 8 – Model produktu w SQLAlchemy
    
    Zdefiniuj model SQLAlchemy o nazwie Product. Powinien on zawierać pola: id (klucz główny, integer), name (string, nie może być pusty) oraz price (float, nie może być pusty). Następnie w interaktywnej konsoli Pythona dodaj kilka przykładowych produktów do bazy danych.
    
    (challenge)
    
9. 🧠 Zadanie 9 – Wyświetlanie produktów
    
    Stwórz ścieżkę /products i szablon products.html. W funkcji pobierz wszystkie produkty z bazy danych (stworzone w zadaniu 8) i przekaż je do szablonu. Wyświetl produkty w tabeli HTML, która będzie miała kolumny "Nazwa" i "Cena".
    
    (challenge)
    
10. 🧠 Zadanie 10 – Aplikacja do rejestracji na wydarzenie
    
    Stwórz kompletną mini-aplikację.
    
    a. Zdefiniuj model SQLAlchemy Registration z polami id, name (string), email (string, unikalny).
    
    b. Stwórz ścieżkę /register, która będzie obsługiwać metody GET i POST (poszukaj w dokumentacji Flaska, jak to zrobić - methods=['GET', 'POST']).
    
    c. Stwórz szablon register.html z formularzem HTML (<form>) zawierającym pola na imię i email oraz przycisk "Zarejestruj". Formularz powinien wysyłać dane metodą POST.
    
    d. W funkcji dla ścieżki /register, sprawdź, czy żądanie jest typu POST. Jeśli tak, pobierz dane z formularza, stwórz nowy obiekt Registration, zapisz go w bazie danych i przekieruj użytkownika na stronę z podziękowaniem. Jeśli żądanie jest typu GET, po prostu wyświetl formularz.
    
    (challenge)