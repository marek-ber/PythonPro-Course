# Od aplikacji Django do aplikacji produkcyjnej — podstawy DevOps

**Czas trwania:** ~5h
**Cel główny:** Zrozumienie istoty DevOps i mechanizmów działania aplikacji w środowisku produkcyjnym. Nie będziemy dziś konfigurować całego serwera – skupimy się na tym, **jak projektować** aplikację w Django, aby była gotowa na wdrożenie (deployment).

### Co osiągniesz po tej lekcji?

* Zaprojektujesz architekturę aplikacji produkcyjnej.
* Zrozumiesz różnice między kodem, plikami statycznymi, mediami, bazą danych i cache'em.
* Przygotujesz kod Django pod przyszłe wdrożenie (zmienne środowiskowe, ścieżki plików).
* Zrozumiesz, z jakich klocków składa się nowoczesne środowisko webowe.

---

## 1. Dlaczego aplikacja lokalna nie jest produkcyjna (30 min)

**Cel:** Zmiana sposobu myślenia.

Kiedy uczysz się Django, Twoje środowisko pracy wygląda zazwyczaj tak:

* **Twój laptop** (jedno urządzenie, na którym robisz wszystko).
* Komenda `python manage.py runserver` (wbudowany serwer deweloperski).
* Baza danych **SQLite** (jeden plik na dysku).
* Pliki wgrywane przez użytkowników (np. zdjęcia) lądują w folderze wewnątrz projektu.

To świetne środowisko do nauki i szybkiego prototypowania. Jednak **produkcja to zupełnie inny świat**.

Na produkcji architektura rozrasta się do systemu naczyń połączonych:

```text
       [ Użytkownik ]
             ↓
        [ Nginx ] (Serwer WWW / Reverse Proxy)
             ↓
       [ Gunicorn ] (Serwer aplikacji WSGI)
             ↓
        [ Django ] (Twoja aplikacja)
             ↓
      [ PostgreSQL ] (Baza danych)
             ↓
[ Storage plików (np. AWS S3) ]
             ↓
     [ Monitoring ] (Śledzenie błędów i wydajności)

```

### Za co tak naprawdę odpowiada Django?

W architekturze produkcyjnej Django ma bardzo konkretne zadanie.
**Django POWINNO:**

* Obsługiwać logikę biznesową (np. obliczać rabaty, tworzyć raporty).
* Wystawiać API dla frontend'u lub aplikacji mobilnych.
* Autoryzować i obsługiwać użytkowników.

**Django NIE POWINNO:**

* Serwować dużych plików (zdjęć, filmów, CSS, JS) – jest do tego zbyt wolne w porównaniu do wyspecjalizowanych narzędzi.
* Zarządzać całym ruchem HTTP (np. certyfikatami SSL/HTTPS).
* Przechowywać danych użytkownika w katalogu z kodem.

---

## 2. Projektowanie aplikacji pod produkcję (60 min)

Zaprojektujmy przykładową aplikację – **"Task Manager"** (System zarządzania zadaniami).
Jej funkcje to: obsługa użytkowników, tworzenie projektów, przypisywanie zadań, dodawanie komentarzy i załączników, wysyłanie powiadomień.

Jak rozbijemy to na komponenty produkcyjne?

```text
                Użytkownik
                    |
                 Nginx  (Ruch sieciowy, HTTPS, pliki statyczne)
                    |
                Django  (Mózg operacji)
       ------------------------
       |          |            |
   PostgreSQL   Redis       Storage
  (Dane SQL)  (Kolejki)    (Pliki)
                    |
              Monitoring (Kontrola zdrowia systemu)

```

### Dlaczego potrzebujemy tych wszystkich klocków?

Każdy komponent rozwiązuje konkretny problem, z którym Django w pojedynkę by sobie nie poradziło (lub robiłoby to nieefektywnie):

1. **Django**
* *Problem:* Gdzie trzymać reguły biznesowe (kto ma dostęp do projektu, jak zmienić status zadania)?
* *Rozwiązanie:* Aplikacja webowa napisana w Pythonie.


2. **PostgreSQL**
* *Problem:* Gdzie bezpiecznie, szybko i trwale przechowywać relacyjne dane (użytkownicy, zadania)? (SQLite przy wielu jednoczesnych użytkownikach blokuje plik i powoduje błędy).
* *Rozwiązanie:* Zewnętrzna, potężna baza danych.


