## Zadanie 1. Uruchomienie prostego kontenera i połączenie z aplikacją Django

**Cel zadania:**
Nauczyć się uruchamiać gotowe obrazy Dockera oraz skonfigurować komunikację między aplikacją Django a zewnętrznym kontenerem (np. Memcached).

**Wymagania:**

* uruchom prosty kontener (np. Memcached),
* skonfiguruj aplikację Django tak, aby korzystała z uruchomionego kontenera,
* sprawdź poprawność połączenia.

**Rozwiązanie:**

* `lesson_37_1_cmds.txt` – komendy Dockera potrzebne do wykonania zadania,
* `lesson_37_1_{nazwa_pliku}.py` – zmodyfikowane pliki konfiguracyjne Django.

---

## Zadanie 2. Własny Dockerfile dla aplikacji Django

**Cel zadania:**
Poznać sposób budowania własnego obrazu Docker oraz wykorzystania zmiennych środowiskowych do konfiguracji aplikacji.

**Wymagania:**

* utwórz własny `Dockerfile` dla aplikacji Django,
* wykorzystaj zmienne środowiskowe (`ENV` lub plik `.env`),
* zbuduj obraz i uruchom kontener.

**Rozwiązanie:**

* `lesson_37_2_dockerfile`,
* `lesson_37_2_cmds.txt` – komendy potrzebne do wykonania zadania.

---

## Zadanie 4. Utworzenie pliku `.dockerignore`

**Cel zadania:**
Zrozumieć, które pliki nie powinny trafiać do obrazu Dockera oraz dlaczego ich pomijanie przyspiesza budowanie obrazu i zmniejsza jego rozmiar.

**Wymagania:**

* zapoznaj się z przeznaczeniem pliku `.dockerignore`,
* określ, jakie pliki i katalogi należy wykluczyć,
* utwórz kompletny plik `.dockerignore`.

**Rozwiązanie:**

* `lesson_37_4.dockerignore`.

---

## Zadanie 5. Środowisko wielokontenerowe

**Cel zadania:**
Nauczyć się budować środowisko składające się z wielu współpracujących kontenerów oraz skonfigurować komunikację między nimi z wykorzystaniem sieci Dockera, Docker DNS oraz wolumenów do trwałego przechowywania danych.

**Wymagania:**

* utwórz środowisko wielokontenerowe składające się z:

  * aplikacji Django,
  * bazy PostgreSQL,
  * opcjonalnie dodatkowego kontenera (np. pgAdmin lub Redis),
* skonfiguruj komunikację między kontenerami,
* wykorzystaj Docker DNS (nazwy usług zamiast adresów IP),
* skonfiguruj wspólną sieć Docker,
* utwórz **named volume** dla PostgreSQL, aby dane bazy były przechowywane poza kontenerem,
* sprawdź, że po usunięciu i ponownym utworzeniu kontenera PostgreSQL dane pozostają dostępne,
* wykonaj migracje modeli z wnętrza kontenera aplikacji.

**Zadanie uznaje się za zaliczone, jeśli:**

* kontenery poprawnie komunikują się ze sobą,
* aplikacja Django łączy się z bazą PostgreSQL,
* migracje wykonują się poprawnie,
* dane w bazie pozostają po ponownym uruchomieniu lub odtworzeniu kontenera dzięki wykorzystaniu wolumenu.

**Rozwiązanie:**

* `lesson_37_5_dockerfile`,
* `lesson_37_5_docker-compose.yml`,
* `lesson_37_5_{nazwa_pliku}.py` – zmodyfikowane pliki konfiguracyjne Django,
* `lesson_37_5_cmds.txt` – komendy potrzebne do wykonania zadania.


---

## Zadanie 6. Multi-stage Dockerfile

**Cel zadania:**
Poznać technikę budowania obrazów wieloetapowych (multi-stage build) oraz zrozumieć, kiedy i dlaczego stosuje się takie rozwiązanie.

**Wymagania:**

* utwórz wieloetapowy `Dockerfile`,
* zastosuj co najmniej dwa etapy budowania,
* przygotuj końcowy obraz zawierający wyłącznie pliki niezbędne do uruchomienia aplikacji,
* zapoznaj się z zaletami multi-stage build:

  * mniejszy rozmiar obrazu,
  * większe bezpieczeństwo,
  * brak zbędnych narzędzi kompilacyjnych w finalnym obrazie,
  * szybsze wdrażanie aplikacji.

**Rozwiązanie:**

* `lesson_37_6_dockerfile`.
