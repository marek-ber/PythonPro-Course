# Kurs: Docker w aplikacjach Django

**Czas trwania:** 4–5 godzin  
**Wymagania wstępne:** Znajomość języka Python, frameworka Django, Django REST Framework oraz podstawowych zapytań SQL / PostgreSQL.

---

## Blok 1: Wprowadzenie do konteneryzacji i Dockera (30–40 min)

### 1.1 Problem "Works on my machine"
W tradycyjnym wytwarzaniu oprogramowania częstym problemem jest rozbieżność środowisk uruchomieniowych:
* Różne wersje interpretera Python zainstalowane lokalnie u programistów.
* Brakujące biblioteki systemowe C (np. wymagane przez `psycopg2` czy `Pillow`).
* Różnice w konfiguracji zmiennych środowiskowych oraz systemów operacyjnych (macOS vs Linux vs Windows).

Konteneryzacja rozwiązuje ten problem, pakując aplikację wraz z jej pełnym środowiskiem uruchomieniowym (zależności systemowe, interpreter, biblioteki Python) w spójną, odizolowaną jednostkę.

### 1.2 Kluczowe pojęcia Dockera
* **Obraz (Docker Image):** Niepodlegający zmianom (immutable) szablon zawierający instrukcje tworzenia kontenera. Składa się z warstw i zawiera kod źródłowy, system plików oraz konfigurację.
* **Kontener (Docker Container):** Uruchomiona instancja obrazu. Jest odizolowanym procesem działającym w przestrzeni użytkownika na hoście.
* **Docker Engine:** Usługa systemowa (daemon `dockerd`) zarządzająca obrazami, kontenerami, sieciami i wolumenami.
* **Docker Hub:** Publiczny/prywatny rejestr obrazów, z którego pobierane są podstawowe obrazy (np. `python`, `postgres`, `redis`).
* **Warstwy obrazu (Image Layers):** Każda instrukcja w pliku `Dockerfile` tworzy nową warstwę. Warstwy są buforowane (cached), co przyspiesza ponowne budowanie obrazu.

### 1.3 Różnice: Docker vs Maszyna Wirtualna (VM)

```
+---------------------------------+     +---------------------------------+
|   Aplikacja A   |   Aplikacja B |     |   Aplikacja A   |   Aplikacja B |
+---------------------------------+     +---------------------------------+
|   Kontener A    |   Kontener B  |     | Guest OS (Linux)| Guest OS (Win)  |
+---------------------------------+     +---------------------------------+
|          Docker Engine          |     |           Hypervisor            |
+---------------------------------+     +---------------------------------+
|          Host OS (Linux)        |     |             Host OS             |
+---------------------------------+     +---------------------------------+
|            Hardware             |     |            Hardware             |
+---------------------------------+     +---------------------------------+
          DOCKER (Kontenery)                     MASZYNA WIRTUALNA
```

* **Maszyna wirtualna:** Emuluje sprzęt i wymaga pełnego systemu operacyjnego dla każdej instancji (Guest OS). Wynik: wysokie zużycie RAM/CPU i długi czas startu.
* **Kontener Docker:** Współdzieli kernel (jądro) systemu operacyjnego z hostem. Izoluje procesy za pomocą mechanizmów kernela Linux (`namespaces` i `cgroups`). Wynik: lekkość, szybki start (sekundy) i niskie zużycie zasobów.

### 1.4 Przepływ pracy (Workflow)

```
+------------------+         docker build         +------------------+
|  Laptop Dev-a    | ---------------------------> |   Obraz Docker   |
|  (Kod + Dockerfile)                             | (django-app:v1)  |
+------------------+                              +------------------+
                                                           |
                                                      docker push
                                                           v
+------------------+          docker run          +------------------+
| Serwer Produkcji | <--------------------------- |    Docker Hub    |
| (Uruchomiony    |                              |   (Rejestr)      |
|  kontener)       |                              +------------------+
+------------------+
```

### Zadanie praktyczne 1
1. Zweryfikuj poprawność instalacji Dockera w systemie, uruchamiając komendę:
   ```bash
   docker --version
   docker run hello-world
   ```
