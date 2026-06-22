# Lekcja: Jak działa web (minimalny model)

---

## 1. Wstęp

Celem tej lekcji jest zrozumienie podstawowego modelu działania aplikacji webowych: przeglądarka wysyła żądanie, serwer odpowiada treścią, a przeglądarka ją renderuje. Poznasz rolę HTML jako struktury strony oraz podstawowe narzędzia DevTools do analizy działania strony. To fundament pod późniejszą pracę z Flask i Django, gdzie ten model będzie rozszerzany o logikę backendu i API. Na tym etapie nie ma jeszcze JavaScript ani frameworków. Skupiamy się na tym, co dzieje się „pod spodem”, gdy otwierasz stronę internetową.

---

## 2. Zagadnienia

---

### 2.1 Przeglądarka vs serwer

#### Koncepcja:

Przeglądarka (client) wysyła żądanie do serwera, a serwer zwraca odpowiedź (np. HTML). To podstawowy model komunikacji w webie: request → response.

#### Kod:

```text
PRZEGLĄDARKA (client)
GET /index.html  --------------------->  SERWER
                                        |
                                        |  zwraca HTML
                                        v
HTML <h1>Witaj</h1>  <------------------
```

#### Wyjaśnienie:

1. Przeglądarka inicjuje komunikację (nie serwer).
2. Żądanie to np. pobranie strony (`GET`).
3. Serwer zwraca dane (najczęściej HTML).
4. Przeglądarka renderuje otrzymany HTML jako stronę.

---

### 2.2 HTML jako struktura strony

#### Koncepcja:

HTML definiuje strukturę strony, czyli „co istnieje na stronie”, a nie jak wygląda.

#### Kod:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Moja pierwsza strona</title>
  </head>
  <body>
    <h1>Witaj świecie</h1>
    <p>To jest pierwszy dokument HTML</p>
  </body>
</html>
```

#### Wyjaśnienie:

1. `<!DOCTYPE html>` mówi przeglądarce, że to HTML5.
2. `<html>` to kontener całego dokumentu.
3. `<head>` zawiera metadane (np. tytuł zakładki).
4. `<body>` zawiera widoczną treść strony.
5. Elementy `<h1>`, `<p>` definiują strukturę treści.

---

### 2.3 Pierwszy plik HTML

#### Koncepcja:

Plik HTML to zwykły plik tekstowy, który przeglądarka interpretuje jako stronę internetową.

#### Kod:

```html
<!-- plik: index.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>Test strony</title>
  </head>
  <body>
    <h1>Strona działa</h1>
    <p>To jest lokalny plik HTML</p>
  </body>
</html>
```

#### Wyjaśnienie:

1. Tworzysz plik `index.html` na komputerze.
2. Otwierasz go w przeglądarce (double click).
3. Przeglądarka renderuje HTML bez serwera.
4. To pokazuje, że HTML działa lokalnie, ale w produkcji pochodzi z serwera.

---

### 2.4 DevTools (Elements + Network)

#### Koncepcja:

DevTools to narzędzie przeglądarki do analizy HTML, CSS i żądań sieciowych.

#### Kod:

```text
Brak kodu aplikacyjnego – narzędzie przeglądarki
```

#### Wyjaśnienie:

1. **Elements** – pokazuje aktualną strukturę HTML strony.
2. **Network** – pokazuje żądania HTTP (np. GET, status 200).
3. Możesz zobaczyć, co serwer faktycznie wysłał.
4. Umożliwia debugowanie backendu (Flask/Django później).
5. Każde odświeżenie strony to nowe żądanie w Network.

---

## 3. Podsumowanie

* Przeglądarka wysyła żądania HTTP do serwera.
* Serwer odpowiada danymi (np. HTML).
* HTML definiuje strukturę strony.
* DevTools pozwala analizować stronę i ruch sieciowy.
* Strona HTML może działać lokalnie bez backendu.
* Model request → response jest podstawą całego weba.

---

## 4. Zadanie praktyczne

1. Utwórz plik `index.html`.
2. Wklej do niego prostą strukturę HTML z:

   * `<h1>` z dowolnym tytułem
   * `<p>` z opisem siebie lub dowolnym tekstem
3. Otwórz plik w przeglądarce.
4. Otwórz DevTools (F12):

   * znajdź zakładkę **Elements**
   * znajdź strukturę swojego HTML
5. Odśwież stronę i sprawdź zakładkę **Network** (czy pojawia się dokument HTML).