3. **Storage (System plików / Object Storage)**
* *Problem:* Gdzie trzymać awatary i załączniki do zadań, żeby nie zapchać dysku serwera aplikacyjnego i nie stracić ich przy aktualizacji kodu?
* *Rozwiązanie:* Osobny, skalowalny system plików (np. AWS S3).


4. **Redis**
* *Problem:* Jak szybko pobrać często używane dane (cache) lub oddelegować ciężkie zadanie (np. wysyłkę 1000 maili z powiadomieniami) w tle, by nie blokować użytkownika?
* *Rozwiązanie:* Baza danych w pamięci RAM używana jako cache lub broker wiadomości (np. dla biblioteki Celery).



---

## 3. Static files i media files (45 min)

W Django rozróżniamy dwa typy plików nieserwerowych. Zrozumienie tej różnicy to "być albo nie być" na produkcji.

### Static (Pliki statyczne)

* **Co to jest?** Pliki CSS, JavaScript, logo Twojej firmy, wbudowane fonty.
* **Skąd pochodzą?** Od Ciebie (programisty). Są częścią kodu.
* **Proces produkcyjny:**
`Kod Django` ➔ komenda `manage.py collectstatic` ➔ zrzut wszystkich plików do jednego folderu `staticfiles/` ➔ serwowanie ich bezpośrednio przez szybkiego **Nginxa**.

### Media (Pliki mediów)

* **Co to jest?** Awatary, załączone dokumenty (PDF), zdjęcia dodane przez użytkowników.
* **Skąd pochodzą?** Od użytkownika (upload).
* **Proces produkcyjny:**
`Upload od usera` ➔ `Django przetwarza żądanie` ➔ `Zapis do zewnętrznego Storage (np. AWS S3)`.

### Konfiguracja (settings.py)

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles" # Tu collectstatic wrzuci pliki

# MEDIA
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media" # Tylko do developmentu! Na produkcji to np. S3

```

**Dlaczego plików Media NIE trzymamy w repozytorium Git ani na dysku obok kodu?**

1. Kod to kod, dane to dane. Backup bazy danych i plików z załącznikami robi się inaczej niż backup kodu.
2. Kontenery (np. Docker) są "ulotne". Jeśli zrestartujesz kontener, stracisz wszystko, co użytkownicy wgrali na jego lokalny dysk.
3. Skalowanie: jeśli masz 3 serwery z Django, na który z nich ma trafić plik? Muszą mieć wspólny, zewnętrzny dysk (Storage).

---

## 4. Baza danych i konfiguracja środowiska (45 min)

**Złota zasada DevOps:** Nigdy nie trzymaj haseł ani konfiguracji środowiska bezpośrednio w kodzie!

**Złe podejście:**

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "tasks",
        "USER": "admin",
        "PASSWORD": "SuperSecretPassword123", # NIGDY TAK NIE RÓB!
    }
}

```

**Rozwiązanie:** Zmienne środowiskowe (Environment Variables).
Dzięki nim ten sam kod może działać na Twoim komputerze, na serwerze testowym (Staging) i na Produkcji – wystarczy zmienić plik konfiguracyjny (np. `.env`), który **nie trafia** do GitHuba.

**Przykład pliku `.env` (lokalnie na serwerze):**

```env
POSTGRES_DB=tasks
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db

```

**Konfiguracja w `settings.py`:**

```python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST")
    }
}

```

*(W projektach często używa się też świetnej biblioteki `django-environ`, która ułatwia to zadanie).*

---

## 5. Reverse proxy — idea (45 min)

Reverse proxy to serwer, który stoi "przed" Twoją aplikacją Django i przejmuje pierwszy kontakt z użytkownikiem. Najpopularniejszym narzędziem do tego jest **Nginx**.

**Problem:**
Jeśli wystawisz Django bezpośrednio do Internetu, zmusisz je do robienia rzeczy, do których nie zostało stworzone. Python jest wolniejszy w czytaniu plików z dysku niż Nginx (napisany w C). Co więcej, Django (przez Gunicorn) nie potrafi samo z siebie obsłużyć szyfrowania HTTPS.

**Rozwiązanie:** Nginx działa jak recepcjonista.

```text
[ Internet ]
      ↓
   [ Nginx ] (Nasłuchuje na porcie 80/443, odszyfrowuje HTTPS)
      ↓
  Czy to żądanie o plik statyczny (np. /static/style.css)?
  ➔ TAK: Nginx sam oddaje plik w ułamek sekundy. Django nawet o tym nie wie.
  ➔ NIE (np. /api/tasks/): Nginx przekazuje żądanie do Django.

```