2. Przeanalizuj wyjście komendy `docker run hello-world` i zidentyfikuj etapy: pobranie obrazu z Docker Hub, utworzenie kontenera, wykonanie procesu i jego zakończenie.

---

## Blok 2: Pierwszy kontener Django (60 min)

### 2.1 Struktura katalogów minimalnego projektu
Utwórz katalog projektu `django-docker-demo` o następującej strukturze:

```
django-docker-demo/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/
│   ├── __init__.py
│   ├── views.py
│   └── urls.py
├── Dockerfile
├── manage.py
└── requirements.txt
```

### 2.2 Zawartość plików konfiguracyjnych

**`requirements.txt`**
```text
Django>=5.0,<5.1
gunicorn>=21.2.0
```

**`config/settings.py`** (istotne fragmenty):
```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'insecure-default-key-change-in-prod')
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'pl-pl'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

**`app/views.py`**
```python
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok", "message": "Aplikacja Django działa w kontenerze!"})
```

**`app/urls.py`**
```python
from django.urls import path
from .views import health_check

urlpatterns = [
    path('health/', health_check, name='health_check'),
]
```

**`config/urls.py`**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
```

### 2.3 Minimalny Dockerfile
Utwórz plik `Dockerfile` w głównym katalogu projektu:

```dockerfile
# 1. Wybór obrazu bazowego z oficjalnym Pythonem 3.12 w wersji slim (odchudzony Debian)
FROM python:3.12-slim

# 2. Ustawienie katalogu roboczego wewnątrz kontenera
WORKDIR /app

# 3. Kopiowanie pliku zależności jako osobny krok (optymalizacja cache Dockera)
COPY requirements.txt .

# 4. Instalacja zależności Python bez tworzenia pamięci podręcznej pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiowanie pozostałego kodu źródłowego aplikacji do /app
COPY . .

# 6. Deklaracja portu, na którym nasłuchuje aplikacja (informacja dla użytkownika/usług)
EXPOSE 8000

# 7. Domyślna komenda uruchamiająca serwer deweloperski Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### Szczegółowe omówienie instrukcji Dockerfile:
* **`FROM python:3.12-slim`**: Określa bazowy obraz. Wersja `slim` wyklucza zbędne pakiety systemowe, zmniejszając rozmiar obrazu z ~1GB do ~150MB.
* **`WORKDIR /app`**: Tworzy katalog `/app` wewnątrz kontenera i ustawia go jako bieżący katalog dla kolejnych instrukcji.
* **`COPY requirements.txt .`**: Kopiuje plik z hosta do obrazu. Kopiowanie `requirements.txt` przed resztą kodu umożliwia ponowne wykorzystanie buforowanej warstwy `RUN pip install`, jeśli zależności się nie zmieniły.
* **`RUN pip install --no-cache-dir -r requirements.txt`**: Wykonuje komendę w trakcie budowania obrazu. Flaga `--no-cache-dir` redukuje rozmiar obrazu.
* **`COPY . .`**: Kopiuje całą zawartość katalogu roboczego hosta do `/app` w obrazie.
* **`EXPOSE 8000`**: Dokumentuje port. Nie przekierowuje go automatycznie na hosta (wymaga to flagi `-p` podczas `docker run`).
* **`CMD [...]`**: Określa domyślne polecenie wykonywane podczas startu kontenera. Używamy tablicy JSON (forma exec). Parametr `0.0.0.0:8000` jest krytyczny – wymusza nasłuchiwanie na wszystkich interfejsach sieciowych kontenera, a nie tylko na wewnętrznym `127.0.0.1`.

### 2.4 Budowanie i uruchamianie kontenera

Budowanie obrazu o nazwie `django-demo`:
```bash
docker build -t django-demo:v1 .
```

Uruchomienie kontenera z przekierowaniem portów:
```bash
docker run -d -p 8000:8000 --name moj_django_kontener django-demo:v1
```

Opcje polecenia `docker run`:
* `-d` (detached): Uruchamia kontener w tle.
* `-p 8000:8000`: Przekierowuje port 8000 z hosta na port 8000 kontenera (`port_hosta:port_kontenera`).
* `--name moj_django_kontener`: Nadaje nazwę kontenerowi.

Weryfikacja działania:
Otwórz przeglądarkę lub wykonaj komendę:
```bash
curl http://localhost:8000/health/
```

### Zadanie practical 2
1. Zbuduj obraz `django-demo:v1`.
2. Uruchom kontener na porcie hosta `8080` zamiennie z `8000` (`-p 8080:8000`).
3. Sprawdź odpowiedzi pod adresem `http://localhost:8080/health/`.
4. Zatrzymaj i usuń kontener za pomocą komend:
   ```bash
   docker stop moj_django_kontener
   docker rm moj_django_kontener
   ```

