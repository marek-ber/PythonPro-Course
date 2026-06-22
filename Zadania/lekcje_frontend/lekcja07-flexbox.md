# Lekcja: Flexbox (core)

---

## 1. Wstęp

Celem lekcji jest opanowanie podstawowego układu Flexbox, który służy do kontrolowania rozmieszczenia elementów w jednym wymiarze (wiersz lub kolumna).
Poznasz kluczowe właściwości: `flex-direction`, `justify-content`, `align-items`, `gap`.
Flexbox jest standardem budowania navbarów, sekcji stron oraz prostych layoutów w aplikacjach frontendowych.
W praktyce używa się go w każdym projekcie webowym, również w szablonach Flask i Django.
Umożliwia szybkie wyrównywanie elementów bez ręcznego liczenia marginesów.
To fundament nowoczesnego CSS layoutu.

---

## 2. Zagadnienia

### 2.1 flex-direction

**Koncepcja:**

`flex-direction` określa kierunek układu elementów w kontenerze flex: poziomo lub pionowo.

**Kod:**

```html
<div class="container">
  <div class="item">A</div>
  <div class="item">B</div>
  <div class="item">C</div>
</div>
```

```css
.container {
  display: flex;
  flex-direction: row;
}

.item {
  padding: 10px;
  background: lightgray;
  border: 1px solid #000;
}
```

**Wyjaśnienie:**

* `display: flex` aktywuje Flexbox
* `flex-direction: row` ustawia elementy w poziomie
* domyślnie Flexbox działa w kierunku poziomym

---

### 2.2 justify-content i align-items

**Koncepcja:**

`justify-content` kontroluje układ w osi głównej, a `align-items` w osi poprzecznej.

**Kod:**

```html
<div class="container">
  <div class="box">1</div>
  <div class="box">2</div>
</div>
```

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 200px;
  border: 1px solid black;
}

.box {
  width: 50px;
  height: 50px;
  background: lightblue;
}
```

**Wyjaśnienie:**

* `justify-content: space-between` rozsuwa elementy na szerokość kontenera
* `align-items: center` centruje elementy w pionie
* `height` jest potrzebny, żeby było widać efekt osi pionowej

---

### 2.3 gap

**Koncepcja:**

`gap` definiuje odstępy między elementami wewnątrz kontenera flex bez używania marginesów.

**Kod:**

```html
<div class="container">
  <div class="item">X</div>
  <div class="item">Y</div>
  <div class="item">Z</div>
</div>
```

```css
.container {
  display: flex;
  gap: 20px;
}

.item {
  background: lightgreen;
  padding: 10px;
}
```

**Wyjaśnienie:**

* `gap` działa tylko w kontenerach flex/grid
* zastępuje marginesy między elementami
* zapewnia równe odstępy bez dodatkowego CSS

---

## 3. Podsumowanie

* `display: flex` aktywuje Flexbox
* `flex-direction` ustawia kierunek układu
* `justify-content` kontroluje oś główną
* `align-items` kontroluje oś pionową
* `gap` ustawia odstępy między elementami
* Flexbox działa w jednym wymiarze (wiersz lub kolumna)

---

## 4. Zadanie praktyczne

Zbuduj prostą stronę:

1. Stwórz navbar (`.navbar`) z 3 elementami: Home, About, Contact
2. Użyj `display: flex`
3. Ustaw `justify-content: space-between`
4. Ustaw `align-items: center`
5. Dodaj `gap: 15px` między linkami
6. Pod navbar dodaj sekcję `.layout` z 2 kolumnami (lewa i prawa) ustawionymi również flexem

Efekt:

* navbar rozciągnięty na szerokość
* elementy równomiernie rozmieszczone
* sekcja pod spodem w układzie 2 kolumn