Nginx zajmuje się certyfikatami SSL, bezpieczeństwem (np. blokowaniem ataków DDoS) i odciążaniem Django ze statycznych zadań.

---

## 6. Docker i przygotowanie środowiska (45 min)

Żeby uruchomić naszą aplikację, Nginxa, Redis'a i Postgresa, musielibyśmy ręcznie instalować każdy z tych programów na serwerze. To koszmar w utrzymaniu.

Rozwiązaniem jest **Docker**. Traktuj Dockera jak wirtualne, lekkie "pudełka" (kontenery), w których zamykasz aplikację wraz z jej zależnościami. Każdy klocek z naszego diagramu to osobny kontener.

**Przykładowa struktura projektu:**

```text
project/
 ├── docker-compose.yml  <-- Mapa, jak połączyć wszystkie kontenery
 ├── app/
 │   ├── Dockerfile      <-- Instrukcja, jak zbudować kontener dla Django
 │   ├── requirements.txt
 │   └── manage.py
 └── nginx/
     └── nginx.conf      <-- Konfiguracja naszego "recepcjonisty"

```

**Przykład `docker-compose.yml` (koncepcja):**

```yaml
version: '3.8'
services:
  web:
    build: ./app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:16
    env_file:
      - .env

  nginx:
    image: nginx
    ports:
      - "80:80"

```

**Zrozum ideę:** Dzięki Dockerowi środowisko jest powtarzalne. Jeśli wpiszesz `docker-compose up` na swoim laptopie, dostaniesz dokładnie taką samą bazę danych i infrastrukturę, jaka będzie działać na serwerze produkcyjnym.

---

## 7. Monitoring i utrzymanie aplikacji (30 min)

Wrzuciłeś aplikację do sieci. Gratulacje! Ale skąd wiesz, że ona działa? A co, jeśli ulegnie awarii o 3 w nocy?

Musimy monitorować system. Składają się na to 3 filary:

1. **Healthcheck (Sprawdzanie pulsu)**
Tworzysz prosty endpoint w Django, np. `/health/`.
```json
{ "status": "ok", "db_connected": true }

```


Zewnętrzny system co minutę pyta ten endpoint. Jeśli nie dostanie odpowiedzi "ok", wysyła powiadomienie do programisty.
2. **Logi**
Błędy (`ERROR`), ostrzeżenia (`WARNING`) i informacje o ruchu. Musisz mieć narzędzie, które zbiera logi z Django, Nginxa i Bazy Danych w jedno miejsce, żeby móc łatwo analizować awarie.
3. **Metryki**
Liczby i wykresy. Ile mamy zapytań na sekundę? Ile zużywamy RAM-u? Jaki jest średni czas odpowiedzi?
*Narzędzia:* **Prometheus** (zbiera dane z systemu) + **Grafana** (rysuje piękne wykresy). Do zadań w tle (Celery) używa się np. narzędzia **Flower**.

---

## 8. AWS jako przykład infrastruktury (30 min)

Pojęcia takie jak "Chmura" (Cloud) czy AWS to nic magicznego. Zrozumienie chmury polega na mapowaniu pojęć lokalnych na ich usługi. Architektura Twojej aplikacji się nie zmienia, zmienia się tylko "wynajmujący" sprzęt.

**Tabela mapowania technologii:**

| Twoja potrzeba               | Twój lokalny stack (Docker) | Odpowiednik w chmurze AWS        |
| ---------------------------- | --------------------------- | -------------------------------- |
| **Serwer / Maszyna**         | Twój laptop                 | **EC2** (Wirtualny serwer)       |
| **Baza danych**              | Kontener `postgres:16`      | **RDS** (Zarządzana baza danych) |
| **Miejsce na pliki (Media)** | Folder na dysku laptopa     | **S3** (Object Storage)          |
| **Monitoring logów / CPU**   | Terminal na laptopie        | **CloudWatch**                   |
| **Domena (DNS)**             | `localhost` / `127.0.0.1`   | **Route 53**                     |

**Najważniejsza idea:** AWS nie zmienia zasady działania Twojego Django. AWS daje po prostu gotowe, skalowalne i bezpieczne klocki, z których układasz architekturę, o której mówiliśmy na początku.

---




## 9. Projekt końcowy lekcji (30 min)

Twoim zadaniem jest samodzielne zaprojektowanie (na papierze lub w programie do notatek) architektury dla Twojej wybranej wymarzonej aplikacji (np. klon Instagrama, system dla sklepu, portal z ogłoszeniami).