---

## Blok 3: Docker Compose i architektura wielokontenerowa (60–90 min)

### 3.1 Architektura docelowa aplikacji
W realnych warunkach produkcyjnych aplikacja Django nie działa w izolacji. Wymaga bazy danych, serwera pamięci podręcznej oraz serwera HTTP/Reverse Proxy.

```
                          Przeglądarka / Klient HTTP
                                      |
                                      v (Port 80)
                         +--------------------------+
                         |      Kontener Nginx      |
                         |     (Reverse Proxy)      |
                         +--------------------------+
                                      |
                                      v (Port 8000)
                         +--------------------------+
                         |  Kontener Django (API)   |
                         |   (WSGI / Gunicorn)      |
                         +--------------------------+
                           /                      \
                          /                        \
                         v                          v
    +--------------------------+        +--------------------------+
    |    Kontener PostgreSQL   |        |     Kontener Redis       |
    |      (Baza Danych)       |        |     (Cache / Session)    |
    +--------------------------+        +--------------------------+
```

### 3.2 Czym jest Docker Compose?
Docker Compose to narzędzie do definiowania i uruchamiania wielokontenerowych aplikacji Docker za pomocą deklaratywnego pliku YAML (`docker-compose.yml`). Umożliwia uruchomienie całego stosu technologicznego jedną komendą.

### 3.3 Definicja usług w `docker-compose.yml`

Utwórz plik `docker-compose.yml` w katalogu głównym:

```yaml
version: '3.8'

services:
  backend:
    build:
      # pliki używane do budowy obrazu
      context: .
      dockerfile: Dockerfile
    container_name: django_backend
    # komenda uruchamiajaca aplikacje
    command: python manage.py runserver 0.0.0.0:8000
    volumes: # wspóldzielenie katalogu z hostem
      - .:/app
    ports: # mapowanie portów
      - "8000:8000"
    environment: # zmienne srodowiskowe
      - DEBUG=1
      - SECRET_KEY=django-insecure-key
      - DB_ENGINE=django.db.backends.postgresql
      - DB_NAME=postgres
      - DB_USER=postgres
      - DB_PASSWORD=postgres
      - DB_HOST=database
      - DB_PORT=5432
      - REDIS_URL=redis://redis:6379/1
    depends_on:
      - database
      - redis
    networks:
      - app_network

  database:
    image: postgres:16-alpine
    container_name: postgres_db
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
      # lokalizacja danych w
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app_network

  redis:
    image: redis:7-alpine
    container_name: redis_cache
    ports:
      - "6379:6379"
    networks:
      - app_network

networks:
  app_network:
    driver: bridge

volumes:
  postgres_data:
```

### 3.4 Komunikacja sieciowa między kontenerami
Docker Compose automatycznie tworzy dedykowaną sieć typu `bridge` dla zdefiniowanych usług (w tym przypadku `app_network`).

Kluczowe zasady sieciowe:
1. **Wewnętrzny DNS:** Docker Engine uruchamia wbudowany serwer DNS. Nazwy serwisu z pliku YAML (`backend`, `database`, `redis`) stają się nazwami hostów (IP) wewnątrz sieci Dockera.
2. **Izolacja:** Kontenery w tej samej sieci mogą komunikować się na wszystkich portach bezpośrednio, używając nazwy usługi (np. `database:5432`).
3. **Mapowanie portów:** Porty nie muszą być mapowane na hosta, aby kontenery komunikowały się między sobą. Mapowanie `ports:` w usłudze `database` nie jest konieczne dla Django, ale przydaje się, jeśli chcesz połączyć się z bazą lokalnym klientem (np. DBeaver).

