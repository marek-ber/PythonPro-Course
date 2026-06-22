# Lekcja: DOM — querySelector, textContent, innerHTML i manipulacja elementami

## 1. Wstęp

Celem tej lekcji jest poznanie podstaw pracy z DOM (Document Object Model), czyli sposobu, w jaki JavaScript uzyskuje dostęp do elementów HTML i je modyfikuje. Nauczysz się wyszukiwać elementy za pomocą `querySelector()`, zmieniać ich zawartość przez `textContent` i `innerHTML`, a także tworzyć nowe elementy i dodawać je do strony. Wszystkie przykłady będą działały w zwykłej przeglądarce bez dodatkowych bibliotek. Na końcu wykorzystasz poznane techniki do stworzenia dynamicznej listy.

---

## 2. Zagadnienia

### 2.1 Wyszukiwanie elementów za pomocą querySelector

#### Koncepcja:

JavaScript musi najpierw znaleźć element HTML, zanim będzie mógł go zmienić. Do tego służy metoda `querySelector()`. Zwraca ona pierwszy element pasujący do podanego selektora CSS.

#### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>querySelector</title>
</head>
<body>

    <h1>Nagłówek strony</h1>

    <script>
        const naglowek = document.querySelector("h1");

        console.log(naglowek);
    </script>

</body>
</html>
```

#### Wyjaśnienie:

* `document` reprezentuje całą stronę HTML.
* `querySelector("h1")` wyszukuje pierwszy element `<h1>`.
* Znaleziony element zostaje zapisany w zmiennej `naglowek`.

---

### 2.2 Zmiana tekstu za pomocą textContent

#### Koncepcja:

Właściwość `textContent` pozwala odczytać lub zmienić tekst znajdujący się wewnątrz elementu. Traktuje zawartość wyłącznie jako tekst.

#### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>textContent</title>
</head>
<body>

    <h1>Stary tytuł</h1>

    <script>
        const naglowek = document.querySelector("h1");

        naglowek.textContent = "Nowy tytuł";
    </script>

</body>
</html>
```

#### Wyjaśnienie:

* `querySelector()` znajduje element `<h1>`.
* `textContent` ustawia nową zawartość tekstową.
* Po załadowaniu strony użytkownik zobaczy „Nowy tytuł”.

---

### 2.3 Wstawianie HTML za pomocą innerHTML

#### Koncepcja:

`innerHTML` pozwala wstawiać kod HTML do wnętrza elementu. W przeciwieństwie do `textContent` przeglądarka interpretuje znaczniki HTML.

#### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>innerHTML</title>
</head>
<body>

    <main>
        <p>Stara zawartość</p>
    </main>

    <script>
        const main = document.querySelector("main");

        main.innerHTML = `
            <h1>Nowy nagłówek</h1>
            <p>Nowy akapit</p>
        `;
    </script>

</body>
</html>
```

#### Wyjaśnienie:

* Pobieramy element `<main>`.
* `innerHTML` usuwa poprzednią zawartość elementu.
* Wstawiony tekst jest interpretowany jako HTML.

#### Drugi przykład

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Porównanie</title>
</head>
<body>

    <main></main>

    <script>
        const main = document.querySelector("main");

        main.textContent = "<h1>Test</h1>";
    </script>

</body>
</html>
```

#### Wyjaśnienie:

* `textContent` nie interpretuje znaczników HTML.
* Na stronie pojawi się dosłownie tekst `<h1>Test</h1>`.
* Jest to główna różnica między `textContent` i `innerHTML`.

---

### 2.4 Zmiana atrybutów elementu

#### Koncepcja:

JavaScript może zmieniać atrybuty elementów, np. adres obrazka lub linku. Dzięki temu wygląd strony może reagować na działania użytkownika.

#### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Atrybuty</title>
</head>
<body>

    <img src="https://via.placeholder.com/150" alt="Obraz">

    <script>
        const obraz = document.querySelector("img");

        obraz.src = "https://via.placeholder.com/300";
    </script>

</body>
</html>
```

#### Wyjaśnienie:

* Pobieramy element `<img>`.
* `src` przechowuje adres obrazka.
* Po zmianie `src` przeglądarka pobiera nowy obraz.

---

### 2.5 Tworzenie nowych elementów

#### Koncepcja:

Elementy mogą być tworzone dynamicznie przez JavaScript. Nie muszą istnieć w HTML od początku.

#### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Tworzenie elementów</title>
</head>
<body>

    <main></main>

    <script>
        const main = document.querySelector("main");

        const akapit = document.createElement("p");

        akapit.textContent = "To jest nowy akapit.";

        main.appendChild(akapit);
    </script>

</body>
</html>
```

#### Wyjaśnienie:

* `createElement("p")` tworzy nowy element `<p>`.
* `textContent` ustawia jego tekst.
* `appendChild()` dodaje element do `<main>`.

---

### 2.6 Dynamiczna lista

#### Koncepcja:

Połączenie tworzenia elementów i dodawania ich do strony pozwala budować dynamiczne interfejsy. Lista może powstawać na podstawie danych zapisanych w tablicy.

#### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Dynamiczna lista</title>
</head>
<body>

    <main>
        <h1>Lista zakupów</h1>
        <ul></ul>
    </main>

    <script>
        const produkty = [
            "Chleb",
            "Mleko",
            "Jajka",
            "Masło"
        ];

        const lista = document.querySelector("ul");

        for (const produkt of produkty) {
            const elementListy = document.createElement("li");

            elementListy.textContent = produkt;

            lista.appendChild(elementListy);
        }
    </script>

</body>
</html>
```

#### Wyjaśnienie:

* Tablica przechowuje dane do wyświetlenia.
* Pętla przechodzi przez każdy element tablicy.
* Dla każdego produktu tworzony jest nowy element `<li>`.
* `appendChild()` dodaje element do listy `<ul>`.
* Lista powstaje automatycznie podczas działania programu.

---

## 3. Podsumowanie

* `querySelector()` wyszukuje elementy HTML.
* `textContent` zmienia lub odczytuje tekst elementu.
* `innerHTML` pozwala wstawiać kod HTML.
* `createElement()` tworzy nowe elementy.
* `appendChild()` dodaje element do DOM.
* Dynamiczne listy można budować na podstawie danych z tablic.

---

## 4. Zadanie praktyczne

Stwórz stronę zawierającą:

* semantyczny element `<main>`
* nagłówek `<h1>` z tekstem „Moje zadania”
* pustą listę `<ul>`

W JavaScript:

1. Utwórz tablicę z pięcioma zadaniami.
2. Pobierz element `<ul>` za pomocą `querySelector()`.
3. Dla każdego zadania utwórz element `<li>`.
4. Wstaw tekst zadania za pomocą `textContent`.
5. Dodaj każdy element `<li>` do listy przy użyciu `appendChild()`.
6. Po utworzeniu listy zmień tekst nagłówka na „Lista zadań na dziś” przy użyciu `textContent`.
