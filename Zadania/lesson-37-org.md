# **Lekcja 37: Docker i Konteneryzacja Aplikacji**

`#lekcja` `#python` `#docker` `#devops` `#konteneryzacja`

W tej lekcji poznasz Docker — technologię, która zrewolucjonizowała sposób, w jaki tworzymy, wdrażamy i zarządzamy aplikacjami. Nauczysz się, czym jest konteneryzacja, jak działa Docker, jak konfigurować sieci kontenerów oraz jak używać docker-compose do zarządzania wielokontenerowymi aplikacjami. Na koniec stworzysz kompletną aplikację działającą w kontenerach.

---

## **1. Konteneryzacja i Wirtualizacja**

> [!definition]
> **Konteneryzacja** to metoda pakowania aplikacji wraz z jej zależnościami w izolowane jednostki zwane kontenerami, które mogą być uruchamiane w sposób spójny na różnych środowiskach.

### Wprowadzenie

Konteneryzacja to nowoczesne podejście do wdrażania aplikacji, które rozwiązuje klasyczny problem "na moim komputerze działa". W przeciwieństwie do maszyn wirtualnych (VM), kontenery są lżejsze, szybsze i bardziej efektywne.

**Różnice między wirtualizacją a konteneryzacją:**

| Aspekt | Wirtualizacja (VM) | Konteneryzacja |
|--------|-------------------|----------------|
| **Izolacja** | Pełna izolacja z własnym OS | Współdzielony kernel hosta |
| **Rozmiar** | GB (całe OS) | MB (tylko aplikacja) |
| **Start** | Minuty | Sekundy |
| **Wydajność** | Overhead przez hypervisor | Prawie natywna |
| **Przenośność** | Średnia | Wysoka |

### Przykład 1: Porównanie rozmiaru obrazów

```python
# Skrypt pokazujący różnicę w rozmiarach między VM a kontenerami

# Symulacja rozmiaru VM z pełnym systemem operacyjnym
vm_os_size_gb = 2.5  # Bazowy system operacyjny
vm_app_size_mb = 150  # Rozmiar aplikacji
vm_dependencies_mb = 500  # Biblioteki i zależności
vm_total_gb = vm_os_size_gb + (vm_app_size_mb + vm_dependencies_mb) / 1024

print(f"Rozmiar VM: {vm_total_gb:.2f} GB")

# Rozmiar kontenera Docker (tylko aplikacja + zależności)
container_base_mb = 80  # Minimalny obraz bazowy (np. alpine)
container_app_mb = 150  # Ta sama aplikacja
container_dependencies_mb = 200  # Tylko potrzebne biblioteki
container_total_mb = container_base_mb + container_app_mb + container_dependencies_mb

print(f"Rozmiar kontenera: {container_total_mb} MB")

# Obliczenie oszczędności
savings_ratio = vm_total_gb * 1024 / container_total_mb
print(f"Kontener jest {savings_ratio:.1f}x mniejszy niż VM")
print(f"Oszczędność miejsca: {(vm_total_gb * 1024 - container_total_mb):.0f} MB")
```

**Output:**
```
Rozmiar VM: 3.13 GB
Rozmiar kontenera: 430 MB
Kontener jest 7.5x mniejszy niż VM
Oszczędność miejsca: 2774 MB
```

### Przykład 2: Czas uruchamiania

```python
import time
from datetime import datetime

def simulate_vm_startup():
    """Symulacja uruchomienia maszyny wirtualnej"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Uruchamianie VM...")
    print("  - Bootowanie OS...")
    time.sleep(2)  # Symulacja bootowania
    print("  - Ładowanie sterowników...")
    time.sleep(1)
    print("  - Inicjalizacja serwisów...")
    time.sleep(1.5)
    print("  - Uruchamianie aplikacji...")
    time.sleep(0.5)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] VM gotowa!")
    return 5  # ~5 sekund (w rzeczywistości może być 30-120s)

def simulate_container_startup():
    """Symulacja uruchomienia kontenera"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Uruchamianie kontenera...")
    time.sleep(0.3)  # Kontener startuje bardzo szybko
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Kontener gotowy!")
    return 0.3

print("=== Test czasu uruchamiania ===\n")

print("Maszyna wirtualna:")
start = time.time()
simulate_vm_startup()
vm_time = time.time() - start
print(f"Czas: {vm_time:.2f}s\n")

print("Kontener Docker:")
start = time.time()
simulate_container_startup()
container_time = time.time() - start
print(f"Czas: {container_time:.2f}s\n")

print(f"Kontener uruchamia się {vm_time/container_time:.1f}x szybciej!")
```

### Przykład 3: Izolacja procesów

```python
import os
import psutil

def show_process_isolation():
    """
    Demonstracja izolacji procesów w kontenerach.

    W kontenerze Docker:
    - Proces widzi tylko swoją przestrzeń nazw (namespace)
    - PID 1 to główny proces aplikacji
    - Nie widzi procesów hosta ani innych kontenerów
    """
    print("=== Informacje o procesie ===\n")

    # PID bieżącego procesu
    pid = os.getpid()
    print(f"PID procesu: {pid}")

    # Informacje o systemie
    print(f"Liczba CPU: {psutil.cpu_count()}")
    print(f"Pamięć RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB")

    # W kontenerze te wartości mogą być ograniczone
    # np. tylko 2 CPU i 512 MB RAM
    print(f"\nW kontenerze te zasoby mogą być limitowane:")
    print(f"  docker run --cpus=2 --memory=512m myapp")

# Uruchomienie
show_process_isolation()
```

### Schemat działania

```mermaid
graph TB
    subgraph "Wirtualizacja"
        H1[Host OS]
        HV[Hypervisor]
        VM1[VM 1<br/>Guest OS<br/>App A]
        VM2[VM 2<br/>Guest OS<br/>App B]
        H1 --> HV
        HV --> VM1
        HV --> VM2
    end
    
    subgraph "Konteneryzacja"
        H2[Host OS]
        DE[Docker Engine]
        C1[Kontener 1<br/>App A]
        C2[Kontener 2<br/>App B]
        C3[Kontener 3<br/>App C]
        H2 --> DE
        DE --> C1
        DE --> C2
        DE --> C3
    end
    
    Wirtualizacja ~~~ Konteneryzacja
```

> [!tip]
> **Kiedy używać kontenerów, a kiedy VM?**
> - **Kontenery**: Mikroserwisy, CI/CD, skalowanie aplikacji webowych, środowiska deweloperskie
> - **VM**: Pełna izolacja dla różnych systemów operacyjnych, legacy aplikacje wymagające konkretnego OS, maksymalne bezpieczeństwo

