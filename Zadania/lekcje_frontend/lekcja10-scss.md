# Lekcja: SCSS (koncepcja) + podstawy stylowania aplikacji

## 1. Wstęp

Celem lekcji jest zrozumienie, czym jest SCSS i dlaczego używa się go zamiast czystego CSS w większych projektach frontendowych.
Poznasz trzy kluczowe elementy: zmienne, nesting oraz to, że SCSS nie działa bezpośrednio w przeglądarce.
Zobaczysz różnicę między SCSS a CSS na konkretnych przykładach kodu.
Dowiesz się również, jak SCSS jest zamieniany na CSS oraz jak można go kompilować lokalnie.
W praktyce SCSS jest używany w aplikacjach webowych (np. dashboardy, systemy administracyjne, aplikacje SPA), gdzie liczba stylów szybko rośnie.

---

## 2. Zagadnienia

## 2.1 Variables w SCSS

### Koncepcja:

Zmienne w SCSS pozwalają przechowywać wartości (np. kolory) w jednym miejscu i wielokrotnie ich używać.
Zmiana jednej zmiennej aktualizuje cały styl.

### Kod:

```scss id="scss_var_1"
$primary-color: #2c3e50;
$text-color: #ffffff;

header {
  background: $primary-color;
  color: $text-color;
  padding: 20px;
}

button {
  background: $primary-color;
  color: $text-color;
  border: none;
}
```

### Wyjaśnienie:

* `$primary-color` przechowuje kolor główny
* `$text-color` przechowuje kolor tekstu
* zmienne są używane w wielu miejscach
* zmiana jednej wartości wpływa na cały styl

---

## 2.2 Nesting w SCSS

### Koncepcja:

Nesting pozwala zapisywać selektory CSS wewnątrz innych selektorów, co odzwierciedla strukturę HTML.
Ułatwia organizację stylów w większych komponentach.

### Kod:

```scss id="scss_nest_1"
.dashboard {
  header {
    background: #2c3e50;
    color: white;
  }

  nav {
    background: #ecf0f1;

    ul {
      list-style: none;

      li {
        padding: 8px;
        color: #333;
      }
    }
  }

  main {
    padding: 20px;

    .card {
      border: 1px solid #ccc;
      padding: 10px;
    }
  }
}
```

### Wyjaśnienie:

* `.dashboard` jest głównym kontenerem
* selektory są zagnieżdżone zgodnie z HTML
* SCSS generuje pełne selektory CSS automatycznie
* struktura stylów jest bardziej czytelna

---

## 2.3 SCSS → CSS + kompilacja

### Koncepcja:

SCSS nie jest rozumiany przez przeglądarkę.
Musi zostać przetłumaczony (skompilowany) do CSS przed użyciem.

### Kod (wynik CSS):

```css id="css_output_1"
header {
  background: #2c3e50;
  color: white;
  padding: 20px;
}

button {
  background: #2c3e50;
  color: #ffffff;
  border: none;
}

.dashboard nav ul {
  list-style: none;
}

.dashboard nav ul li {
  padding: 8px;
  color: #333;
}

.dashboard main .card {
  border: 1px solid #ccc;
  padding: 10px;
}
```

### Wyjaśnienie:

* SCSS zamienia się w standardowy CSS
* przeglądarka widzi tylko CSS
* nesting zostaje rozwinięty do pełnych selektorów
* zmienne zostają zastąpione wartościami

---

### Kompilacja SCSS (narzędzia i proces)

SCSS kompiluje się lokalnie przed uruchomieniem strony.

#### Narzędzie 1: Dart Sass (najprostsze i standardowe)

Instalacja:

```bash id="sass_install"
npm install -g sass
```

Kompilacja pliku:

```bash id="sass_compile"
sass style.scss style.css
```

Tryb automatyczny (watch):

```bash id="sass_watch"
sass --watch style.scss:style.css
```

---

#### Narzędzie 2: VS Code Live Sass Compiler

* instalacja jako rozszerzenie VS Code
* kliknięcie „Watch Sass”
* automatyczne generowanie CSS

---

## 3. Podsumowanie

* SCSS rozszerza CSS o zmienne i nesting
* zmienne zaczynają się od `$`
* nesting odwzorowuje strukturę HTML
* SCSS nie działa bez kompilacji
* wynik SCSS to standardowy CSS
* najprostsze narzędzie: `sass --watch`
* przeglądarka interpretuje tylko CSS

---

## 4. Zadanie praktyczne

Utwórz projekt stylowania strony:

Wymagania:

* użyj semantycznego HTML: `header`, `nav`, `main`
* w SCSS zdefiniuj zmienną koloru głównego
* użyj nesting do stylowania całej struktury
* dodaj `nav ul li` wewnątrz nesting
* dodaj 3 karty w `main`
* skompiluj SCSS do CSS przy użyciu `sass --watch`
* podłącz wygenerowany CSS do HTML

Efekt: strona z jednolitą kolorystyką i uporządkowanym SCSS w strukturze komponentowej
