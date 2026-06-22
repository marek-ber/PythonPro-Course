# Lekcja: Fetch POST + formularze

## 1. Wstęp

Celem lekcji jest nauczenie wysyłania danych z formularza HTML do API. Poznasz metodę `POST` w `fetch`, która służy do przesyłania danych. Nauczysz się budować ciało zapytania (`body`) w formacie JSON. Zobaczysz, jak pobierać dane z formularza i konwertować je do formatu wymaganego przez API. Na końcu wyślesz dane i wyświetlisz odpowiedź serwera.

---

## 2. Zagadnienia

### 2.1 Formularz HTML + pobieranie danych

**Koncepcja:**

Formularz HTML służy do zbierania danych od użytkownika. W JavaScript można odczytać wartości pól i użyć ich w zapytaniu.

**Kod:**

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Formularz</title>
</head>
<body>

    <main>
        <h1>Dodaj użytkownika</h1>

        <form>
            <label>
                Imię:
                <input type="text" name="name">
            </label>

            <label>
                Email:
                <input type="email" name="email">
            </label>

            <button type="submit">Wyślij</button>
        </form>

        <pre></pre>
    </main>

    <script>
        const form = document.querySelector("form");
        const output = document.querySelector("pre");

        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const name = form.querySelector("input[name='name']").value;
            const email = form.querySelector("input[name='email']").value;

            output.textContent = name + " | " + email;
        });
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* `submit` uruchamia się po kliknięciu „Wyślij”.
* `event.preventDefault()` blokuje przeładowanie strony.
* `.value` pobiera dane z inputów.
* Dane można zapisać w zmiennych JS.
* `textContent` pokazuje wynik na stronie.

---

### 2.2 Fetch POST + JSON body

**Koncepcja:**

Metoda POST służy do wysyłania danych do serwera. Dane muszą być zamienione na JSON i wysłane w `body`.

**Kod:**

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Fetch POST</title>
</head>
<body>

    <main>
        <h1>Wysyłanie danych</h1>

        <button>Wyślij test</button>

        <pre></pre>
    </main>

    <script>
        const button = document.querySelector("button");
        const output = document.querySelector("pre");

        button.addEventListener("click", async function () {
            const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    title: "Test",
                    body: "Przykładowa treść",
                    userId: 1
                })
            });

            const data = await response.json();

            output.textContent = JSON.stringify(data, null, 2);
        });
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* `method: "POST"` ustawia typ zapytania.
* `headers` informuje serwer o formacie JSON.
* `JSON.stringify()` zamienia obiekt na tekst JSON.
* `body` zawiera dane wysyłane do API.
* `response.json()` odczytuje odpowiedź serwera.

---

### 2.3 Integracja formularza z POST

**Koncepcja:**

Dane z formularza można bezpośrednio wysłać do API przez `fetch POST`.

**Kod:**

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Form POST API</title>
</head>
<body>

    <main>
        <h1>Dodaj wpis</h1>

        <form>
            <label>
                Tytuł:
                <input type="text" name="title">
            </label>

            <label>
                Treść:
                <input type="text" name="body">
            </label>

            <button type="submit">Dodaj</button>
        </form>

        <pre></pre>
    </main>

    <script>
        const form = document.querySelector("form");
        const output = document.querySelector("pre");

        form.addEventListener("submit", async function (event) {
            event.preventDefault();

            const title = form.querySelector("input[name='title']").value;
            const body = form.querySelector("input[name='body']").value;

            const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    title: title,
                    body: body,
                    userId: 1
                })
            });

            const data = await response.json();

            output.textContent = JSON.stringify(data, null, 2);

            form.reset();
        });
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* `submit` łączy formularz z JavaScript.
* Dane z inputów trafiają do obiektu JSON.
* `fetch` wysyła dane do API.
* `form.reset()` czyści formularz po wysłaniu.
* Odpowiedź API jest wyświetlana w `<pre>`.

---

## 3. Podsumowanie

* `submit` obsługuje wysyłanie formularza
* `preventDefault()` blokuje przeładowanie strony
* `fetch POST` wysyła dane do serwera
* `JSON.stringify()` konwertuje obiekt do JSON
* `headers` definiują typ danych
* `response.json()` odbiera odpowiedź API
* formularz można bezpośrednio łączyć z API

---

## 4. Zadanie praktyczne

Zbuduj aplikację „Notatki API”.

Wymagania:

* Utwórz formularz z polami:

  * tytuł
  * treść
* Po wysłaniu formularza:

  * zatrzymaj przeładowanie strony
  * wyślij dane metodą POST do `https://jsonplaceholder.typicode.com/posts`
* Wyświetl odpowiedź API w czytelnej formie
* Wyczyść formularz po wysłaniu
* Nie wysyłaj pustych pól (walidacja w JS)