> [!warning]
> **Bezpieczeństwo**: Kontenery współdzielą kernel systemu hosta. Jeśli kernel zostanie skompromitowany, wszystkie kontenery są zagrożone. W VM każda maszyna ma własny kernel, co daje lepszą izolację.

> [!note]
> **Historia**: Docker został wydany w 2013 roku przez firmę dotCloud (później Docker Inc.). Szybko stał się standardem przemysłowym, wypierając starsze rozwiązania konteneryzacyjne jak LXC.

---

## **2. Docker jako Technologia**

> [!definition]
> **Docker** to platforma do tworzenia, wdrażania i uruchamiania aplikacji w kontenerach. Umożliwia pakowanie aplikacji wraz z zależnościami w przenośne obrazy, które działają identycznie na każdym systemie z zainstalowanym Dockerem.

### Wprowadzenie

Docker składa się z kilku kluczowych komponentów:
- **Docker Engine** - daemon zarządzający kontenerami
- **Docker Image** - szablon tylko do odczytu z aplikacją
- **Docker Container** - uruchomiona instancja obrazu
- **Dockerfile** - plik tekstowy z instrukcjami budowania obrazu
- **Docker Hub** - rejestr publicznych obrazów

### Przykład 1: Podstawowy Dockerfile dla aplikacji Python

```python
# Dockerfile - plik definiujący obraz Docker
"""
# To jest Dockerfile (bez rozszerzenia)
# Każda linia to instrukcja dla Docker Engine

# 1. Bazowy obraz - używamy oficjalnego obrazu Python
FROM python:3.11-slim

# 2. Metadata o autorze
LABEL maintainer="developer@example.com"

# 3. Ustawienie zmiennych środowiskowych
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_HOME=/app

# 4. Utworzenie katalogu roboczego
WORKDIR $APP_HOME

# 5. Kopiowanie pliku z zależnościami
COPY requirements.txt .

# 6. Instalacja zależności
# --no-cache-dir zmniejsza rozmiar obrazu
RUN pip install --no-cache-dir -r requirements.txt

# 7. Kopiowanie kodu aplikacji
COPY . .

# 8. Utworzenie użytkownika bez uprawnień root (bezpieczeństwo)
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser $APP_HOME
USER appuser

# 9. Port, na którym działa aplikacja
EXPOSE 8000

# 10. Komenda uruchamiająca aplikację
CMD ["python", "main.py"]
"""

# Plik main.py - prosta aplikacja webowa
from aiohttp import web

async def hello(request):
    return web.Response(text="Hello from Docker!")

async def health(request):
    return web.json_response({"status": "healthy"})

app = web.Application()
app.router.add_get('/', hello)
app.router.add_get('/health', health)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8000)
```

**Struktura projektu:**
```
my-app/
├── Dockerfile
├── requirements.txt  (zawiera: aiohttp==3.9.0)
└── main.py
```

**Budowanie i uruchamianie:**
```bash
# Zbudowanie obrazu
docker build -t my-python-app:1.0 .

# Uruchomienie kontenera
docker run -d -p 8000:8000 --name my-app my-python-app:1.0

# Sprawdzenie czy działa
curl http://localhost:8000/
```

### Przykład 2: Warstwy obrazu i cache

```python
"""
Docker buduje obrazy warstwami. Każda instrukcja w Dockerfile
tworzy nową warstwę. Docker cachuje warstwy, co przyspiesza
kolejne buildy.

Optymalizacja Dockerfile - porównanie:
"""

# ❌ ZŁA PRAKTYKA - każda zmiana w kodzie wymusza reinstalację zależności
"""
FROM python:3.11-slim
COPY . .                          # Kopiuje wszystko
RUN pip install -r requirements.txt  # Instaluje zależności
CMD ["python", "main.py"]
"""

# ✅ DOBRA PRAKTYKA - zależności są cachowane
"""
FROM python:3.11-slim
COPY requirements.txt .           # Kopiuje tylko requirements
RUN pip install -r requirements.txt  # Ta warstwa jest cachowana
COPY . .                          # Kod zmienia się często
CMD ["python", "main.py"]
"""

# Skrypt pokazujący warstwy obrazu
import subprocess
import json

def show_image_layers(image_name):
    """Wyświetla warstwy obrazu Docker"""
    # Pobranie historii obrazu
    result = subprocess.run(
        ['docker', 'history', image_name, '--format', '{{json .}}'],
        capture_output=True,
        text=True
    )

    print(f"=== Warstwy obrazu {image_name} ===\n")
    total_size = 0

    for line in result.stdout.strip().split('\n'):
        layer = json.loads(line)
        size = layer.get('Size', 'N/A')
        created_by = layer.get('CreatedBy', 'N/A')[:60]

        print(f"Rozmiar: {size:>10} | {created_by}")

        # Parsowanie rozmiaru (uproszczone)
        if 'MB' in size:
            total_size += float(size.replace('MB', ''))

    print(f"\nŁączny rozmiar: ~{total_size:.1f} MB")

# Przykładowe użycie
# show_image_layers('my-python-app:1.0')
```

### Przykład 3: Multi-stage build dla mniejszych obrazów

```python
"""
Multi-stage build pozwala na utworzenie mniejszych obrazów produkcyjnych
poprzez budowanie w etapach i kopiowanie tylko niezbędnych plików.

Dockerfile z multi-stage build:
"""

# ===== STAGE 1: Builder =====
"""
FROM python:3.11 AS builder

WORKDIR /build

# Instalacja zależności w virtualenv
COPY requirements.txt .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Opcjonalnie: kompilacja kodu
# RUN python -m compileall .
"""

# ===== STAGE 2: Production =====
"""
FROM python:3.11-slim

# Kopiowanie tylko virtualenv z buildera (bez narzędzi budowania)
COPY --from=builder /opt/venv /opt/venv

# Ustawienie PATH
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Kopiowanie kodu aplikacji
COPY main.py .

# Użytkownik bez uprawnień
RUN useradd -m appuser
USER appuser

EXPOSE 8000
CMD ["python", "main.py"]
"""

# Porównanie rozmiarów
def compare_build_sizes():
    """
    Przykładowe porównanie rozmiarów:

    Single-stage build:  850 MB
    Multi-stage build:   180 MB

    Oszczędność: ~670 MB (78%)
    """
    single_stage = 850
    multi_stage = 180

    savings = single_stage - multi_stage
    savings_percent = (savings / single_stage) * 100

    print(f"Single-stage: {single_stage} MB")
    print(f"Multi-stage:  {multi_stage} MB")
    print(f"Oszczędność:  {savings} MB ({savings_percent:.0f}%)")

compare_build_sizes()
```

