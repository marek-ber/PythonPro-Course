# Lekcja: Eventy

## 1. Wstęp

Celem tej lekcji jest poznanie podstaw interakcji użytkownika ze stroną internetową. Nauczysz się reagować na kliknięcia przycisków oraz wpisywanie tekstu do pól formularza. Poznasz mechanizm event listenerów, który pozwala uruchamiać kod po wystąpieniu określonego zdarzenia. Dowiesz się także, jak pobierać dane wpisane przez użytkownika i aktualizować zawartość strony. Na końcu zbudujesz prostą listę, do której użytkownik będzie dodawał nowe elementy.

---

## 2. Zagadnienia

### 2.1 Event click

**Koncepcja:**

Event `click` występuje, gdy użytkownik kliknie element strony. Za pomocą event listenera możemy uruchomić dowolny kod w odpowiedzi na kliknięcie.

**Kod:**

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Click Event</title>
</head>
<body>

    <main>
        <h1>Licznik kliknięć</h1>

        <button>Kliknij mnie</button>

        <p>Liczba kliknięć: <span>0</span></p>
    </main>

    <script>
        const button = document.querySelector("button");
        const counter = document.querySelector("span");

        let clicks = 0;

        button.addEventListener("click", function () {
            clicks++;
            counter.textContent = clicks;
        });
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* `querySelector()` pobiera element ze strony.
* `addEventListener("click", ...)` nasłuchuje kliknięcia.
* Po kliknięciu zwiększamy wartość zmiennej `clicks`.
* `textContent` zmienia tekst widoczny na stronie.
* Funkcja wewnątrz `addEventListener()` wykonuje się przy każdym kliknięciu.

---

### 2.2 Event input

**Koncepcja:**

Event `input` uruchamia się podczas wpisywania tekstu do pola formularza. Pozwala reagować natychmiast na każdą zmianę wartości.

**Kod:**

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Input Event</title>
</head>
<body>

    <main>
        <h1>Podgląd tekstu</h1>

        <label>
            Wpisz tekst:
            <input type="text">
        </label>

        <p>Wpisałeś: <span></span></p>
    </main>

    <script>
        const input = document.querySelector("input");
        const output = document.querySelector("span");

        input.addEventListener("input", function () {
            output.textContent = input.value;
        });
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* `input.value` zawiera aktualny tekst wpisany przez użytkownika.
* Event `input` działa przy każdej zmianie pola.
* `textContent` aktualizuje zawartość elementu `<span>`.
* Użytkownik widzi wynik natychmiast podczas pisania.

---

### 2.3 Obiekt event

**Koncepcja:**

Podczas wystąpienia zdarzenia przeglądarka przekazuje informacje o tym zdarzeniu. Są one dostępne w parametrze funkcji obsługującej event.

**Kod:**

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Event Object</title>
</head>
<body>

    <main>
        <h1>Informacja o wpisywanym tekście</h1>

        <input type="text">

        <p></p>
    </main>

    <script>
        const input = document.querySelector("input");
        const paragraph = document.querySelector("p");

        input.addEventListener("input", function (event) {
            paragraph.textContent = event.target.value;
        });
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* Parametr `event` zawiera informacje o zdarzeniu.
* `event.target` wskazuje element, który wywołał zdarzenie.
* `event.target.value` pobiera aktualną wartość pola.
* Dzięki temu nie musimy odwoływać się bezpośrednio do zmiennej `input`.

---

### 2.4 Dodawanie elementów do listy

**Koncepcja:**

JavaScript może tworzyć nowe elementy HTML i dodawać je do strony. Jest to jedna z najczęściej wykorzystywanych technik przy budowie interfejsów użytkownika.

**Kod:**

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Lista zadań</title>
</head>
<body>

    <main>
        <h1>Lista zakupów</h1>

        <label>
            Produkt:
            <input type="text">
        </label>

        <button>Dodaj</button>

        <ul>
        </ul>
    </main>

    <script>
        const input = document.querySelector("input");
        const button = document.querySelector("button");
        const list = document.querySelector("ul");

        button.addEventListener("click", function () {
            const text = input.value;

            if (text === "") {
                return;
            }

            const item = document.createElement("li");

            item.textContent = text;

            list.appendChild(item);

            input.value = "";
        });
    </script>

</body>
</html>
```

**Wyjaśnienie:**

* `createElement("li")` tworzy nowy element listy.
* `textContent` ustawia tekst nowego elementu.
* `appendChild()` dodaje element do listy `<ul>`.
* Instrukcja `if` blokuje dodawanie pustych wpisów.
* `input.value = ""` czyści pole po dodaniu elementu.

---

## 3. Podsumowanie

* Event `click` reaguje na kliknięcie elementu.
* Event `input` reaguje na zmianę wartości pola formularza.
* `addEventListener()` służy do nasłuchiwania zdarzeń.
* Obiekt `event` zawiera informacje o zdarzeniu.
* `createElement()` tworzy nowe elementy HTML.
* `appendChild()` dodaje element do dokumentu.

---

## 4. Zadanie praktyczne

Napisz aplikację „Lista zadań”.

Wymagania:

* Utwórz pole `<input>`.
* Utwórz przycisk „Dodaj zadanie”.
* Utwórz pustą listę `<ul>`.
* Po kliknięciu przycisku dodaj nowy element `<li>` do listy.
* Nie dodawaj pustych elementów.
* Po dodaniu zadania wyczyść pole tekstowe.
* Nad listą wyświetl liczbę wszystkich dodanych zadań.
* Licznik ma aktualizować się po każdym dodaniu elementu.
