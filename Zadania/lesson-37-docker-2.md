
## Docker 2: Zaawansowany Dockerfile i optymalizacja obrazów (60 min)

### 1. Mechanizm cache warstw (Layer Caching)

Każda instrukcja w pliku `Dockerfile` tworzy nową warstwę. Warstwy są buforowane (cached), co znacznie przyspiesza ponowne budowanie obrazu. Docker buduje obraz linijka po linijce, z góry na dół. Jeśli kod warstwy się nie zmienił, Docker użyje jej z pamięci podręcznej. Jeśli jednak warstwa ulegnie zmianie, Docker musi przebudować ją oraz **wszystkie warstwy poniżej**.

Kolejność instrukcji ma zatem krytyczne znaczenie dla szybkości budowania. Kopiowanie pliku zależności i ich instalacja to krok optymalizacji cache Dockera.

**Prawidłowa kolejność (szybki build):**

```dockerfile
# Zmienia się rzadko
COPY requirements.txt .
RUN pip install -r requirements.txt

# Zmienia się ciągle (przy każdym zapisie pliku)
COPY . .

```

Dzięki temu, gdy zmienisz tylko kod aplikacji (np. `views.py`), Docker użyje gotowego cache'u dla `pip install` i przebuduje tylko ostatnią warstwę.

**Błędna kolejność (bardzo wolny build):**

```dockerfile
# Zmienia się ciągle
COPY . .

# Przebudowywane przy KAŻDEJ zmianie w kodzie!
RUN pip install -r requirements.txt

```

### 2. Multi-stage build (Budowanie wieloetapowe)

Standardowy obraz Pythona jest duży, ponieważ zawiera kompilatory (np. `gcc`) potrzebne do zbudowania niektórych bibliotek. W środowisku uruchomieniowym (runtime) są one całkowicie zbędne i tylko niepotrzebnie powiększają ostateczny obraz, zwiększając też podatność na ataki.

Multi-stage build pozwala podzielić `Dockerfile` na etapy (stages). Każda instrukcja `FROM` rozpoczyna nowy etap. Pozwala to na skompilowanie zależności w jednym etapie (builder), a następnie skopiowanie wyłącznie gotowych plików do docelowego, czystego i małego obrazu.

**Przykład:**

```dockerfile
# Etap 1: Budowanie (Builder)
FROM python:3.12 AS builder
WORKDIR /build
COPY requirements.txt .
# Tworzymy pakiety wheel zamiast instalować
RUN pip wheel -r requirements.txt --wheel-dir /build/wheels

# Etap 2: Środowisko uruchomieniowe (Runtime)
FROM python:3.12-slim
WORKDIR /app
# Kopiujemy tylko gotowe pakiety z etapu builder
COPY --from=builder /build/wheels /wheels
RUN pip install --no-cache /wheels/*
COPY . .

```
czylui
**Schemat działania:**

```text
Builder
 ├── gcc
 ├── pip
 ├── kompilacja
 └── zależności
        │
COPY --from
        ▼
Runtime
 ├── python
 ├── aplikacja
 └── gotowe biblioteki

```

### 3. Obraz bazowy vs etap (Stage)

To zagadnienie często myli początkujących programistów analizujących zaawansowane pliki `Dockerfile`.

* **`FROM python:3.12-slim`**: Odwołuje się do obrazu bazowego. Docker Engine połączy się z publicznym rejestrem Docker Hub i pobierze ten obraz z internetu (jeśli nie ma go lokalnie na dysku).


* **`FROM builder`** lub **`COPY --from=builder`**: Nie pobiera niczego z internetu. Słowo `builder` to jedynie lokalny alias (nazwa etapu) zdefiniowany wcześniej w tym samym pliku `Dockerfile` za pomocą instrukcji `AS builder`.

### 4. Context builda (Kontekst budowania)

W pliku konfiguracyjnym spotykamy zapis `context: .`. Kropka `.` oznacza bieżący katalog. Kontekst to zbiór plików i folderów, które są pakowane i wysyłane do demona Dockera (`dockerd`) w momencie startu budowania obrazu.

**Dlaczego `COPY ../plik.txt .` nie działa?**
Demon Dockera działa w izolacji i ma dostęp **tylko** do plików przekazanych mu w kontekście. Nie może poruszać się po Twoim lokalnym dysku powyżej zdefiniowanego katalogu. Jeśli kontekstem jest `.`, demon widzi tylko to, co jest wewnątrz tego folderu.

