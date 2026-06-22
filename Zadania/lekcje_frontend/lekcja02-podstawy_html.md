Lekcja: Jak działa web + podstawy HTML

---

## 1. Wstęp


To fundament pracy z frontendem i późniejszej integracji z backendem (Flask, Django, REST API).
Każda aplikacja webowa działa w modelu: klient (przeglądarka) → serwer → odpowiedź (HTML / JSON).
Na tym poziomie skupiamy się na HTML jako strukturze strony.
W kolejnych etapach ten sam model będzie używany do API i dynamicznych danych.

---

## 2. Zagadnienia

---

### 2.1 Jak działa web (model request–response)

**Koncepcja:**

Przeglądarka wysyła zapytanie do serwera, a serwer zwraca odpowiedź (np. HTML).
To podstawowy mechanizm działania wszystkich stron i API.


Przykładowa odpowiedź serwera:

```html
<!doctype html>
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Hello</h1>
  </body>
</html>
```

**Wyjaśnienie:**
* przegladarka wysyła żądanie html do serwera
* serwer zwraca dokument HTML jako tekst
* przeglądarka interpretuje HTML i renderuje stronę
* ten sam model działa później dla REST API (zamiast HTML → JSON)

---

### 2.2 Struktura dokumentu HTML

**Koncepcja:**

Każda strona HTML ma stałą strukturę: deklarację, sekcję head i body.
To szkielet, na którym buduje się całą stronę.

**Kod:**

```html
<!doctype html>
<html lang="pl">
  <head>
    <meta charset="UTF-8" />
    <title>Moja strona</title>
  </head>
  <body>
    <h1>Witaj</h1>
  </body>
</html>
```

**Wyjaśnienie:**

* `<!doctype html>` informuje przeglądarkę o HTML5
* `<html>` to główny kontener dokumentu
* `<head>` zawiera dane techniczne (tytuł, kodowanie)
* `<body>` zawiera widoczną treść strony

---

### 2.3 Podstawowe tagi, atrybuty, linki i obrazy

**Koncepcja:**

HTML składa się z tagów, które opisują elementy strony.
Tagi mogą mieć atrybuty, które zmieniają ich zachowanie lub wygląd.

**Kod:**

```html
<!doctype html>
<html lang="pl">
  <head>
    <meta charset="UTF-8" />
    <title>Profil</title>
  </head>

  <body>
    <h1>Jan Kowalski</h1>
    <h2>Frontend Developer</h2>

    <p>Uczę się HTML i backendu.</p>

    <span>Miasto:</span> Warszawa

    <p>
      <a href="https://developer.mozilla.org">Dokumentacja HTML</a>
    </p>

    <img
      src="https://via.placeholder.com/150"
      alt="Zdjęcie profilu"
    />
  </body>
</html>
```

**Wyjaśnienie:**

* `<h1>–<h6>` definiują nagłówki (hierarchia ważności)
* `<p>` oznacza akapit tekstu
* `<span>` to element inline (do małych fragmentów tekstu)
* `<a href="">` tworzy link do innej strony
* `<img src="" alt="">` wstawia obraz (alt ważny dla dostępności)
* atrybuty (`href`, `src`, `alt`) dostarczają dodatkowych informacji o tagu

---

## 3. Podsumowanie

* Web działa w modelu request → response
* Przeglądarka interpretuje HTML i renderuje stronę
* HTML ma strukturę: doctype → html → head → body
* Tagi opisują strukturę treści
* Atrybuty rozszerzają działanie tagów
* Linki (`a`) i obrazy (`img`) są podstawą nawigacji i treści

---

## 4. Zadanie praktyczne

Stwórz plik `index.html` z własnym profilem zawierającym:

* nagłówek z imieniem i nazwiskiem (`h1`)
* podtytuł z rolą (`h2`)
* opis w paragrafie (`p`)
* link do dowolnej strony (`a`)
* obraz z internetu (`img`)
* dodatkowy element `span` z miastem

Plik musi się otwierać w przeglądarce i poprawnie renderować całą strukturę.