**Krok 1: Narysuj diagram przepływu**
Stwórz ścieżkę od Użytkownika aż po najgłębsze elementy infrastruktury (gdzie idzie ruch, gdzie są pliki, gdzie są dane).
*Podpowiedź:* Użyj klocków: *User, Nginx, Django, Postgres, S3, Redis, Grafana*.

**Krok 2: Tabela komponentów**
Stwórz tabelę określającą, jaki element odpowiada za co w Twoim systemie (Logika, Dane, Cache, Pliki, Ruch, Kontrola).

**Krok 3: Implementacja w kodzie (zadanie domowe)**
Wejdź do swojego projektu w Django i przygotuj go pod wdrożenie:

1. Zainstaluj `django-environ` (lub `python-dotenv`).
2. Przenieś klucze, hasła i URL bazy danych do pliku `.env`.
3. Skonfiguruj `STATIC_ROOT` i `STATIC_URL` w `settings.py`.
4. Skonfiguruj `MEDIA_ROOT` i `MEDIA_URL` w `settings.py`.
5. Napisz prosty widok `health_check` zwracający JSON ze statusem "OK" i podepnij go pod URL `/health/`.


### Rozszerzenie 1: Jak w ogóle dostać się na serwer? Czym jest SSH (15 min)

*(To warto dodać przed omawianiem konfiguracji na serwerze, np. między sekcją 4 a 5)*

**Problem:** Masz już wykupiony serwer w chmurze (np. AWS EC2). Jak tam wejść? Przecież nie podłączysz do niego klawiatury i monitora.
**Rozwiązanie:** SSH (Secure Shell).

**Co to jest?**
SSH to protokół sieciowy, który pozwala na bezpieczne (szyfrowane) połączenie terminalowe z obcym komputerem przez Internet.

**Jak z tego korzystamy?**
Wpisujesz w swoim lokalnym terminalu:
`ssh user@adres-twojego-serwera`
I nagle Twój terminal staje się terminalem serwera w chmurze. Możesz tam tworzyć pliki, uruchamiać Dockera, czytać logi.

**Dlaczego to standard?**

1. **Szyfrowanie:** Cały ruch jest szyfrowany. Nikt nie "podsłucha" Twoich haseł w sieci.
2. **Klucze SSH zamiast haseł:** W DevOps rzadko używa się haseł do logowania. Zamiast tego na swoim laptopie generujesz kryptograficzny "klucz prywatny" (którego nikomu nie dajesz) i "klucz publiczny" (który wgrywasz na serwer). Serwer wpuszcza Cię automatycznie, bo rozpoznaje Twój klucz. To wielokrotnie bezpieczniejsze niż najtrudniejsze hasło.

---

### Rozszerzenie 2: Nginx w praktyce – coś więcej niż Reverse Proxy (25 min)

*(Uzupełnienie sekcji 5 i 6)*

Nginx to potężny kombajn. W architekturze produkcyjnej pełni zazwyczaj 3 role naraz:

1. **Reverse Proxy** (kieruje ruch "wewnętrzny" do Django).
2. **Web Server** (samodzielnie, błyskawicznie serwuje pliki CSS/JS/Media, odciążając Django).
3. **Strażnik bezpieczeństwa** (zarządza certyfikatami SSL, odrzuca złośliwy ruch z dziwnych adresów URL).

**Gdzie żyje plik `nginx.conf` i jak trafia do Dockera?**
Ten plik tworzysz w kodzie swojego projektu (na swoim laptopie). Kiedy uruchamiasz Dockera na serwerze, **nie musisz budować nowego obrazu Nginxa**. Używa się tzw. **Wolumenów (Volumes)** – mapujesz plik z Twojego serwera do wnętrza kontenera.

**Przykładowy, uproszczony `nginx.conf`:**

```nginx
upstream hello_django {
    # Nginx wie, że aplikacja Django nasłuchuje w kontenerze o nazwie "web" na porcie 8000
    server web:8000;
}

server {
    listen 80; # Nasłuchuj na domyślnym porcie HTTP

    # 1. Zlecenia po pliki statyczne - Nginx robi to SAM!
    location /static/ {
        alias /usr/src/app/staticfiles/; # Ścieżka wewnątrz kontenera Nginx
    }

    # 2. Zlecenia po media (zdjęcia userów) - Nginx robi to SAM!
    location /media/ {
        alias /usr/src/app/media/;
    }

    # 3. Reszta ruchu (np. /api/, /login/) - Przekaż do Django
    location / {
        proxy_pass http://hello_django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

```