### Podstawowe komendy Docker

```mermaid
graph LR
    A[Dockerfile] -->|docker build| B[Image]
    B -->|docker run| C[Container]
    C -->|docker commit| B
    B -->|docker push| D[Registry]
    D -->|docker pull| B

    style A fill:#f9f,stroke:#333
    style B fill:#bbf,stroke:#333
    style C fill:#bfb,stroke:#333
    style D fill:#fbb,stroke:#333
```

### Najważniejsze komendy

```bash
# Budowanie obrazu
docker build -t nazwa:tag .

# Listowanie obrazów
docker images

# Uruchamianie kontenera
docker run -d -p 8000:8000 --name kontener nazwa:tag

# Listowanie kontenerów
docker ps        # działające
docker ps -a     # wszystkie

# Zatrzymanie i usunięcie
docker stop kontener
docker rm kontener

# Logi kontenera
docker logs kontener
docker logs -f kontener  # follow

# Wejście do kontenera
docker exec -it kontener bash

# Usunięcie obrazu
docker rmi nazwa:tag

# Czyszczenie systemu
docker system prune -a  # usuwa nieużywane obrazy, kontenery, sieci
```

> [!tip]
> **Docker .dockerignore**: Podobnie jak .gitignore, plik .dockerignore określa, które pliki nie powinny być kopiowane do obrazu. Typowa zawartość:
> ```
> __pycache__/
> *.pyc
> .git/
> .env
> venv/
> ```

> [!warning]
> **Nigdy nie commituj sekretów do obrazów!** Używaj zmiennych środowiskowych lub Docker secrets do przechowywania haseł, kluczy API itp.

> [!info]
> **Docker Desktop** to aplikacja GUI dla Windows/Mac, która instaluje Docker Engine, Docker CLI i dodatkowe narzędzia. Na Linuxie instaluje się Docker Engine bezpośrednio.

---

## **3. Sieci Docker**

> [!definition]
> **Sieć Docker (Docker Network)** to wirtualna sieć umożliwiająca komunikację między kontenerami, a także między kontenerami a światem zewnętrznym. Docker automatycznie zarządza konfiguracją sieciową.

### Wprowadzenie

Docker oferuje kilka typów sieci:
- **bridge** (domyślna) - kontenery w tej samej sieci mogą się komunikować
- **host** - kontener używa bezpośrednio sieci hosta (brak izolacji)
- **none** - kontener nie ma dostępu do sieci
- **overlay** - sieć rozproszona dla Docker Swarm (klastry)
- **macvlan** - kontener otrzymuje własny adres MAC

### Przykład 1: Tworzenie i używanie niestandardowej sieci

```python
"""
Domyślnie kontenery komunikują się po nazwach tylko w niestandardowych sieciach.
W domyślnej sieci bridge trzeba używać adresów IP.
"""

# Komendy Docker dla sieci
network_commands = """
# Utworzenie niestandardowej sieci
docker network create my-app-network

# Listowanie sieci
docker network ls

# Informacje o sieci
docker network inspect my-app-network

# Uruchomienie kontenerów w tej samej sieci
docker run -d --name backend --network my-app-network backend-image
docker run -d --name frontend --network my-app-network frontend-image

# Teraz kontenery mogą się komunikować po nazwach:
# frontend może wywołać: http://backend:8000/api

# Usunięcie sieci
docker network rm my-app-network
"""

# Przykład: Backend API w kontenerze
from aiohttp import web
import socket

async def api_handler(request):
    """API endpoint zwracający informacje o kontenerze"""
    hostname = socket.gethostname()  # ID kontenera

    return web.json_response({
        "message": "Hello from backend",
        "container_id": hostname,
        "service": "backend"
    })

async def create_backend_app():
    app = web.Application()
    app.router.add_get('/api', api_handler)
    return app

# Przykład: Frontend w kontenerze komunikujący się z backendem
import aiohttp

async def call_backend():
    """
    Frontend wywołuje backend po nazwie kontenera.
    Docker DNS automatycznie rozwiązuje nazwę 'backend' na IP kontenera.
    """
    async with aiohttp.ClientSession() as session:
        # 'backend' to nazwa kontenera w tej samej sieci Docker
        async with session.get('http://backend:8000/api') as response:
            data = await response.json()
            print(f"Odpowiedź z backendu: {data}")
            return data

async def frontend_handler(request):
    """Frontend endpoint, który wywołuje backend"""
    try:
        backend_data = await call_backend()
        return web.json_response({
            "frontend": "OK",
            "backend_response": backend_data
        })
    except Exception as e:
        return web.json_response({
            "error": str(e)
        }, status=500)

async def create_frontend_app():
    app = web.Application()
    app.router.add_get('/', frontend_handler)
    return app

print("Kontenery w tej samej sieci Docker komunikują się po nazwach!")
```

### Przykład 2: Mapowanie portów (port publishing)

```python
"""
Mapowanie portów pozwala udostępnić usługę kontenera na hoście.

Format: -p [host_port]:[container_port]
"""

# Różne sposoby mapowania portów
port_mapping_examples = {
    "podstawowe": {
        "komenda": "docker run -p 8000:8000 myapp",
        "opis": "Port 8000 hosta → port 8000 kontenera"
    },
    "różne_porty": {
        "komenda": "docker run -p 80:8000 myapp",
        "opis": "Port 80 hosta → port 8000 kontenera"
    },
    "tylko_localhost": {
        "komenda": "docker run -p 127.0.0.1:8000:8000 myapp",
        "opis": "Dostępne tylko lokalnie na hoście"
    },
    "losowy_port": {
        "komenda": "docker run -p 8000 myapp",
        "opis": "Docker wybiera losowy port hosta"
    },
    "wiele_portów": {
        "komenda": "docker run -p 8000:8000 -p 8001:8001 myapp",
        "opis": "Mapowanie wielu portów"
    }
}

for name, config in port_mapping_examples.items():
    print(f"\n{name.upper().replace('_', ' ')}:")
    print(f"  Komenda: {config['komenda']}")
    print(f"  Opis: {config['opis']}")

# Aplikacja nasłuchująca na wielu portach
async def create_multi_port_app():
    """Aplikacja z wieloma portami"""

    # App na porcie 8000 - API
    api_app = web.Application()

    async def api_endpoint(request):
        return web.json_response({"service": "API", "port": 8000})

    api_app.router.add_get('/api', api_endpoint)

    # App na porcie 8001 - Metrics
    metrics_app = web.Application()

    async def metrics_endpoint(request):
        return web.json_response({
            "service": "Metrics",
            "port": 8001,
            "requests_total": 1234
        })

    metrics_app.router.add_get('/metrics', metrics_endpoint)

    print("API dostępne na porcie 8000")
    print("Metrics dostępne na porcie 8001")

    return api_app, metrics_app

# W Dockerfile trzeba wyeksponować oba porty:
# EXPOSE 8000 8001
```

