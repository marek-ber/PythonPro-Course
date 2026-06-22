# Lekcja: CSS podstawy + selektory + stylowanie HTML

## 1. Wstęp

Celem lekcji jest zrozumienie, jak CSS zmienia wygląd HTML oraz jak działa selekcjonowanie elementów na stronie. Nauczysz się podstawowych selektorów, ustawiania kolorów i fontów oraz stylowania elementów w sposób używany w Flask i Django templates. CSS jest warstwą prezentacji, która działa niezależnie od backendu, ale jest z nim ściśle powiązana przez HTML generowany przez serwer. W praktyce każdy widok w aplikacjach webowych jest kombinacją HTML + CSS + dane z backendu. Ta lekcja pokazuje minimalny, realny model pracy frontend + backend.

---

## 2. Zagadnienia

---

## 2.1 Podłączenie CSS do HTML

### Koncepcja:

CSS można podłączyć do HTML przez zewnętrzny plik `.css`, który definiuje wygląd elementów strony. HTML pozostaje strukturą, CSS odpowiada za styl.

### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>CSS podstawy</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<header>
    <h1>Moja strona</h1>
</header>

<main>
    <p>To jest paragraf tekstu</p>
</main>

</body>
</html>
```

```css
body {
    background-color: #f2f2f2;
}
```

### Wyjaśnienie:

* `<link rel="stylesheet">` łączy HTML z CSS
* `style.css` to zewnętrzny plik stylów
* `body {}` oznacza styl całej strony
* `background-color` ustawia kolor tła
* CSS nie zmienia treści, tylko wygląd

---

## 2.2 Selektory CSS

### Koncepcja:

Selektory określają, które elementy HTML mają zostać wystylowane. Mogą odnosić się do tagów, klas lub identyfikatorów.

### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Selektory CSS</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<h1>Główny tytuł</h1>

<p class="tekst">Pierwszy paragraf</p>
<p class="tekst">Drugi paragraf</p>

<p id="specjalny">Specjalny paragraf</p>

</body>
</html>
```

```css
h1 {
    color: blue;
}

.tekst {
    color: green;
    font-size: 18px;
}

#specjalny {
    color: red;
    font-weight: bold;
}
```

### Wyjaśnienie:

* `h1` → selektor tagu (wszystkie h1)
* `.tekst` → selektor klasy (wiele elementów)
* `#specjalny` → selektor id (jeden element)
* `color` ustawia kolor tekstu
* `font-size` zmienia wielkość tekstu
* `font-weight` zmienia grubość fontu

---

## 3. Podsumowanie

* CSS odpowiada za wygląd, HTML za strukturę
* CSS podłącza się przez `<link>`
* selektory: tag, klasa, id
* `body` styluje całą stronę
* `.class` działa na wiele elementów
* `#id` działa na jeden element
* CSS nie zmienia danych, tylko ich prezentację

---

## 4. Zadanie praktyczne

Stwórz stronę HTML i CSS:

Wymagania:

* tło strony: jasnoszare
* nagłówek (`h1`) ma być czerwony
* trzy paragrafy:

  * pierwszy i drugi mają klasę `tekst` i są niebieskie
  * trzeci ma id `wyróżniony` i jest pogrubiony oraz zielony

Pliki:

* `index.html`
* `style.css`

Nie używaj inline CSS.