`hello_django` w podanym przykładzie to **dowolna, wymyślona przeze mnie nazwa własna (etykieta)**, która działa jak wskaźnik lub alias w konfiguracji Nginxa.

Spójrzmy jeszcze raz na ten kluczowy fragment konfiguracji:

```nginx
# 1. Definicja grupy serwerów (nadajemy jej nazwę "hello_django")
upstream hello_django {
    server web:8000; 
}

server {
    ...
    location / {
        # 2. Użycie tej nazwy
        proxy_pass http://hello_django;
    }
}

```

Oto co dokładnie się tu dzieje, krok po kroku:

### 1. Dyrektywa `upstream` (Grupowanie)

Sekcja `upstream hello_django` mówi Nginxowi: *"Słuchaj, pod nazwą `hello_django` kryje się nasza główna aplikacja. Fizycznie znajduje się ona pod adresem `web:8000`"*.

(Zauważ, że `web` to po prostu nazwa kontenera z naszego pliku `docker-compose.yml`. Nginx wewnątrz sieci Dockera potrafi "przetłumaczyć" tę nazwę na konkretny adres IP kontenera).

### 2. Przekazanie ruchu (`proxy_pass`)

Kiedy przychodzi zwykły użytkownik i chce wejść na stronę główną, trafia do bloku `location /`. Wtedy dyrektywa `proxy_pass http://hello_django;` mówi Nginxowi: *"Wszystko, co tu wpada, przekaż do grupy serwerów, którą nazwaliśmy `hello_django`"*.

### Dlaczego tak się to robi, a nie podaje adresu bezpośrednio? (Load Balancing)

Mógłbyś zapytać: *Dlaczego po prostu nie wpisać `proxy_pass http://web:8000;` od razu w bloku location?*

Mógłbyś! To by zadziałało. Ale używanie bloku `upstream` to **dobra praktyka DevOps**, ponieważ przygotowuje Twoją aplikację na **skalowanie (Load Balancing)**.

Wyobraź sobie, że Twoja aplikacja staje się super popularna i jeden kontener z Django nie wyrabia. Uruchamiasz więc trzy kontenery z Django. Z blokiem `upstream` sprawa jest banalnie prosta:

```nginx
upstream hello_django {
    server web1:8000;
    server web2:8000;
    server web3:8000;
}

```

Nginx jest tak mądry, że widząc taką konfigurację, automatycznie zacznie rozdzielać ruch po równo: pierwszego użytkownika wyśle do `web1`, drugiego do `web2`, trzeciego do `web3` (to tzw. algorytm Round-Robin). Nie musisz zmieniać niczego w głównej konfiguracji ścieżek!

---

### Rozszerzenie 3: Samonaprawiająca się aplikacja (Restart i Healthcheck w Dockerze) (20 min)

*(Uzupełnienie sekcji 6)*

**Problem:** Aplikacja na produkcji nagle rzuca błędem krytycznym (np. brak pamięci RAM) i proces Pythona "umiera". Jak zrestartować serwis w przypadku awarii? O 3 w nocy nie obudzisz się, żeby wpisać `docker restart web`.

**Rozwiązanie:** Nie robisz tego ręcznie. Zrzucasz odpowiedzialność na Dockera (tzw. mechanizmy orkiestracji/nadzorcy).

Docker potrafi sam monitorować stan kontenera i reagować.

* **`restart: unless-stopped`** – mówi Dockerowi: "Jeśli kontener padnie, podnieś go natychmiast ponownie. Rób to zawsze, chyba że ja ręcznie wpiszę `docker stop`".
* **`healthcheck`** – Docker potrafi co np. 30 sekund pukać pod konkretny adres w Twoim Django. Jeśli Django nie odpowie 3 razy z rzędu – Docker uznaje, że aplikacja się zawiesiła i sam ją restartuje.

**Jak to zapisać w `docker-compose.yml`? (Integracja z Nginxem i Healthcheckiem)**

```yaml
version: '3.8'

services:
  web:
    build: .
    # Uruchom Gunicorna zamiast runserver!
    command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
    restart: unless-stopped  # <--- Automatyczny restart po awarii!
    env_file:
      - .env
    depends_on:
      - db
    # Definicja "pulsu" aplikacji
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health/"]
      interval: 30s    # Sprawdzaj co 30 sekund
      timeout: 10s     # Czekaj max 10 sekund na odpowiedź
      retries: 3       # Po 3 nieudanych próbach uznaj kontener za zepsuty (unhealthy)

  db:
    image: postgres:16
    restart: unless-stopped # <--- Baza też wstaje sama
    env_file:
      - .env

  nginx:
    image: nginx:latest
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      # Mapowanie: [plik_na_gospodarzu] : [ścieżka_w_kontenerze]
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf
      # Nginx musi mieć dostęp do plików statycznych wygenerowanych przez Django
      - static_volume:/usr/src/app/staticfiles
      - media_volume:/usr/src/app/media
    depends_on:
      - web

volumes:
  static_volume:
  media_volume:

```