### Przykład 3: DNS i service discovery

```python
"""
Docker ma wbudowany DNS server, który automatycznie rozwiązuje
nazwy kontenerów na ich adresy IP w obrębie tej samej sieci.
"""

import socket
import asyncio

async def dns_resolution_demo():
    """
    Demonstracja jak Docker DNS rozwiązuje nazwy kontenerów
    """
    services = ['backend', 'database', 'cache', 'frontend']

    print("=== Docker DNS Resolution ===\n")

    for service in services:
        try:
            # W kontenerze Docker, socket.gethostbyname() użyje Docker DNS
            ip = socket.gethostbyname(service)
            print(f"{service:15} → {ip}")
        except socket.gaierror:
            print(f"{service:15} → [nie znaleziono]")

    print("\n" + "="*40)
    print("Docker automatycznie aktualizuje DNS gdy kontenery")
    print("startują lub zatrzymują się!")

# Praktyczny przykład: aplikacja łącząca się z bazą danych
import asyncpg

async def connect_to_database():
    """
    Połączenie z PostgreSQL w kontenerze.

    Zamiast używać IP, używamy nazwy kontenera 'database'.
    Docker DNS automatycznie to rozwiąże.
    """
    connection = await asyncpg.connect(
        host='database',  # Nazwa kontenera, a nie IP!
        port=5432,
        user='postgres',
        password='secret',
        database='myapp'
    )

    version = await connection.fetchval('SELECT version()')
    print(f"Połączono z: {version}")

    await connection.close()

print("Docker DNS umożliwia service discovery bez hardcodowania IP!")
```

### Schemat sieci Docker

```mermaid
graph TB
    subgraph "Host Machine"
        subgraph "my-app-network (bridge)"
            FE[Frontend Container<br/>frontend:3000]
            BE[Backend Container<br/>backend:8000]
            DB[(Database Container<br/>database:5432)]

            FE -->|HTTP| BE
            BE -->|SQL| DB
        end

        DNS[Docker DNS<br/>10.0.0.2]

        FE -.->|nazwa→IP| DNS
        BE -.->|nazwa→IP| DNS

        DOCKER[Docker Engine]
        DNS --- DOCKER
    end

    USER[User Browser] -->|localhost:3000| FE

    style DNS fill:#ffe6e6
    style FE fill:#e6f3ff
    style BE fill:#e6ffe6
    style DB fill:#fff0e6
```

> [!tip]
> **Alias w sieci**: Możesz nadać kontenerowi alias w sieci, aby był dostępny pod wieloma nazwami:
> ```bash
> docker run --network my-net --network-alias api --network-alias backend myapp
> ```

> [!warning]
> **Domyślna sieć bridge**: W domyślnej sieci bridge kontenery NIE mogą się komunikować po nazwach - tylko przez IP. Zawsze twórz niestandardowe sieci dla aplikacji wielokontenerowych.

> [!info]
> **Port 0.0.0.0 vs 127.0.0.1**: W kontenerze aplikacja musi nasłuchiwać na 0.0.0.0 (wszystkie interfejsy), a nie 127.0.0.1 (tylko localhost), aby była dostępna z zewnątrz kontenera.

---

## **4. Docker Compose**

> [!definition]
> **Docker Compose** to narzędzie do definiowania i uruchamiania wielokontenerowych aplikacji Docker. Używa pliku YAML (`docker-compose.yml`) do konfiguracji wszystkich serwisów, sieci i wolumenów.

### Wprowadzenie

Docker Compose rozwiązuje problem zarządzania wieloma kontenerami. Zamiast uruchamiać każdy kontener osobno długą komendą `docker run`, definiujesz całą aplikację w jednym pliku.

**Korzyści:**
- Deklaratywna konfiguracja (infrastructure as code)
- Łatwe zarządzanie zależnościami między serwisami
- Automatyczne tworzenie sieci i wolumenów
- Proste skalowanie serwisów
- Środowiska deweloperskie identyczne z produkcją

### Przykład 1: Podstawowy docker-compose.yml dla aplikacji Python

```yaml
# docker-compose.yml - plik konfiguracyjny Docker Compose

version: '3.8'

services:
  # Serwis backend (aplikacja Python)
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: myapp-backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@database:5432/myapp
      - REDIS_URL=redis://cache:6379/0
    depends_on:
      - database
      - cache
    networks:
      - app-network
    volumes:
      - ./backend:/app
    restart: unless-stopped
    command: python main.py

  # Serwis bazy danych PostgreSQL
  database:
    image: postgres:15-alpine
    container_name: myapp-db
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=myapp
    ports:
      - "5432:5432"
    networks:
      - app-network
    volumes:
      - postgres-data:/var/lib/postgresql/data
    restart: unless-stopped

  # Serwis cache Redis
  cache:
    image: redis:7-alpine
    container_name: myapp-cache
    ports:
      - "6379:6379"
    networks:
      - app-network
    volumes:
      - redis-data:/data
    restart: unless-stopped

# Definicja sieci
networks:
  app-network:
    driver: bridge

# Definicja wolumenów (trwałe dane)
volumes:
  postgres-data:
  redis-data:
```

```python
# backend/main.py - aplikacja używająca zmiennych z docker-compose
import os
from aiohttp import web
import asyncpg
import aioredis

# Odczyt zmiennych środowiskowych z docker-compose.yml
DATABASE_URL = os.getenv('DATABASE_URL')
REDIS_URL = os.getenv('REDIS_URL')

async def init_db(app):
    """Inicjalizacja połączenia z bazą danych przy starcie"""
    app['db'] = await asyncpg.create_pool(DATABASE_URL)
    print("✓ Połączono z PostgreSQL")

async def init_cache(app):
    """Inicjalizacja połączenia z Redis przy starcie"""
    app['cache'] = await aioredis.create_redis_pool(REDIS_URL)
    print("✓ Połączono z Redis")

async def close_db(app):
    """Zamknięcie połączenia przy zatrzymaniu"""
    await app['db'].close()

async def close_cache(app):
    """Zamknięcie połączenia Redis"""
    app['cache'].close()
    await app['cache'].wait_closed()

async def health_check(request):
    """Endpoint sprawdzający połączenia z bazą i cache"""
    app = request.app

    # Test połączenia z bazą
    try:
        async with app['db'].acquire() as conn:
            await conn.fetchval('SELECT 1')
        db_status = "OK"
    except Exception as e:
        db_status = f"ERROR: {e}"

    # Test połączenia z Redis
    try:
        await app['cache'].ping()
        cache_status = "OK"
    except Exception as e:
        cache_status = f"ERROR: {e}"

    return web.json_response({
        "status": "healthy",
        "database": db_status,
        "cache": cache_status
    })

# Konfiguracja aplikacji
app = web.Application()
app.router.add_get('/health', health_check)

# Lifecycle hooks
app.on_startup.append(init_db)
app.on_startup.append(init_cache)
app.on_cleanup.append(close_db)
app.on_cleanup.append(close_cache)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8000)
```

