# Lekcja: CSS responsywność (media queries, mobile-first, breakpointy)

---

## 1. Wstęp

Celem lekcji jest zrozumienie, jak strona internetowa dostosowuje się do różnych szerokości ekranu.
Poznasz media queries, podejście mobile-first oraz breakpointy.
Te mechanizmy są podstawą tworzenia stron działających na telefonach, tabletach i desktopach.
W praktyce są używane w każdym projekcie frontendowym oraz w widokach renderowanych przez Flask i Django.
Responsywność decyduje o tym, czy aplikacja działa poprawnie na urządzeniach użytkownika.
Bez tego interfejs jest nieużywalny poza jednym rozmiarem ekranu.

---

## 2. Zagadnienia

### 2.1 media queries

**Koncepcja:**

Media queries pozwalają zmieniać style CSS w zależności od szerokości ekranu.

**Kod:**

```html
<div class="box">Element</div>
```

```css
.box {
  width: 100%;
  background: lightblue;
}

@media (min-width: 600px) {
  .box {
    width: 50%;
  }
}
```

**Wyjaśnienie:**

* domyślnie element ma 100% szerokości
* od 600px wzwyż zmienia się na 50%
* CSS reaguje na szerokość ekranu

---

### 2.2 mobile-first

**Koncepcja:**

Mobile-first to podejście, w którym styl bazowy jest dla małych ekranów, a większe ekrany są nadpisywane media queries.

**Kod:**

```css
.container {
  display: block;
}

@media (min-width: 768px) {
  .container {
    display: flex;
  }
}
```

```html
<div class="container">
  <div>1</div>
  <div>2</div>
</div>
```

**Wyjaśnienie:**

* domyślnie układ jest prosty (mobile)
* od 768px włącza się flex (desktop)
* styl rośnie wraz z ekranem, nie maleje

---

### 2.3 breakpointy

**Koncepcja:**

Breakpoint to konkretna szerokość ekranu, w której zmienia się układ strony.

**Kod:**

```css
.card {
  width: 100%;
}

@media (min-width: 600px) {
  .card {
    width: 50%;
  }
}

@media (min-width: 1024px) {
  .card {
    width: 25%;
  }
}
```

```html
<div class="card">A</div>
<div class="card">B</div>
<div class="card">C</div>
<div class="card">D</div>
```

**Wyjaśnienie:**

* 600px → tablet
* 1024px → desktop
* elementy zmieniają szerokość zależnie od ekranu

---

## 3. Podsumowanie

* media queries sterują stylami zależnie od szerokości
* mobile-first zaczyna od małych ekranów
* breakpointy to konkretne progi zmiany layoutu
* CSS może mieć wiele warunków dla różnych ekranów
* responsywność jest standardem w webie i API UI

---

## 4. Zadanie praktyczne

Zbuduj responsywną sekcję:

1. Stwórz 3 elementy `.card`
2. Mobile-first:

   * domyślnie `width: 100%`
3. Dodaj breakpoint 600px:

   * `width: 50%`
4. Dodaj breakpoint 900px:

   * `width: 33%`
5. Użyj `display: block` w mobile i `display: flex` od 600px

Efekt:

* 1 kolumna na telefonie
* 2 kolumny na tabletach
* 3 kolumny na desktopie