---

### Rozszerzenie 4: Prometheus i Grafana – oczy i uszy DevOpsa (25 min)

*(Uzupełnienie sekcji 7)*

Mówiliśmy, że potrzebujemy monitoringu, ale czym on fizycznie jest w architekturze?

**Po co nam one?**

* **Prometheus:** To narzędzie przypomina ankietera. Co kilkanaście sekund puka do Twojej aplikacji (zazwyczaj na ukryty endpoint `/metrics`) i "zbiera" statystyki: ile było requestów? Ile zapytań do bazy? Ile błędów 500? Trzyma te dane w postaci zoptymalizowanych szeregów czasowych.
* **Grafana:** Prometheus ma surowe, brzydkie dane liczbowe. Grafana to aplikacja webowa podłączona do Prometheusa, która zamienia te nudne liczby w piękne, kolorowe wykresy (dashboardy), na które patrzysz na ekranie telewizora w biurze. Posiada też potężny system alertów (np. "jeśli zużycie CPU przekroczy 90% przez 5 minut – wyślij wiadomość na Slacka").

**Jak przygotować na to Django?**
Instalujesz bibliotekę, np. `django-prometheus`. Dodaje ona automatycznie endpoint `/metrics`, w którym wystawia tysiące statystyk gotowych do "połknięcia" przez Prometheusa.

**Jak uruchomić ten tandem?**
To kolejne "klocki" w naszym pliku `docker-compose.yml`. Działają jako osobne usługi!

```yaml
  prometheus:
    image: prom/prometheus
    restart: unless-stopped
    ports:
      - "9090:9090"
    volumes:
      # Wgrywamy plik konfiguracyjny (mówimy Prometheusowi gdzie jest Django)
      - ./prometheus.yml:/etc/prometheus/prometheus.yml 

  grafana:
    image: grafana/grafana
    restart: unless-stopped
    ports:
      - "3000:3000"
    depends_on:
      - prometheus

```

### 1. Prometheus (`prom/prometheus`)

* **Co dostajesz gotowe:** Potężny silnik bazy danych szeregów czasowych oraz mechanizm "odpytywania" (scraper).
* **Czego brakuje:** Prometheus nie wie, że Twoja aplikacja Django w ogóle istnieje, ani pod jakim adresem ma szukać jej metryk.
* **Jak go konfigurujesz?**
Tworzysz w swoim projekcie (obok `docker-compose.yml`) mały plik tekstowy, np. `prometheus.yml`. Wpisujesz w nim:

```yaml
global:
  scrape_interval: 15s # Pytaj o statystyki co 15 sekund

scrape_configs:
  - job_name: 'django_app'
    static_configs:
      - targets: ['web:8000'] # Nazwa kontenera Django i jego port

```

Następnie w `docker-compose.yml` używasz mechanizmu **wolumenów** (Volumes), aby wstrzyknąć ten plik do gotowego kontenera:

```yaml
volumes:
  - ./prometheus.yml:/etc/prometheus/prometheus.yml

```

Dzięki temu odpalasz gotowy program z Docker Hub, ale z *Twoimi* wytycznymi.

### 2. Grafana (`grafana/grafana`)

* **Co dostajesz gotowe:** Ogromną aplikację webową z systemem logowania, zarządzania uprawnieniami i silnikiem do rysowania wykresów.
* **Czego brakuje:** Grafana po uruchomieniu jest pusta. Nie ma wykresów ani nie wie, skąd brać dane.
* **Jak ją konfigurujesz?**
W przypadku Grafany często robi się to po prostu przez przeglądarkę (lub przez specjalne pliki konfiguracyjne dla zaawansowanych).

1. Uruchamiasz `docker-compose up`.
2. Wchodzisz na `localhost:3000` i logujesz się (domyślnie admin/admin).
3. Klikasz **Add Data Source**, wybierasz "Prometheus" i wpisujesz adres: `http://prometheus:9090` (tak, kontenery znają się po nazwach!).
4. Zamiast rysować wykresy ręcznie, wchodzisz na stronę Grafany, znajdujesz gotowy "Dashboard" dla Django (są ich tam tysiące tworzone przez społeczność), kopiujesz jego numer ID i klikasz **Import**.