**Komendy Docker Compose:**
```bash
# Uruchomienie wszystkich serwisów
docker-compose up

# Uruchomienie w tle
docker-compose up -d

# Zatrzymanie wszystkich serwisów
docker-compose down

# Zatrzymanie i usunięcie wolumenów (kasuje dane!)
docker-compose down -v

# Zobacz logi wszystkich serwisów
docker-compose logs

# Logi konkretnego serwisu
docker-compose logs backend

# Logi w czasie rzeczywistym
docker-compose logs -f

# Restartowanie serwisu
docker-compose restart backend

# Przebudowanie obrazów
docker-compose build

# Przebudowanie i uruchomienie
docker-compose up --build

# Listowanie uruchomionych serwisów
docker-compose ps
```

### Przykład 2: Docker Compose z wieloma środowiskami

```yaml
# docker-compose.yml - konfiguracja bazowa

version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "${BACKEND_PORT:-8000}:8000"
    environment:
      - ENV=${ENV:-development}
    env_file:
      - .env

  database:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    env_file:
      - .env
```

```yaml
# docker-compose.override.yml - automatycznie używany w development
# Ten plik nadpisuje wartości z docker-compose.yml

version: '3.8'

services:
  backend:
    volumes:
      - ./backend:/app  # Hot reload dla developmentu
    environment:
      - DEBUG=true
    command: python main.py --reload

  database:
    ports:
      - "5432:5432"  # Wyeksponuj port w dev
```

```yaml
# docker-compose.prod.yml - produkcja
# Użycie: docker-compose -f docker-compose.yml -f docker-compose.prod.yml up

version: '3.8'

services:
  backend:
    restart: always
    environment:
      - DEBUG=false
    # Brak volume mounting - obraz zawiera cały kod

  database:
    # W produkcji nie eksponujemy portów publicznie
    # ports: []  # usuwa mapowanie portów
    restart: always
```

```python
# Skrypt Python do zarządzania środowiskami
import os
import subprocess

def run_compose(environment='dev'):
    """
    Uruchamia docker-compose z odpowiednią konfiguracją

    Args:
        environment: 'dev', 'staging', 'prod'
    """
    base_cmd = ['docker-compose', '-f', 'docker-compose.yml']

    if environment == 'dev':
        # W dev używa docker-compose.override.yml automatycznie
        compose_files = []
    elif environment == 'staging':
        compose_files = ['-f', 'docker-compose.staging.yml']
    elif environment == 'prod':
        compose_files = ['-f', 'docker-compose.prod.yml']
    else:
        raise ValueError(f"Nieznane środowisko: {environment}")

    cmd = base_cmd + compose_files + ['up', '-d']

    print(f"Uruchamianie środowiska: {environment}")
    print(f"Komenda: {' '.join(cmd)}")

    subprocess.run(cmd)

# Plik .env - zmienne środowiskowe
env_example = """
# .env - plik ze zmiennymi środowiskowymi

# Środowisko
ENV=development

# Backend
BACKEND_PORT=8000
DEBUG=true

# Database
DB_PASSWORD=secret_password_change_in_production
POSTGRES_USER=postgres
POSTGRES_DB=myapp

# Redis
REDIS_PASSWORD=

# Security
SECRET_KEY=generate-random-secret-key-here
"""

print("Plik .env powinien zawierać:")
print(env_example)
```

### Przykład 3: Docker Compose z depends_on i health checks

```yaml
# docker-compose.yml z zaawansowanymi zależnościami

version: '3.8'

services:
  backend:
    build: ./backend
    depends_on:
      database:
        condition: service_healthy
      cache:
        condition: service_healthy
    environment:
      - DATABASE_URL=postgresql://postgres:secret@database:5432/myapp
    networks:
      - app-network

  database:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=myapp
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
    networks:
      - app-network

  cache:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5
    networks:
      - app-network

networks:
  app-network:
```

```python
# Skrypt pokazujący jak działa depends_on z health checks

import asyncio
import time

async def wait_for_service(service_name, health_check_fn, timeout=30):
    """
    Czeka aż serwis będzie zdrowy (healthy).
    Docker Compose robi to automatycznie z health checks.

    Args:
        service_name: nazwa serwisu
        health_check_fn: funkcja sprawdzająca czy serwis działa
        timeout: maksymalny czas oczekiwania w sekundach
    """
    print(f"⏳ Czekam na {service_name}...")
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            is_healthy = await health_check_fn()
            if is_healthy:
                print(f"✓ {service_name} jest gotowy!")
                return True
        except Exception as e:
            print(f"  {service_name} jeszcze nie gotowy: {e}")

        await asyncio.sleep(2)

    print(f"✗ Timeout: {service_name} nie odpowiada po {timeout}s")
    return False

async def check_postgres_health():
    """Health check dla PostgreSQL"""
    import asyncpg
    try:
        conn = await asyncpg.connect(
            host='database',
            port=5432,
            user='postgres',
            password='secret',
            database='myapp',
            timeout=2
        )
        await conn.fetchval('SELECT 1')
        await conn.close()
        return True
    except:
        return False

async def check_redis_health():
    """Health check dla Redis"""
    import aioredis
    try:
        redis = await aioredis.create_redis_pool('redis://cache:6379', timeout=2)
        await redis.ping()
        redis.close()
        await redis.wait_closed()
        return True
    except:
        return False

async def startup_sequence():
    """
    Sekwencja startowa aplikacji - czeka na zależności.
    Docker Compose z depends_on + healthcheck robi to automatycznie!
    """
    print("=== Startowanie aplikacji ===\n")

    # Czekaj na bazę danych
    db_ready = await wait_for_service('PostgreSQL', check_postgres_health)
    if not db_ready:
        raise Exception("Nie można połączyć się z bazą danych")

    # Czekaj na cache
    cache_ready = await wait_for_service('Redis', check_redis_health)
    if not cache_ready:
        raise Exception("Nie można połączyć się z Redis")

    print("\n✓ Wszystkie zależności gotowe - uruchamiam aplikację!")

# asyncio.run(startup_sequence())
```

