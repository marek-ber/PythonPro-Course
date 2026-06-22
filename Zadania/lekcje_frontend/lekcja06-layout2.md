# Lekcja: Layout — display + podstawy układu

---

## 1. Wstęp

Celem lekcji jest zrozumienie, jak elementy HTML zachowują się na stronie oraz jak kontrolować ich układ.
Poznasz różnice między elementami blokowymi i liniowymi oraz jak wpływa na nie właściwość `display`.
Nauczysz się również podstaw centrowania i ograniczania szerokości elementów.
Te mechanizmy są fundamentem budowania layoutów w CSS.
W praktyce są używane w każdej aplikacji webowej, zarówno w frontendzie, jak i w interfejsach renderowanych przez Flask lub Django templates.
Bez tego nie da się poprawnie budować UI ani struktur stron.

---

## 2. Zagadnienia

### 2.1 Elementy block / inline / inline-block

**Koncepcja:**

Elementy HTML mają domyślne zachowanie w układzie strony: zajmują całą linię (block) albo tylko tyle miejsca, ile potrzebują (inline).

**Kod:**

```html
<div class="block">Block 1</div>
<div class="block">Block 2</div>

<span class="inline">Inline 1</span>
<span class="inline">Inline 2</span>

<span class="inline-block">Inline-block 1</span>
<span class="inline-block">Inline-block 2</span>
```

```css
.block {
  display: block;
  background: lightgray;
}

.inline {
  display: inline;
  background: lightblue;
}

.inline-block {
  display: inline-block;
  background: lightgreen;
  width: 100px;
  height: 50px;
}
```

**Wyjaśnienie:**

* `block` zajmuje całą szerokość i zawsze zaczyna nową linię
* `inline` układa się w jednej linii, nie przyjmuje szerokości/wysokości
* `inline-block` zachowuje się jak inline, ale pozwala ustawiać wymiary

---

### 2.2 Właściwość display

**Koncepcja:**

`display` kontroluje sposób renderowania elementu w układzie strony.

**Kod:**

```html
<p class="example">Przykładowy tekst</p>
```

```css
.example {
  display: block;
}
```

**Wyjaśnienie:**

* `display` zmienia domyślne zachowanie elementu
* może przełączać elementy między block, inline i inline-block
* jest podstawą kontroli layoutu w CSS

---

### 2.3 max-width i centrowanie

**Koncepcja:**

`max-width` ogranicza szerokość elementu, a `margin: auto` pozwala go wyśrodkować.

**Kod:**

```html
<div class="container">
  Treść strony
</div>
```

```css
.container {
  max-width: 600px;
  margin: 0 auto;
  background: lightcoral;
}
```

**Wyjaśnienie:**

* `max-width` zapobiega rozciąganiu elementu na pełną szerokość ekranu
* `margin: 0 auto` automatycznie centruje element poziomo
* to podstawowy wzorzec dla layoutów stron i paneli aplikacji

---

## 3. Podsumowanie

* `block` zajmuje całą szerokość
* `inline` układa się w jednej linii
* `inline-block` łączy cechy obu
* `display` zmienia typ renderowania elementu
* `max-width` ogranicza szerokość kontenera
* `margin: auto` centruje element
* te zasady są bazą każdego layoutu

---

## 4. Zadanie praktyczne

Stwórz stronę HTML z trzema blokami:

1. Kontener `.container` o `max-width: 500px` i wycentrowany na stronie
2. W środku umieść 3 elementy `<div>` ustawione jako `inline-block`
3. Każdy ma mieć inną szerokość i tło

Efekt: elementy mają być w jednej linii (jeśli się mieszczą), a całość ma być wyśrodkowana na stronie.