## S3

---

### Złe podejście: Django jako pośrednik (Proxy)

Gdyby Django pobierało plik z S3 i wysyłało go do użytkownika, przepływ wyglądałby tak:

`Przeglądarka ➔ Nginx ➔ Gunicorn (Django) ➔ Zapytanie do S3 ➔ Django czeka na plik ➔ Django wysyła plik ➔ Przeglądarka`

**Dlaczego to katastrofa na produkcji?**
Pamiętasz nasze workery Gunicorna? Jeśli masz 3 workery, a 3 użytkowników zacznie pobierać z Twojej strony duże, 100-megabajtowe pliki wideo, to przez cały czas trwania pobierania (np. kilkanaście sekund) **wszystkie Twoje workery są zablokowane**. Twój serwer staje się "zajęty", mimo że procesor nic nie liczy — po prostu bezmyślnie przerzuca bajty z S3 do użytkownika. Czwarty użytkownik, który chce tylko wejść na stronę główną, dostanie błąd lub będzie musiał czekać.

---

### Dobre podejście: Bezpośrednie połączenie (Przeglądarka ➔ S3)

W architekturze chmurowej Django służy wyłącznie jako "informator". Mówi przeglądarce: *"Nie mam tego pliku, ale wiem, gdzie on leży. Idź sobie go weź stamtąd"*.

Prawidłowy, produkcyjny przepływ wygląda tak:

1. **Przeglądarka** prosi Django o profil użytkownika (HTML lub JSON przez API).
2. **Django** pyta bazę PostgreSQL o dane użytkownika. W bazie (w kolumnie np. `avatar_path`) zapisany jest tylko krótki tekst: `avatars/user123.jpg`.
3. **Django** (korzystając z biblioteki) łączy ten tekst z głównym adresem Twojego S3 i buduje pełny URL: `[https://twoj-bucket.s3.amazonaws.com/media/avatars/user123.jpg](https://twoj-bucket.s3.amazonaws.com/media/avatars/user123.jpg)`.
4. **Django zwraca do przeglądarki** sam tekst (kod HTML lub JSON), w którym znajduje się ten link.
5. **Przeglądarka (Front-end)** czyta ten kod, widzi tag `<img src="https://twoj-bucket...">` i **sama nawiązuje bezpośrednie połączenie z AWS S3**, aby pobrać obrazek.

W tym scenariuszu Django wykonało ułamek sekundy pracy (zbudowanie tekstu z adresem), worker Gunicorna jest od razu wolny dla kolejnego użytkownika, a ciężar wysłania gigabajtów danych bierze na siebie potężna infrastruktura Amazonu.

---

### Jak to wygląda w kodzie Django?

Na produkcji używa się do tego standardowej biblioteki **`django-storages`** (oraz `boto3` do komunikacji z AWS).

Kiedy w `settings.py` ustawisz S3 jako domyślny magazyn plików:

```python
# settings.py
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'moj-super-bucket'

```

Magia dzieje się pod spodem. Kiedy w szablonie HTML (lub w serializerze Django REST Framework) wywołasz:

```django
<img src="{{ user.avatar.url }}">

```

Django nie szuka już tego pliku na lokalnym dysku serwera. Biblioteka `django-storages` nadpisuje metodę `.url` i "w locie" generuje link do chmury. Twój kod (widoki, modele) pozostaje dokładnie taki sam, jak podczas pracy lokalnej!

---

> **Ważne podsumowanie:**
> Z perspektywy architektury zdejmujemy z serwera aplikacji (Django) odpowiedzialność za tzw. *I/O (Input/Output)* dla dużych plików. Serwer ma przetwarzać logikę tak szybko, jak to możliwe, i przekierowywać ruch po pliki do rozwiązań chmurowych.

Oto kompletny, minimalny przykład spięcia Django z AWS S3. Co najważniejsze – po skonfigurowaniu tego w ustawieniach, **nie musisz zmieniać ani jednej linijki w swoich modelach czy widokach**.

### Krok 1: Instalacja bibliotek

W swoim środowisku (lub w pliku `requirements.txt` dla Dockera) musisz zainstalować dwie paczki:

```bash
pip install boto3 django-storages

```

* `boto3` – to oficjalna biblioteka Pythona do komunikacji z AWS.
* `django-storages` – to biblioteka, która tłumaczy wbudowany system plików Django na komendy zrozumiałe dla `boto3`.