### Diagram Docker Compose

```mermaid-code
graph TB
    COMPOSE[docker-compose.yml]

    COMPOSE -->|definiuje| NET[Sieć: app-network]
    COMPOSE -->|definiuje| VOL1[Wolumin: postgres-data]
    COMPOSE -->|definiuje| VOL2[Wolumin: redis-data]

    COMPOSE -->|uruchamia| BE[Backend Container]
    COMPOSE -->|uruchamia| DB[Database Container]
    COMPOSE -->|uruchamia| CACHE[Redis Container]

    BE -->|depends_on| DB
    BE -->|depends_on| CACHE

    DB -->|używa| VOL1
    CACHE -->|używa| VOL2

    BE -->|łączy się| NET
    DB -->|łączy się| NET
    CACHE -->|łączy się| NET

    style COMPOSE fill:#ffe6cc
    style NET fill:#e6f3ff
    style VOL1 fill:#ffe6f0
    style VOL2 fill:#ffe6f0
```

![[Screenshot 2025-12-02 at 18.29.16.png]]




> [!tip]
> **Profiles w Docker Compose**: Możesz definiować profile, aby uruchamiać tylko wybrane serwisy:
> ```yaml
> services:
>   backend:
>     # ...
>
>   test-db:
>     profiles: ["testing"]
>     image: postgres:15-alpine
> ```
> Uruchomienie: `docker-compose --profile testing up`

> [!warning]
> **Wersja docker-compose.yml**: Używaj wersji 3.8+. Starsze wersje (2.x) mają inne składnię i możliwości.

> [!info]
> **Alternatywa: docker compose (v2)**: Nowsze wersje Docker mają wbudowany `docker compose` (bez myślnika) zamiast oddzielnego narzędzia `docker-compose`.

---

## **5. Ćwiczenie: Aplikacja w Kontenerze**

### Wprowadzenie

Teraz stworzymy kompletną aplikację blog API z Django REST Framework działającą w kontenerach Docker z bazą danych PostgreSQL, Redis cache i Nginx jako reverse proxy.

### Przykład 1: Struktura projektu

```python
"""
Struktura projektu:

blog-api/
├── docker-compose.yml
├── .env
├── .dockerignore
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── blog/
│       ├── __init__.py
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
└── nginx/
    ├── Dockerfile
    └── nginx.conf
"""

# .env - zmienne środowiskowe
env_content = """
# PostgreSQL
POSTGRES_DB=blogdb
POSTGRES_USER=bloguser
POSTGRES_PASSWORD=strong_password_here
DATABASE_URL=postgresql://bloguser:strong_password_here@database:5432/blogdb

# Django
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Redis
REDIS_URL=redis://cache:6379/0
"""

# .dockerignore
dockerignore_content = """
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
.env
.venv/
venv/
.git/
.gitignore
*.md
.vscode/
.idea/
*.sqlite3
"""

print("Podstawowa struktura projektu:")
print("- backend/ - kod Django aplikacji")
print("- nginx/ - konfiguracja reverse proxy")
print("- docker-compose.yml - orkiestracja kontenerów")
print("- .env - zmienne środowiskowe")
```

### Przykład 2: Backend - Django w kontenerze

```python
# backend/requirements.txt
requirements = """
Django==4.2.0
djangorestframework==3.14.0
psycopg2-binary==2.9.6
redis==4.5.5
django-redis==5.2.0
gunicorn==20.1.0
"""

# backend/Dockerfile
dockerfile = """
FROM python:3.11-slim

# Zmienne środowiskowe
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Instalacja zależności systemowych dla psycopg2
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    musl-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalacja zależności Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Kopiowanie kodu
COPY . .

# Utworzenie użytkownika
RUN useradd -m -u 1000 django && \
    chown -R django:django /app
USER django

EXPOSE 8000

# Skrypt startowy
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
"""

# backend/config/settings.py (fragmenty)
settings_code = """
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blog',
]

# PostgreSQL z docker-compose
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'database',  # Nazwa serwisu w docker-compose
        'PORT': '5432',
    }
}

# Redis cache
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv('REDIS_URL'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
"""

# backend/blog/models.py
models_code = """
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
"""

# backend/blog/serializers.py
serializers_code = """
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'published']
        read_only_fields = ['id', 'created_at', 'updated_at']
"""

# backend/blog/views.py
views_code = """
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.cache import cache
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        # Sprawdź cache
        cache_key = 'posts_list'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response({'source': 'cache', 'data': cached_data})

        # Jeśli nie ma w cache, pobierz z bazy
        queryset = self.get_queryset().filter(published=True)
        serializer = self.get_serializer(queryset, many=True)

        # Zapisz do cache na 5 minut
        cache.set(cache_key, serializer.data, 300)

        return Response({'source': 'database', 'data': serializer.data})

    @action(detail=False, methods=['post'])
    def clear_cache(self, request):
        cache.clear()
        return Response({'message': 'Cache cleared'})
"""

print("Django aplikacja z PostgreSQL i Redis cache")
```

### Przykład 3: Kompletny docker-compose.yml

```yaml
# docker-compose.yml - kompletna aplikacja

version: '3.8'

services:
  # Backend Django
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: blog-backend
    command: >
      sh -c "python manage.py migrate &&
             python manage.py collectstatic --noinput &&
             gunicorn config.wsgi:application --bind 0.0.0.0:8000"
    volumes:
      - ./backend:/app
      - static-files:/app/staticfiles
    env_file:
      - .env
    depends_on:
      database:
        condition: service_healthy
      cache:
        condition: service_healthy
    networks:
      - blog-network
    restart: unless-stopped

  # PostgreSQL database
  database:
    image: postgres:15-alpine
    container_name: blog-database
    volumes:
      - postgres-data:/var/lib/postgresql/data
    env_file:
      - .env
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - blog-network
    restart: unless-stopped

  # Redis cache
  cache:
    image: redis:7-alpine
    container_name: blog-cache
    volumes:
      - redis-data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5
    networks:
      - blog-network
    restart: unless-stopped

  # Nginx reverse proxy
  nginx:
    build:
      context: ./nginx
      dockerfile: Dockerfile
    container_name: blog-nginx
    ports:
      - "80:80"
    volumes:
      - static-files:/static
    depends_on:
      - backend
    networks:
      - blog-network
    restart: unless-stopped

networks:
  blog-network:
    driver: bridge

volumes:
  postgres-data:
  redis-data:
  static-files:
```