### Zadanie praktyczne 3
1. Uruchom zestaw kontenerów w trybie pierwszoplanowym:
   ```bash
   docker compose up
   ```
2. Zaobserwuj logi generowane jednocześnie przez serwisy `backend`, `database` i `redis`.
3. Zatrzymaj zestaw kombinacją klawiszy `Ctrl + C`.

---

## Blok 4: Baza danych PostgreSQL i trwałość danych (Volumes) (45 min)

### 4.1 Konfiguracja Django do obsługi PostgreSQL
Zaktualizuj `requirements.txt`:
```text
Django>=5.0,<5.1
psycopg2-binary>=2.9.9
gunicorn>=21.2.0
django-redis>=5.4.0
```

Zaktualizuj `DATABASES` w `config/settings.py`:
```python
import os

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
        'HOST': os.getenv('DB_HOST', 'database'),  # Nazwa serwisu z docker-compose.yml
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

### 4.2 Dlaczego `localhost` nie działa w konfiguracji bazy danych?

Błąd powszechnie popełniany przez początkujących:
```python
# BŁĘDNA KONFIGURACJA W DOCKERZE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost', # LUB '127.0.0.1'
        ...
    }
}
```

**Przyczyna błędu:**  
Wewnątrz kontenera `backend` adres `localhost` (127.0.0.1) odnosi się do pętli zwrotnej (loopback) **tego konkretnego kontenera**. Baza danych PostgreSQL nie działa w tym kontenerze, lecz w osobnym kontenerze `database`. Prawidłowy adres to nazwa usługi `database`, która jest rozstrzygana przez wewnętrzny DNS Dockera na adres IP kontenera bazy.

### 4.3 Trwałość danych (Docker Volumes)

#### Problem braku stanowości (Statelessness):
Kontenery są z założenia ulotne (ephemeral). usunięcie kontenera komendą `docker rm postgres_db` powoduje bezpowrotną utratę wszystkich danych zapisanych w jego wewnętrznym systemie plików (w tym bazy danych PostgreSQL zlokalizowanej w `/var/lib/postgresql/data`).

#### Rozwiązanie: Named Volumes (Wolumeny nazwane)
Wolumeny to katalogi zarządzane bezpośrednio przez Docker Engine na hoście, montowane do wybranego punktu wewnątrz kontenera.

```yaml
services:
  database:
    image: postgres:16-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:  # Zarządzany wolumen nazwany
```

Dzięki tej konfiguracji, usunięcie i ponowne utworzenie kontenera bazy danych nie niszczy danych – nowy kontener montuje istniejący wolumen `postgres_data`.

### Zadanie praktyczne 4
1. Uruchom serwisy: `docker compose up -d`.
2. Wykonaj migracje bazy danych w kontenerze:
   ```bash
   docker compose exec backend python manage.py migrate
   ```
3. Usuń kontenery komendą: `docker compose down`.
4. Uruchom ponownie `docker compose up -d` i sprawdź, czy migracje nie muszą być wykonywane powtórnie (dane w wolumenie przetrwały).

---

## Blok 5: Zmienne środowiskowe i bezpieczeństwo (45 min)

### 5.1 Zarządzanie konfiguracją i sekretami
Przechowywanie kluczy API, haseł bazy danych czy parametrów `SECRET_KEY` bezpośrednio w kodzie źródłowym (`settings.py`) jest poważnym błędem bezpieczeństwa. Konfiguracja musi być odseparowana od kodu zgodnie z metodologią *Twelve-Factor App*.

### 5.2 Tworzenie pliku `.env`

Utwórz plik `.env` w katalogu głównym projektu:

```env
DEBUG=1
SECRET_KEY=c89f3a1d6e8b4c7a2e5f1g9h0i3j6k9l2m5n8o1p4q7r0s3t6u9v2w5x8y1z
DB_ENGINE=django.db.backends.postgresql
DB_NAME=blog_db
DB_USER=blog_user
DB_PASSWORD=secure_postgres_password_123
DB_HOST=database
DB_PORT=5432
REDIS_URL=redis://redis:6379/1
```

Dodaj `.env` do pliku `.gitignore`:
```text
*.pyc
__pycache__/
db.sqlite3
.env
.venv/
```

### 5.3 Integracja pliku `.env` z Docker Compose

Zaktualizuj `docker-compose.yml`, zastępując twardo wpisane wartości w `environment:` sekcją `env_file:`:

```yaml
version: '3.8'

