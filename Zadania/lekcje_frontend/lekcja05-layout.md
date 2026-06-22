# Lekcja: Box model + podstawy layoutu CSS

## 1. Wstęp

Celem lekcji jest zrozumienie, jak przeglądarka buduje elementy HTML w przestrzeni strony i jak CSS wpływa na ich rozmiar oraz odstępy. Poznasz model pudełkowy (box model), który jest podstawą całego layoutu w CSS. Nauczysz się kontrolować rozmiary elementów oraz odstępy między nimi za pomocą `margin`, `padding`, `border`, `width` i `height`. Dodatkowo zobaczysz, jak używać narzędzi deweloperskich do analizy stylów. To jest fundament pracy z frontendem w aplikacjach Flask i Django, gdzie HTML generuje backend, a CSS odpowiada za układ.

---

## 2. Zagadnienia

---

## 2.1 Box model (model pudełkowy)

### Koncepcja:

Każdy element HTML jest traktowany jak prostokąt składający się z: content, padding, border i margin. CSS kontroluje każdy z tych obszarów osobno.

### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Box model</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<div class="card">
    <h2>Jan Kowalski</h2>
    <p>Frontend developer</p>
</div>

</body>
</html>
```

```css
.card {
    width: 300px;
    padding: 20px;
    border: 2px solid black;
    margin: 30px;
}
```

### Wyjaśnienie:

* `width` określa szerokość zawartości elementu
* `padding` dodaje przestrzeń wewnątrz elementu (między treścią a borderem)
* `border` dodaje obramowanie wokół elementu
* `margin` dodaje przestrzeń na zewnątrz elementu
* wszystkie te warstwy razem tworzą „pudełko” elementu

---

## 2.2 Wysokość, szerokość i kontrola rozmiaru

### Koncepcja:

`width` i `height` kontrolują rozmiar elementu, ale ich zachowanie zależy od padding i border, dlatego trzeba rozumieć jak wpływają na finalny wymiar.

### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Rozmiary</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<div class="box">
    Box 1
</div>

<div class="box large">
    Box 2
</div>

</body>
</html>
```

```css
.box {
    width: 150px;
    height: 80px;
    border: 1px solid gray;
    margin: 10px;
}

.large {
    width: 300px;
    height: 120px;
    padding: 10px;
    border: 2px solid black;
}
```

### Wyjaśnienie:

* `width` ustawia szerokość elementu
* `height` ustawia wysokość elementu
* padding zwiększa realny rozmiar wizualny elementu
* border również zwiększa zajmowaną przestrzeń
* różne klasy pozwalają zmieniać wygląd tego samego elementu

---

## 2.3 Debug box model w DevTools

### Koncepcja:

Narzędzia deweloperskie przeglądarki pokazują dokładny box model elementu i pozwalają analizować margin, padding i border.

### Kod:

```html
<!-- komentarz -->
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>DevTools</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<div class="debug">
    Debug element
</div>

</body>
</html>
```

```css
.debug {
    width: 200px;
    padding: 15px;
    border: 3px solid blue;
    margin: 20px 10px;
    margin-left: 5px;
}
```

### Wyjaśnienie:

* DevTools pokazuje element jako „pudełko”
* widzisz osobno content, padding, border i margin
* możesz na żywo zmieniać CSS i obserwować efekt
* to podstawowe narzędzie do debugowania layoutu

---

### Inne wartości używane w CSS

Podsumowanie
- `px` = stałe piksele
- `%` = względem rodzica
- `em` = * font rodzica
- `rem` = * font root'a (html)
- `vw` = % szerokość ekranu
- `vh` = % wysokość ekranu

## 3. Podsumowanie

* każdy element HTML to box
* box składa się z: content, padding, border, margin
* `width` i `height` kontrolują rozmiar elementu
* padding zwiększa przestrzeń wewnętrzną
* margin kontroluje odstęp od innych elementów
* DevTools pozwala analizować box model
* CSS layout opiera się na tych zasadach

---

## 4. Zadanie praktyczne

Zbuduj kartę użytkownika:

Wymagania:

* element `.card`
* szerokość 300px
* padding 20px
* border 2px solid czarny
* margin 30px
* wewnątrz:

  * `h2` z imieniem
  * `p` z opisem
* dodaj drugi `.card` z innym użytkownikiem
* sprawdź w DevTools jak zmienia się box model

Pliki:

* `index.html`
* `style.css`
