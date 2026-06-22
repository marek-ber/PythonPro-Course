# Lekcja: Fetch API (podstawy)

## 1. Wstęp

Celem tej lekcji jest wprowadzenie do pobierania danych z internetu w JavaScript. Nauczysz się używać `fetch` do wykonywania zapytań HTTP typu GET. Zobaczysz, jak przetwarzać odpowiedź w formacie JSON. Poznasz dwie metody obsługi asynchroniczności: `.then()` oraz `async/await`. Na końcu pobierzesz dane z publicznego API i wyświetlisz je na stronie.

---

## 2. Zagadnienia

### 2.1 Fetch GET

**Koncepcja:**

`fetch` służy do wysyłania zapytań HTTP. Najprostszy przypadek to GET, czyli pobieranie danych z API.

**Kod:**

```html id="f1k2p9"
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Fetch GET</title>
</head>
<body>

    <main>
        <h1>Losowy użytkownik</h1>
        <button>Pobierz dane</button>
        <pre></pre>
    </main>

    <script>
        const button = document.querySelector("button");
        const output = document.querySelector("pre");

        button.addEventListener("click", function () {
            fetch("https://jsonplaceholder.typicode.com/users/1")
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    output.textContent = JSON.stringify(data, null, 2);
                });
        });
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* `fetch(url)` wysyła zapytanie GET do API.
* `response.json()` konwertuje odpowiedź do obiektu JavaScript.
* Drugi `.then()` odbiera już gotowe dane.
* `JSON.stringify()` zamienia obiekt na czytelny tekst.
* `pre` zachowuje formatowanie JSON.

---

### 2.2 async / await

**Koncepcja:**

`async/await` to alternatywny sposób obsługi operacji asynchronicznych. Upraszcza kod i eliminuje łańcuch `.then()`.

**Kod:**

```html id="q8l3mn"
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Fetch async/await</title>
</head>
<body>

    <main>
        <h1>Losowy użytkownik (async)</h1>
        <button>Pobierz dane</button>
        <pre></pre>
    </main>

    <script>
        const button = document.querySelector("button");
        const output = document.querySelector("pre");

        async function getUser() {
            const response = await fetch("https://jsonplaceholder.typicode.com/users/2");
            const data = await response.json();

            output.textContent = JSON.stringify(data, null, 2);
        }

        button.addEventListener("click", getUser);
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* `async function` pozwala używać `await`.
* `await fetch()` czeka na odpowiedź serwera.
* `await response.json()` konwertuje dane.
* Kod wygląda liniowo, mimo że działa asynchronicznie.

---

### 2.3 JSON parsing

**Koncepcja:**

Dane z API często są w formacie JSON. Trzeba je zamienić na obiekty JavaScript.

**Kod:**

```html id="v2x9qp"
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>JSON parsing</title>
</head>
<body>

    <main>
        <h1>Dane użytkownika</h1>
        <button>Pobierz</button>
        <p></p>
    </main>

    <script>
        const button = document.querySelector("button");
        const output = document.querySelector("p");

        button.addEventListener("click", async function () {
            const response = await fetch("https://jsonplaceholder.typicode.com/users/3");
            const data = await response.json();

            output.textContent = data.name + " — " + data.email;
        });
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* API zwraca JSON, nie obiekt JS.
* `response.json()` wykonuje parsowanie.
* `data.name` i `data.email` to już zwykłe właściwości obiektu.
* Wynik można bezpośrednio użyć w DOM.

---

## 3. Podsumowanie

* `fetch()` służy do pobierania danych z API
* domyślnie wykonuje request GET
* `response.json()` zamienia JSON na obiekt JS
* `.then()` obsługuje wynik asynchroniczny
* `async/await` upraszcza kod asynchroniczny
* dane z API można bezpośrednio wyświetlać w DOM

---

## 4. Zadanie praktyczne

Zbuduj aplikację „Użytkownik z API”.

Wymagania:

* Utwórz przycisk „Pobierz użytkownika”
* Pobierz dane z endpointu:
  `https://jsonplaceholder.typicode.com/users/1`
* Wyświetl:

  * imię i nazwisko
  * email
  * miasto (address.city)
* Użyj `async/await`
* Dane mają pojawiać się po kliknięciu przycisku
* Nie wyświetlaj surowego JSON-a