services:
  backend:
    build: .
    container_name: django_backend
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - database
      - redis
    networks:
      - app_network

  database:
    image: postgres:16-alpine
    container_name: postgres_db
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app_network

  redis:
    image: redis:7-alpine
    container_name: redis_cache
    networks:
      - app_network

networks:
  app_network:
    driver: bridge

volumes:
  postgres_data:
```

### Zadanie practical 5
1. Utwórz plik `.env` z własnymi wartościami haseł.
2. Zaktualizuj plik `docker-compose.yml` przy użyciu zmiennych z `.env`.
3. Przetestuj poprawność wczytywania zmiennych uruchamiając:
   ```bash
   docker compose config
   ```
   Komenda ta wyświetli scaloną, ostateczną strukturę konfiguracji.

---

## Blok 6: Cache z wykorzystaniem Redis (45 min)

### 6.1 Konfiguracja `django-redis` w Django

Dodaj konfigurację pamięci podręcznej do `config/settings.py`:

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://redis:6379/1"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

### 6.2 Przykład użycia Cache API w Django

Zaktualizuj `app/views.py`, dodając symulację kosztownej operacji bazodanowej / obliczeniowej z buforowaniem w Redis:

```python
import time
from django.http import JsonResponse
from django.core.cache import cache

def heavy_calculation_view(request):
    cache_key = "heavy_calc_result"
    
    # 1. Próba pobrania danych z pamięci podręcznej Redis
    cached_data = cache.get(cache_key)
    
    if cached_data:
        return JsonResponse({
            "source": "cache",
            "data": cached_data
        })
    
    # 2. Symulacja długotrwałej operacji (np. skomplikowane zapytanie SQL)
    time.sleep(2)
    result = {"user_count": 1050, "active_sessions": 42}
    
    # 3. Zapis wyniku do Redis z czasem życia (TTL) 60 sekund
    cache.set(cache_key, result, timeout=60)
    
    return JsonResponse({
        "source": "database_calculation",
        "data": result
    })
```

Dodaj ścieżkę w `app/urls.py`:
```python
from django.urls import path
from .views import health_check, heavy_calculation_view

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('heavy-calc/', heavy_calculation_view, name='heavy_calc'),
]
```

### Zadanie praktyczne 6
1. Uruchom aplikację: `docker compose up -d`.
2. Wykonaj zapytanie HTTP pod adresem `http://localhost:8000/heavy-calc/`. Pierwsze zapytanie zajmie > 2 sekundy (źródło: `database_calculation`).
3. Wykonaj zapytanie powtórnie. Odpowiedź powróci natychmiast (źródło: `cache`).
4. Zweryfikuj zawartość bazy Redis wewnątrz kontenera:
   ```bash
   docker compose exec redis redis-cli KEYS "*"
   ```

---

## Blok 7: Produkcyjny sposób uruchomienia Django (45 min)

### 7.1 Development vs Production

| Cecha                          | Środowisko Deweloperskie           | Środowisko Produkcyjne             |
| :----------------------------- | :--------------------------------- | :--------------------------------- |
| **Serwer WSGI**                | `manage.py runserver`              | `Gunicorn` / `uWSGI`               |
| **Obsługa plików statycznych** | Serwer deweloperski Django         | `Nginx` / CDN                      |
| **Przeznaczenie**              | Debugowanie, auto-reload           | Wysoka wydajność, wielowątkowość   |
| **Obsługa awarii**             | Brak automatycznego restartu       | Autorestart kontenera/procesu      |
| **Bezpieczeństwo**             | `DEBUG = True`, wygenerowane błędy | `DEBUG = False`, maskowanie błędów |

### 7.2 Architektura produkcyjna z Nginx i Gunicorn