```python
# nginx/nginx.conf
nginx_config = """
upstream backend {
    server backend:8000;
}

server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /static/;
    }

    location /health {
        access_log off;
        return 200 "healthy\\n";
        add_header Content-Type text/plain;
    }
}
"""

# nginx/Dockerfile
nginx_dockerfile = """
FROM nginx:1.25-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
"""

# Skrypt uruchamiający projekt
startup_script = """
#!/bin/bash

# Skrypt uruchamiający blog-api

echo "🐳 Uruchamianie Blog API..."

# Sprawdzenie czy Docker działa
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker nie jest uruchomiony. Uruchom Docker Desktop."
    exit 1
fi

# Zatrzymanie starych kontenerów
echo "🛑 Zatrzymywanie starych kontenerów..."
docker-compose down

# Budowanie obrazów
echo "🔨 Budowanie obrazów Docker..."
docker-compose build

# Uruchomienie
echo "🚀 Uruchamianie kontenerów..."
docker-compose up -d

# Czekanie na backend
echo "⏳ Czekanie na backend..."
sleep 10

# Sprawdzenie statusu
echo ""
echo "📊 Status kontenerów:"
docker-compose ps

echo ""
echo "✅ Aplikacja uruchomiona!"
echo ""
echo "🌐 Dostępne endpointy:"
echo "   http://localhost/api/posts/     - Lista postów"
echo "   http://localhost/admin/         - Panel administracyjny"
echo "   http://localhost/health         - Health check"
echo ""
echo "📝 Przydatne komendy:"
echo "   docker-compose logs -f          - Logi wszystkich serwisów"
echo "   docker-compose exec backend python manage.py createsuperuser"
echo "   docker-compose down             - Zatrzymanie"
"""

print("Kompletna aplikacja Blog API z Docker Compose")
print("\nArchitektura:")
print("  Client → Nginx (port 80) → Django Backend (port 8000)")
print("                              ↓         ↓")
print("                          PostgreSQL  Redis")
```

### Diagram kompletnej aplikacji

```mermaid-code
graph TB
    USER[👤 User] -->|HTTP :80| NGINX

    subgraph "Docker Compose"
        subgraph "blog-network"
            NGINX[🌐 Nginx<br/>Reverse Proxy]
            BACKEND[🐍 Django Backend<br/>:8000]
            DB[(🗄️ PostgreSQL<br/>:5432)]
            CACHE[(⚡ Redis<br/>:6379)]
        end

        NGINX -->|proxy_pass| BACKEND
        BACKEND -->|SQL queries| DB
        BACKEND -->|cache| CACHE

        VOL1[📦 postgres-data]
        VOL2[📦 redis-data]
        VOL3[📦 static-files]

        DB -.->|persists| VOL1
        CACHE -.->|persists| VOL2
        BACKEND -.->|writes| VOL3
        NGINX -.->|serves| VOL3
    end

    style USER fill:#e1f5ff
    style NGINX fill:#fff3e0
    style BACKEND fill:#e8f5e9
    style DB fill:#fce4ec
    style CACHE fill:#fff9c4
```


![[Screenshot 2025-12-02 at 18.29.52.png]]




> [!tip]
> **Debugowanie w kontenerze**: Aby debugować aplikację w kontenerze:
> ```bash
> # Wejdź do kontenera
> docker-compose exec backend bash
>
> # Uruchom Django shell
> python manage.py shell
>
> # Sprawdź logi
> docker-compose logs -f backend
> ```

> [!warning]
> **Dane w kontenerach są efemeryczne!** Bez wolumenów wszystkie dane znikną po usunięciu kontenera. Zawsze używaj wolumenów dla baz danych.

> [!info]
> **Produkcja**: W produkcji używaj zmiennych środowiskowych z secrets management (np. AWS Secrets Manager, HashiCorp Vault), nie pliku .env w repozytorium.

---

## **🤖 Wykorzystanie AI**

Docker świetnie współpracuje z aplikacjami AI. Możesz konteneryzować:

### OpenAI API w kontenerze

```python
# Aplikacja używająca OpenAI API w kontenerze
import os
from openai import AsyncOpenAI
from aiohttp import web

client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))

async def chat_endpoint(request):
    """Endpoint chatbot wykorzystujący GPT-4"""
    data = await request.json()
    user_message = data.get('message')

    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem."},
            {"role": "user", "content": user_message}
        ]
    )

    return web.json_response({
        "response": response.choices[0].message.content
    })

app = web.Application()
app.router.add_post('/chat', chat_endpoint)
```

**docker-compose.yml z AI:**
```yaml
services:
  ai-backend:
    build: ./backend
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    # Pozostała konfiguracja...
```

### Modele ML w kontenerach

```python
# Aplikacja z modelem ML (np. z Hugging Face)
from transformers import pipeline

# Załaduj model przy starcie kontenera
classifier = pipeline("sentiment-analysis")

async def analyze_sentiment(request):
    data = await request.json()
    text = data.get('text')

    result = classifier(text)

    return web.json_response(result)
```

> [!note]
> **GPU w Docker**: Docker obsługuje GPU (NVIDIA) dla trenowania modeli ML. Wymaga nvidia-docker i odpowiedniej konfiguracji.

---

## **🧪 Zadania do Samodzielnej Pracy**

### ✏️ Zadania podstawowe (1-8)

1. **✏️ Zadanie 1 – Pierwszy kontener**

   Stwórz prosty Dockerfile dla aplikacji Python, która wyświetla "Hello, Docker!". Zbuduj obraz i uruchom kontener.

   (proste)

2. **✏️ Zadanie 2 – Zmienne środowiskowe**

   Zmodyfikuj kontener z zadania 1, aby przyjmował zmienną środowiskową `NAME` i wyświetlał "Hello, {NAME}!". Uruchom kontener z różnymi wartościami.

   (proste)

3. **✏️ Zadanie 3 – Mapowanie portów**

   Stwórz prosty serwer HTTP w Python (aiohttp), który nasłuchuje na porcie 8000. Uruchom w kontenerze i zmapuj na port 3000 hosta.

   (proste)

4. **✏️ Zadanie 4 – Wolumin dla danych**

   Stwórz kontener, który zapisuje logi do pliku. Użyj woluminu, aby logi przetrwały restart kontenera.

   (proste)

5. **✏️ Zadanie 5 – Multi-stage build**

   Przepisz Dockerfile z zadania 3 używając multi-stage build. Porównaj rozmiary obrazów.

   (proste)

