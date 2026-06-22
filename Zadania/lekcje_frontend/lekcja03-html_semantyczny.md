# Lekcja: Jak działa web + HTML semantyczny

## 1. Wstęp

Celem lekcji jest zrozumienie struktury HTML opartej o znaczniki semantyczne. Poznasz, jak przeglądarka komunikuje się z serwerem i co faktycznie dostaje w odpowiedzi. Następnie nauczysz się budować stronę w HTML w sposób czytelny dla przeglądarek, frameworków backendowych (Flask, Django) oraz wyszukiwarek. Ten model jest fundamentem dla pracy z REST API i template’ami backendowymi. Bez tego trudno zrozumieć, skąd bierze się widok strony. Lekcja skupia się na praktyce, nie teorii abstrakcyjnej.

---

## 2 HTML semantyczny

### Koncepcja:

HTML semantyczny oznacza używanie znaczników opisujących znaczenie struktury strony, a nie tylko wygląd. Zamiast `div` używa się elementów opisujących rolę treści.

### Kod:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Strona semantyczna</title>
</head>

<body>

<header>
    <h1>Moja strona</h1>
</header>

<main>
    <section>
        <h2>O mnie</h2>
        <p>Jestem początkującym developerem.</p>
    </section>

    <section>
        <h2>Artykuły</h2>

        <article>
            <h3>Artykuł 1</h3>
            <p>Treść pierwszego artykułu.</p>
        </article>

        <article>
            <h3>Artykuł 2</h3>
            <p>Treść drugiego artykułu.</p>
        </article>

    </section>
</main>

<footer>
    <p>Stopka strony</p>
</footer>

</body>
</html>
```

### Wyjaśnienie:

* `header` → nagłówek strony (tytuł, logo)
* `main` → główna treść strony
* `section` → logiczne sekcje treści
* `article` → niezależne jednostki treści
* `footer` → stopka strony
* struktura jest czytelna dla:

  * przeglądarek
  * SEO
  * backendowych template’ów (Flask/Django)
* ułatwia późniejsze podpinanie dynamicznych danych

---

## 3. Podsumowanie

* web działa w modelu request → response
* backend zwraca HTML do przeglądarki
* Flask może zwracać HTML jako string
* HTML semantyczny opisuje strukturę, nie wygląd
* `header`, `main`, `section`, `article`, `footer` mają konkretne role
* semantyka poprawia SEO i czytelność kodu
* backendowe template’y bazują na tej strukturze

---

## 4. Zadanie praktyczne

Przepisz poniższy HTML (zakładając, że to „stara strona”) na wersję semantyczną:

```html
<div>
    <div>Moja strona</div>

    <div>
        <div>O mnie</div>
        <div>Jestem junior dev</div>
    </div>

    <div>
        <div>Post 1</div>
        <div>Treść 1</div>
    </div>

    <div>Stopka</div>
</div>
```

Wymagania:

* użyj `header`, `main`, `section`, `article`, `footer`
* zachowaj strukturę treści
* kod ma być pełnym dokumentem HTML