```
[ Klient / Internet ] 
         |
         v (Port 80)
+-------------------------------------------------------+
| Nginx (Kontener)                                      |
| - Serwuje pliki statyczne (/static/) bezpośrednio    |
| - Przekazuje ruch dynamiczny do Gunicorna             |
+-------------------------------------------------------+
         |
         v (Proxy do gunicorn:8000)
+-------------------------------------------------------+
| Django + Gunicorn (Kontener)                          |
| CMD ["gunicorn", "config.wsgi:application", ...]      |
+-------------------------------------------------------+
```

### 7.3 Konfiguracja Nginx (`nginx/nginx.conf`)

Utwórz plik `nginx/nginx.conf`:

```nginx
server {
    listen 80;
    server_name localhost;

    location /static/ {
        alias /app/staticfiles/;
    }

    location /media/ {
        alias /app/media/;
    }

    location / {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 7.4 Produkcyjny plik `Dockerfile.prod`

Utwórz plik `Dockerfile.prod`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends     gcc     libpq-dev     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Uruchomienie Gunicorna z 3 workerami na porcie 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
```

### Zadanie praktyczne 7
1. Przeanalizuj różnice między produkcyjną koncepcją uruchomienia Gunicorna a serwerem deweloperskim `runserver`.
2. Zwróć uwagę na rolę serwera Nginx w obsłudze ruchu i serwowaniu statyki bez obciążania procesu Pythona.

---

## Blok 8: Debugowanie, operacje i zarzadzanie kontenerami (30 min)

### 8.1 Podstawowe komendy Docker CLI

```bash
# Lista uruchomionych kontenerów
docker ps

# Lista wszystkich kontenerów (w tym zatrzymanych)
docker ps -a

# Wyświetlenie logów kontenera w czasie rzeczywistym
docker logs -f django_backend

# Wejście do powłoki interaktywnej kontenera
docker exec -it django_backend bash
```

### 8.2 Kluczowe polecenia Docker Compose

```bash
# Uruchomienie wszystkich usług w tle z przebudowaniem obrazów
docker compose up -d --build

# Zatrzymanie i usunięcie kontenerów oraz sieci
docker compose down

# Zatrzymanie usunięcie kontenerów, sieci ORAZ wolumenów (UWAGA: kasuje dane bazy!)
docker compose down -v

# Restart pojedynczej usługi
docker compose restart backend
```

### 8.3 Wykonywanie operacji administracyjnych Django w kontenerze

Nigdy nie uruchamiaj poleceń `python manage.py` na swoim hoście, jeśli zależne usugi (baza, redis) działają w kontenerach! Wszystkie operacje wykonuj wewnątrz kontenera aplikacji:

```bash
# 1. Wykonywanie migracji bazy danych
docker compose exec backend python manage.py migrate

# 2. Tworzenie superużytkownika
docker compose exec backend python manage.py createsuperuser

# 3. Uruchomienie interaktywnej powłoki Django Shell
docker compose exec backend python manage.py shell

# 4. Zbierz pliki statyczne
docker compose exec backend python manage.py collectstatic --no-input
```

---

## Projekt końcowy: Django Blog API w Docker Compose

Kompletna, produkcyjna implementacja systemu blogowego opartego o Django REST Framework, PostgreSQL, Redis oraz Nginx.

### Struktura katalogów projektu

```
blog-docker/
├── backend/
│   ├── blog/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── Dockerfile
│   ├── Dockerfile.prod
│   ├── manage.py
│   └── requirements.txt
├── nginx/
│   └── nginx.conf
├── .env
├── .env.example
├── docker-compose.yml
└── docker-compose.prod.yml
```

---

### Kod źródłowy projektu

#### 1. `backend/requirements.txt`
```text
Django>=5.0,<5.1
djangorestframework>=3.14.0
psycopg2-binary>=2.9.9
django-redis>=5.4.0
gunicorn>=21.2.0
```