### 5. Plik .dockerignore

Podczas wysyłania kontekstu do demona Dockera, przesyłane są wszystkie pliki. Wysyłanie zbędnych danych (jak wirtualne środowisko czy historia repozytorium) drastycznie wydłuża czas budowania i powiększa kontekst. Rozwiązaniem jest plik `.dockerignore` (działający analogicznie do `.gitignore`).

**Przykładowy plik `.dockerignore` dla Django:**

```text
.git
venv/
.venv/
.env
__pycache__/
*.pyc
.pytest_cache

```

**Zalety używania `.dockerignore`:**

* **Zmniejszenie contextu:** Demon Dockera otrzymuje tylko niezbędne pliki.
* **Szybszy build:** Kopiowanie plików (`COPY . .`) trwa ułamki sekund.
* **Bezpieczeństwo:** Przypadkowo nie skopiujesz do obrazu pliku `.env` z sekretami z lokalnego środowiska.

### 6. ENTRYPOINT vs CMD

W naszym podstawowym pliku używamy polecenia `CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]`. Warto jednak znać różnicę między dwiema kluczowymi instrukcjami uruchomieniowymi.

* **`ENTRYPOINT`**: Konfiguruje kontener tak, aby działał jak konkretny program. Nadpisanie go z poziomu terminala jest trudne (wymaga specjalnej flagi).
* **`CMD`**: Stanowi domyślne argumenty dla `ENTRYPOINT` (jeśli ten jest podany) lub po prostu domyślną komendę, którą bardzo łatwo nadpisać (np. `docker run moj_obraz bash`).

**Przykład połączonego użycia:**

```dockerfile
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

```

Dzięki temu, wpisując `docker run moj_obraz migrate`, słowo `migrate` zastąpi domyślne `CMD`, a kontener wykona `python manage.py migrate`.

### 7. Dev vs Prod Dockerfile

W profesjonalnych projektach rzadko korzysta się z jednego pliku. Zazwyczaj mamy deweloperski `Dockerfile` oraz produkcyjny `Dockerfile.prod`. Poniższa tabela zbiera ich najważniejsze różnice, wynikające ze specyfiki obu środowisk:

| Cecha           | Środowisko Deweloperskie (`Dockerfile`)               | Środowisko Produkcyjne (`Dockerfile.prod`) |
| --------------- | ----------------------------------------------------- | ------------------------------------------ |
| **Pliki kodu**  | Współdzielone z hostem przez wolumen (Volume)         | Wbudowane na stałe w obraz (skopiowane)    |
| **Serwer WSGI** | Wbudowany serwer: `manage.py runserver`<br>           | Wydajny serwer: `Gunicorn` / `uWSGI`<br>   |
| **Tryb Debug**  | `DEBUG=True`                                          | `DEBUG=False`                              |
| **Odświeżanie** | Autoreload włączony (zmiany w kodzie resetują serwer) | Brak autoreloadu (stały kod)               |

### 8. Build arguments (ARG) i zmienne (ENV)

Konfigurację można przekazywać na różnych etapach życia kontenera.

* **`ARG` (Build-time):** Dostępne **tylko** podczas budowania obrazu. Przydatne do parametryzacji `Dockerfile`.
* **`ENV` (Run-time):** Dostępne zarówno podczas budowania, jak i **wewnątrz działającego kontenera** (widoczne dla aplikacji Django).

**Przykład użycia ARG i ENV:**

```dockerfile
# ARG dostępne przed FROM
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim

# ENV dostępne dla działającej aplikacji
ENV PYTHONDONTWRITEBYTECODE=1

```

### 9. Rejestry obrazów i workflow CI/CD

Jak fizycznie obraz trafia z komputera dewelopera na serwer produkcyjny? Służą do tego rejestry obrazów, takie jak publiczny i prywatny Docker Hub czy GitHub Container Registry (GHCR).

Poniższy schemat obrazuje kompletny proces (workflow), który stanowi fundament automatyzacji CI/CD (Continuous Integration / Continuous Deployment):

```text
  [ Lokalny komputer / CI Server ]
           Dockerfile
               │
        (1) docker build
               │
          Gotowy Image
               │
        (2) docker tag (np. v1.0.0)
               │
        (3) docker push
               │
               ▼
  [ Rejestr (np. Docker Hub / GHCR) ]
               │
        (4) docker pull
               │
               ▼
      [ Serwer Produkcyjny ]
               │
        (5) docker run
               │
      Uruchomiony Kontener

```