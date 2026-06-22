# Lekcja: Jak działa web + podstawy CSS Grid

## 1. Wstęp

Celem tej lekcji jest zrozumienie jak buduje się układ strony za pomocą CSS Grid.
CSS Grid pozwala układać elementy w dwuwymiarowej siatce (wiersze i kolumny), co jest standardem w nowoczesnych dashboardach i panelach administracyjnych.
W praktyce Grid jest używany w aplikacjach webowych do budowy layoutów typu: dashboard, panel użytkownika, CRM.

---

## 2.2 CSS Grid – podstawy układu

### Koncepcja:

CSS Grid pozwala tworzyć układ strony w formie siatki z kolumn i wierszy.
Elementy potomne są automatycznie rozmieszczane w tej siatce.

### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <title>Dashboard Grid</title>
  <style>
    .dashboard {
      display: grid;
      grid-template-columns: 250px 1fr;
      grid-template-rows: 60px 1fr;
      gap: 10px;
      height: 100vh;
    }

    header {
      grid-column: 1 / 3;
      background: #333;
      color: white;
      padding: 15px;
    }

    nav {
      background: #f0f0f0;
      padding: 10px;
    }

    main {
      background: #e0e0e0;
      padding: 10px;
    }
  </style>
</head>
<body>

<div class="dashboard">
  <header>Header</header>
  <nav>Menu</nav>
  <main>Main content</main>
</div>

</body>
</html>
```

### Wyjaśnienie:

* `display: grid` → aktywuje układ siatki
* `grid-template-columns: 200px 1fr 1fr` → 3 kolumny (stała + elastyczne)
* `gap: 10px` → odstępy między elementami
* elementy `.box` automatycznie wypełniają kolejne pola siatki

---

## 2.3 Dashboard layout (praktyczne użycie Grid)

### Koncepcja:

Dashboard to układ aplikacji z menu, główną treścią i panelem bocznym.
Grid pozwala zdefiniować taki layout w jednej strukturze CSS.

### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <title>Dashboard Grid</title>
  <style>
    .dashboard {
      display: grid;
      grid-template-columns: 250px 1fr;
      grid-template-rows: 60px 1fr;
      gap: 10px;
      height: 100vh;
    }

    .header {
      grid-column: 1 / 3;
      background: #333;
      color: white;
      padding: 15px;
    }

    .sidebar {
      background: #f0f0f0;
      padding: 10px;
    }

    .content {
      background: #e0e0e0;
      padding: 10px;
    }
  </style>
</head>
<body>

<div class="dashboard">
  <div class="header">Header</div>
  <div class="sidebar">Menu</div>
  <div class="content">Main content</div>
</div>

</body>
</html>
```

### Wyjaśnienie:

* `grid-template-columns: 250px 1fr` → sidebar + content
* `grid-template-rows: 60px 1fr` → header + reszta strony
* `grid-column: 1 / 3` → header zajmuje całą szerokość
* `100vh` → wysokość całego ekranu

---

## 3. Podsumowanie

* CSS Grid buduje układy 2D (wiersze i kolumny)
* `grid-template-columns` definiuje strukturę kolumn
* `gap` kontroluje odstępy
* `grid-column` pozwala rozciągać elementy
* Dashboardy są typowym zastosowaniem Grid

---

## 4. Zadanie praktyczne

Zbuduj jeden plik HTML:

Wymagania:

* layout dashboard
* 3 sekcje:

  * header (pełna szerokość)
  * sidebar (lewa kolumna)
  * content (prawa kolumna)
* dodaj 4 kafelki w content używając Grid
* użyj `grid-template-columns` i `gap`

Czas: 5–10 minut
Efekt: działający układ przypominający prosty panel administracyjny