#### 2. `backend/Dockerfile`
```dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### 3. `backend/Dockerfile.prod`
```dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
```

#### 4. `backend/config/settings.py`
```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'default-insecure-key')
DEBUG = int(os.getenv('DEBUG', 1))

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party
    'rest_framework',
    # Local apps
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', 'blog_db'),
        'USER': os.getenv('DB_USER', 'blog_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'blog_password'),
        'HOST': os.getenv('DB_HOST', 'database'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://redis:6379/1"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

LANGUAGE_CODE = 'pl-pl'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

#### 5. `backend/blog/models.py`
```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

#### 6. `backend/blog/serializers.py`
```python
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'content', 'created_at', 'updated_at']
```

#### 7. `backend/blog/views.py`
```python
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        # Automatycznie przypisuje zalogowanego użytkownika lub pierwszego admina
        author = self.request.user if self.request.user.is_authenticated else None
        serializer.save(author=author)

    # Buforowanie listy postów w Redis na 60 sekund
    @method_decorator(cache_page(60))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)
```

#### 8. `backend/blog/urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]
```

#### 9. `backend/config/urls.py`
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### 10. `nginx/nginx.conf`
```nginx
server {
    listen 80;
    server_name localhost;

    location /static/ {
        alias /app/staticfiles/;
    }

    location /media/ {
        alias /app/media/;
    }

    location / {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### 11. `.env`
```env
DEBUG=1
SECRET_KEY=super-secret-django-key-replace-in-production
ALLOWED_HOSTS=localhost,127.0.0.1,backend

DB_ENGINE=django.db.backends.postgresql
DB_NAME=blog_db
DB_USER=blog_user
DB_PASSWORD=blog_password123
DB_HOST=database
DB_PORT=5432

REDIS_URL=redis://redis:6379/1
```

#### 12. `docker-compose.yml` (Deweloperski)
```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: blog_backend_dev
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
    # kolejnosc uruchamianych kontenerów-zależnosci
    depends_on:
      - database
      - redis
    networks:
      - blog_network

  database:
    image: postgres:16-alpine
    container_name: blog_postgres_dev
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - blog_network

  redis:
    image: redis:7-alpine
    container_name: blog_redis_dev
    ports:
      - "6379:6379"
    networks:
      - blog_network

networks:
  blog_network:
    driver: bridge

volumes:
  postgres_data:
```

#### 13. `docker-compose.prod.yml` (Produkcyjny)
```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.prod
    container_name: blog_backend_prod
    env_file:
      - .env
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    depends_on:
      - database
      - redis
    networks:
      - blog_network

  database:
    image: postgres:16-alpine
    container_name: blog_postgres_prod
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data_prod:/var/lib/postgresql/data
    networks:
      - blog_network

  redis:
    image: redis:7-alpine
    container_name: blog_redis_prod
    networks:
      - blog_network

  nginx:
    image: nginx:1.25-alpine
    container_name: blog_nginx_prod
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    depends_on:
      - backend
    networks:
      - blog_network

networks:
  blog_network:
    driver: bridge

volumes:
  postgres_data_prod:
  static_volume:
  media_volume:
```

---

### Instrukcja uruchomienia i weryfikacji projektu końcowego

#### Krok 1: Inicjalizacja środowiska deweloperskiego
```bash
# 1. Uruchomienie serwisów w trybie detached
docker compose up -d

# 2. Wykonanie migracji bazodanowych
docker compose exec backend python manage.py migrate

# 3. Utworzenie konta administratora
docker compose exec backend python manage.py createsuperuser

# 4. Sprawdzenie stanu serwisów
docker compose ps
```

#### Krok 2: Testowanie API DRF
* **Panel Administracyjny:** Otwórz `http://localhost:8000/admin/` i zaloguj się utworzonym superużytkownikiem.
* **API Endpoint:** Otwórz `http://localhost:8000/api/posts/` i dodaj nowy wpis za pomocą formularza browsable API.

#### Krok 3: Uruchomienie stosu produkcyjnego z Nginx
```bash
# 1. Zatrzymanie stosu deweloperskiego
docker compose down

# 2. Uruchomienie stosu produkcyjnego
docker compose -f docker-compose.prod.yml up -d --build

# 3. Wykonanie migracji i zbieranie plików statycznych w środowisku produkcyjnym
docker compose -f docker-compose.prod.yml exec backend python manage.py migrate
docker compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --no-input

# 4. Weryfikacja działania pod adresem portu 80 Nginxa:
curl -I http://localhost/api/posts/
```