6. **✏️ Zadanie 6 – Docker Compose podstawowy**

   Stwórz docker-compose.yml dla aplikacji z dwoma serwisami: backend (Python) i database (PostgreSQL). Backend powinien połączyć się z bazą.

   (proste)

7. **✏️ Zadanie 7 – Health checks**

   Dodaj health check do serwisu PostgreSQL w docker-compose.yml. Backend powinien czekać aż baza będzie zdrowa (`depends_on` z `condition`).

   (proste)

8. **✏️ Zadanie 8 – Sieć niestandardowa**

   Stwórz dwa kontenery w niestandardowej sieci bridge. Sprawdź, czy mogą się komunikować po nazwach.

   (proste)

### ✏️ Zadania średnie (9-12)

9. **✏️ Zadanie 9 – API z cache**

   Stwórz aplikację API (aiohttp/FastAPI) z Redis cache. Pierwszy request pobiera z "bazy" (symulacja), kolejne z cache. Użyj docker-compose.

   Serwisy: backend, redis

   (średnie)

10. **✏️ Zadanie 10 – CRUD API w kontenerach**

    Stwórz pełne CRUD API (Create, Read, Update, Delete) dla prostej encji (np. książki) używając Django/FastAPI + PostgreSQL. Wszystko w docker-compose.

    Endpointy: GET /books, POST /books, PUT /books/{id}, DELETE /books/{id}

    (średnie)

11. **✏️ Zadanie 11 – Nginx reverse proxy**

    Dodaj Nginx jako reverse proxy przed backend z zadania 10. Nginx powinien przekierowywać requesty do backendu i serwować pliki statyczne.

    (średnie)

12. **✏️ Zadanie 12 – Środowiska dev/prod**

    Stwórz dwa pliki: docker-compose.yml (bazowy) i docker-compose.prod.yml (produkcja). W dev montuj kod jako volume (hot reload), w prod nie. Przetestuj oba.

    (średnie)

### 🧠 Zadania wyzwanie (13-20)

13. **🧠 Zadanie 13 – Mikroservices architecture**

    Stwórz architekturę mikroserwisów z 3 serwisami:
    - **users-service** (zarządzanie użytkownikami)
    - **posts-service** (posty użytkowników)
    - **api-gateway** (agreguje dane z obu serwisów)

    Każdy serwis ma swoją bazę danych (pattern: database per service). Użyj docker-compose.

    (challenge)

14. **🧠 Zadanie 14 – Message queue z Celery**

    Stwórz aplikację z Django + Celery + Redis jako broker. Backend przyjmuje zadania (np. generowanie raportu), Celery worker je przetwarza w tle. Wszystko w kontenerach.

    Serwisy: backend, celery-worker, redis, database

    (challenge)

15. **🧠 Zadanie 15 – Monitoring z Prometheus**

    Dodaj monitoring do aplikacji z zadania 10. Użyj Prometheus do zbierania metryk i Grafana do wizualizacji. Backend powinien eksponować endpoint `/metrics`.

    Serwisy: backend, database, prometheus, grafana

    (challenge)

16. **🧠 Zadanie 16 – Scaling serwisów**

    Zmodyfikuj docker-compose.yml z zadania 11, aby uruchamiał 3 instancje backendu. Nginx powinien load balancować między nimi (round-robin).

    Użyj: `docker-compose up --scale backend=3`

    (challenge)

17. **🧠 Zadanie 17 – CI/CD pipeline**

    Stwórz GitHub Actions workflow, który:
    - Buduje obraz Docker
    - Uruchamia testy w kontenerze
    - Pushuje obraz do Docker Hub (jeśli testy przeszły)

    (challenge)

18. **🧠 Zadanie 18 – WebSocket chat w kontenerach**

    Stwórz aplikację chat w czasie rzeczywistym (WebSocket) z Redis Pub/Sub do komunikacji między instancjami. Uruchom wiele instancji backendu - użytkownicy w różnych instancjach powinni się widzieć.

    Serwisy: backend (x3), redis, nginx

    (challenge)

19. **🧠 Zadanie 19 – Init containers pattern**

    Stwórz init container, który przed startem backendu:
    - Czeka aż baza będzie dostępna
    - Uruchamia migracje
    - Tworzy superusera (jeśli nie istnieje)

    Wykorzystaj Docker Compose `depends_on` i custom entrypoint scripts.

    (challenge)

20. **🧠 Zadanie 20 – Full-stack app z AI**

    Stwórz kompletną aplikację full-stack:
    - **Frontend**: React/Vue w kontenerze (Nginx)
    - **Backend**: FastAPI z endpoint do AI (OpenAI API / Ollama local)
    - **Database**: PostgreSQL
    - **Cache**: Redis
    - **Queue**: Celery dla długich zadań AI

    Aplikacja: System rekomendacji książek wykorzystujący embeddings z OpenAI.

    (challenge)

---

## **📚 Podsumowanie**

W tej lekcji nauczyłeś się:

### Kluczowe Koncepcje

- **Konteneryzacja vs Wirtualizacja**: Kontenery są lżejsze i szybsze niż VM, ale współdzielą kernel hosta
- **Docker**: Platforma do tworzenia, wdrażania i uruchamiania aplikacji w kontenerach
- **Dockerfile**: Plik z instrukcjami budowania obrazu (FROM, COPY, RUN, CMD, EXPOSE)
- **Multi-stage build**: Technika tworzenia mniejszych obrazów produkcyjnych
- **Sieci Docker**: Kontenery komunikują się po nazwach w niestandardowych sieciach bridge
- **Docker Compose**: Narzędzie do definiowania wielokontenerowych aplikacji w YAML

### Praktyczne Umiejętności

- Pisanie efektywnych Dockerfile (cachowanie warstw, multi-stage)
- Konfiguracja sieci i komunikacji między kontenerami
- Używanie Docker Compose do orkiestracji serwisów
- Zarządzanie zależnościami z `depends_on` i health checks
- Używanie wolumenów do persystencji danych
- Konfiguracja różnych środowisk (dev/staging/prod)

### Powiązanie z Poprzednimi Lekcjami

Docker świetnie współgra z tym, czego się już nauczyłeś:

- **Aiohttp/FastAPI** → Idealne do konteneryzacji (małe obrazy, szybki start)
- **PostgreSQL** → Oficjalny obraz Docker, łatwa konfiguracja
- **Redis** → Używany jako cache i message broker w kontenerach
- **AWS/DevOps** → Docker to fundament CI/CD i cloud deployments