### Krok 2: Konfiguracja w `settings.py`

Dodaj `storages` do zainstalowanych aplikacji i skonfiguruj połączenie z użyciem zmiennych środowiskowych (żeby nie trzymać kluczy w kodzie!):

```python
import os

INSTALLED_APPS = [
    # ... inne aplikacje ...
    'storages',
]

# 1. Poświadczenia do konta AWS (pobierane z pliku .env)
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

# 2. Region Twojego bucketu (np. eu-central-1 dla Frankfurtu)
AWS_S3_REGION_NAME = 'eu-central-1'

# 3. Zabezpieczenie przed nadpisywaniem plików o tej samej nazwie
# Jeśli dwóch userów wgra 'avatar.jpg', Django z automatu nazwie drugi plik 'avatar_XYZ.jpg'
AWS_S3_FILE_OVERWRITE = False

# 4. Nowe buckety S3 domyślnie blokują publiczne ACL. Ta opcja to respektuje.
AWS_DEFAULT_ACL = None 

# 5. KLUCZOWY MOMENT: Mówimy Django, żeby od teraz wysyłał media do S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

```

### Krok 3: Jak to działa w kodzie (Modele)

Magia tego rozwiązania polega na tym, że Twój kod biznesowy pozostaje bez zmian. Nadal używasz standardowych pól:

```python
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    # Kiedy użytkownik wgra plik w formularzu, Django automatycznie wyśle go na S3!
    avatar = models.ImageField(upload_to='avatars/')

```

A w szablonie HTML wywołujesz to dokładnie tak samo jak lokalnie:

```django
<!-- Django samo wygeneruje długi link do AWS S3, np: -->
<!-- https://moj-bucket.s3.eu-central-1.amazonaws.com/avatars/foto.jpg -->
<img src="{{ profile.avatar.url }}" alt="Avatar">

```

### O czym warto pamiętać (kontekst DevOps)?

Dzięki tej konfiguracji Twój kontener Docker stał się **bezstanowy (stateless)**. Możesz go w każdej chwili usunąć, zrestartować lub uruchomić na 5 różnych serwerach jednocześnie – pliki użytkowników są bezpieczne w chmurze AWS, a sama aplikacja Django to już tylko "silnik" bez bagażu w postaci plików.


S3 to po prostu usługa typu **Object Storage** (magazyn obiektowy). AWS była pierwszą firmą, która to spopularyzowała, ale sam protokół przesyłania danych (tzw. **S3 API**) stał się branżowym standardem.

Oznacza to, że możesz zastąpić AWS S3 własnym serwerem lub inną chmurą, **nie zmieniając ani jednej linijki w kodzie Django** — zmieniasz tylko adres serwera (tzw. `endpoint_url`) w pliku `.env`!

Oto najlepsze alternatywy, podzielone na dwie kategorie:

---

## 1. Własny kontener na serwerze (Self-Hosted)

Jeśli masz własny serwer (np. z macierzą RAID dla bezpieczeństwa danych) i nie chcesz płacić Amazonowi, uruchamiasz system Open Source.

### 🥇 MinIO (Król rozwiązań Self-Hosted)

**Co to jest?** MinIO to mały, niesamowicie szybki program, który uruchamiasz jako **zwykły kontener w Dockerze**. Zmienia Twój lokalny dysk (lub macierz RAID) w prywatną chmurę S3.

* **Zalety:** Jest w 100% kompatybilne z AWS S3 API. Ma piękny panel graficzny w przeglądarce, gdzie możesz przeglądać pliki.
* **Jak to spiąć z Dockerem?** Dodajesz MinIO do swojego `docker-compose.yml`:

```yaml
services:
  minio:
    image: minio/minio
    ports:
      - "9000:9000"   # Port dla API (S3)
      - "9001:9001"   # Panel administracyjny w przeglądarce
    environment:
      MINIO_ROOT_USER: "admin"
      MINIO_ROOT_PASSWORD: "SuperSecretPassword123"
    volumes:
      # Podpinasz folder ze swojego serwera/RAIDu do kontenera!
      - /mnt/storage_raid/minio_data:/data 
    command: server /data --console-address ":9001"

```

* **Zmiana w Django:** W `settings.py` dodajesz tylko jedną linijkę mówiącą, gdzie szukać S3 zamiast w AWS:

```python
# Zamiast do serwerów Amazona, wysyłaj pliki do lokalnego MinIO!
AWS_S3_ENDPOINT_URL = 'http://minio:9000' 

```