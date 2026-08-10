# Lekcja: Zadania w tle i skalowanie pracy z Celery w Django (180 minut)

## Blok 1: Problem i architektura (30 minut)

Klasyczny cykl obsługi żądania HTTP w Django jest synchroniczny. Oznacza to, że proces (worker) Gunicorn/uWSGI obsługujący dany request jest zablokowany do momentu wygenerowania pełnej odpowiedzi.

`gunicorn core.wsgi:application --workers 4 --bind localhost:8000`

**Problem z długimi operacjami**
Rozważmy widok generujący raport, który zajmuje 20 sekund:

```python
import time
from django.http import JsonResponse

def generate_report(request):
    time.sleep(20)  # Symulacja długiej operacji
    return JsonResponse({"status": "done"})

```

Skutki takiego podejścia:

* Użytkownik przez 20 sekund widzi ładującą się stronę.
* Worker Django jest w pełni zablokowany.
* Jeśli serwer dysponuje 4 workerami, 4 takie requesty jednocześnie całkowicie zablokują aplikację dla wszystkich innych użytkowników.

**Niewystarczające alternatywy**

| Rozwiązanie                  | Dlaczego się nie nadaje                                                                                                                                                                 |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Osobny wątek (threading)** | Brak trwałości. Restart serwera przerywa zadania. Brak mechanizmu ponawiania (retry).                                                                                                   |
| **async/await**              | Optymalizuje operacje I/O (np. zapytania do sieci), ale nie nadaje się do ciężkich, blokujących operacji CPU (jak generowanie PDF) i nie tworzy kolejki zadań między wieloma maszynami. |
| **Cron**                     | Działa na poziomie systemu operacyjnego. Nie pozwala na dynamiczne zlecanie zadań z poziomu kodu (np. "wygeneruj raport dla tego konkretnego rekordu teraz").                           |

**Architektura Celery**
Rozwiązaniem jest system kolejkowy. Przenosimy wykonanie pracy poza cykl HTTP.

```text
  [Django]  --> 1. task.delay() -->  [Broker]
     |                                  |
 2. Zwraca id zadania                   | 3. Przechowuje kolejkę
     |                                  v
 [Użytkownik]                       [Worker Celery] --> 4. Pobiera i wykonuje zadanie

```

**Kluczowe pojęcia:**

* **Celery:** Biblioteka zarządzająca wysyłaniem, pobieraniem i wykonywaniem zadań.
* **Broker:** Zewnętrzna usługa (np. Redis, RabbitMQ), która przechowuje kolejkę komunikatów. Django i Worker nie komunikują się bezpośrednio, lecz przez brokera.
* **Worker:** Osobny proces (lub wiele procesów) Pythona, działający niezależnie od Django, który nasłuchuje na brokerze i wykonuje zadania.

**Zalety i wady**

* **Zalety:** Możliwość skalowania (dodawanie kolejnych workerów), wbudowane mechanizmy ponawiania (retry), harmonogramowanie (Beat), oddzielenie ciężkich operacji od interfejsu użytkownika.
* **Wady:** Wymaga utrzymania dodatkowej infrastruktury (Redis, procesy workerów), zwiększa złożoność wdrożenia, utrudnia debugowanie, wprowadza asynchroniczność (wynik nie jest dostępny natychmiast, co wyklucza bezpośrednie zastosowanie w architekturach realtime).

---

## Blok 2: Instalacja i konfiguracja (45 minut)

Aby system działał, należy uruchomić brokera (Redis) oraz zintegrować Celery z istniejącym projektem Django. Poniższa kolejność jest wymagana do poprawnego załadowania konfiguracji.

1. **Uruchomienie brokera Redis:** Wymaga zainstalowanego środowiska Docker.
Utwórz plik `docker-compose.yml` w głównym katalogu projektu i uruchom go poleceniem `docker compose up -d`.

```yaml
version: '3.8'
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

```


2. **Instalacja pakietów Pythona:**
Zainstaluj wymagane biblioteki w wirtualnym środowisku projektu.

```bash
pip install celery redis django

```


3. **Dodanie konfiguracji brokera do settings.py:**
Wskaż adres brokera w głównym pliku ustawień Django (`project/settings.py`).

```python
# project/settings.py

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

```


4. **Inicjalizacja aplikacji Celery:** Tworzenie pliku project/celery.py.
Utwórz plik `celery.py` w tym samym katalogu, w którym znajduje się `settings.py`. Ten plik konfiguruje instancję Celery.

```python
# project/celery.py

import os
from celery import Celery

# Ustawienie domyślnego modułu ustawień Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Pobieranie konfiguracji z settings.py (z prefiksem CELERY_)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatyczne wykrywanie zadań w plikach tasks.py we wszystkich aplikacjach
app.autodiscover_tasks()

```


5. **Rejestracja Celery podczas startu Django:** Edycja pliku project/init.py.
Zmodyfikuj plik `__init__.py` w katalogu `project`, aby upewnić się, że aplikacja Celery jest ładowana przy starcie Django. Pozwala to na używanie dekoratora `@shared_task`.

```python
# project/__init__.py

from .celery import app as celery_app

__all__ = ('celery_app',)

```


---

## Blok 3: Pierwszy działający przepływ (45 minut)

Budujemy funkcjonalność asynchronicznego generowania raportów w aplikacji `reports`.

**1. Model danych**
Zadania w tle wymagają trwałego przechowywania statusu operacji w bazie danych.

```python
# reports/models.py

from django.db import models

class Report(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("RUNNING", "Running"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Report {self.id} - {self.status}"

```

*Po dodaniu modelu wykonaj `python manage.py makemigrations` oraz `python manage.py migrate`.*

**2. Definicja zadania (Task)**
Zadania definiujemy w pliku `tasks.py` wewnątrz katalogu aplikacji.

**Krytyczna zasada:** Do zadania przekazujemy wyłącznie identyfikatory (np. `report_id`), nigdy instancje obiektów ORM.

* **Serializacja:** Obiekty ORM nie są domyślnie serializowalne do formatu JSON używanego przez brokera.
* **Nieaktualne dane (Stale Data):** Obiekt pobrany w Django może ulec zmianie w bazie zanim worker podejmie zadanie.
* **Brak współdzielenia pamięci:** Worker działa w osobnym procesie, nierzadko na innej maszynie. Nie ma dostępu do pamięci podręcznej Django.

```python
# reports/tasks.py

import time
from celery import shared_task
from .models import Report

@shared_task
def generate_report_task(report_id):
    try:
        report = Report.objects.get(id=report_id)
    except Report.DoesNotExist:
        return

    # Zmiana statusu na uruchomiony
    report.status = "RUNNING"
    report.save(update_fields=["status"])

    # Symulacja ciężkiej pracy (np. generowanie pliku, agregacja danych)
    time.sleep(10)

    # Zakończenie pracy
    report.status = "SUCCESS"
    report.save(update_fields=["status"])

```

**Znaczenie `update_fields=["status"]`:**
Podczas gdy worker generuje raport, inna część systemu (lub sam użytkownik) może zaktualizować inny atrybut tego samego rekordu w bazie. Brak `update_fields` sprawi, że worker nadpisze cały rekord danymi, które pobrał na początku zadania, ignorując zmiany wprowadzone w międzyczasie.

**3. Widok zlecający zadanie**

```python
# reports/views.py

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Report
from .tasks import generate_report_task

@require_POST
def create_report(request):
    report = Report.objects.create(status="PENDING")
    
    # Przekazanie zadania do kolejki brokera (nie blokuje wykonania)
    generate_report_task.delay(report.id)
    
    return JsonResponse({
        "id": report.id,
        "status": report.status,
        "message": "Report generation started."
    }, status=202)

def check_report_status(request, report_id):
    try:
        report = Report.objects.get(id=report_id)
        return JsonResponse({"id": report.id, "status": report.status})
    except Report.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

```

**4. Routing**

```python
# project/urls.py

from django.urls import path
from reports.views import create_report, check_report_status

urlpatterns = [
    path('reports/create/', create_report, name='create_report'),
    path('reports/<int:report_id>/status/', check_report_status, name='check_status'),
]

```

**5. Uruchomienie i weryfikacja**
Uruchom serwer Django:
`python manage.py runserver`

W nowym oknie terminala uruchom workera Celery:
`celery -A project worker -l INFO`

Weryfikacja (z użyciem curl lub Postman):

1. `curl -X POST [http://127.0.0.1:8000/reports/create/](http://127.0.0.1:8000/reports/create/)` (Zwraca natychmiast odpowiedź HTTP 202).
2. Worker podejmuje log, status w terminalu Celery zmienia się.
3. `curl [http://127.0.0.1:8000/reports/1/status/](http://127.0.0.1:8000/reports/1/status/)` (Zwraca aktualny status PENDING, RUNNING lub SUCCESS).

---

## Blok 4: Celery Beat (30 minut)

Celery Beat to wbudowany w środowisko Celery harmonogram zadań (scheduler).
**Istotna różnica:** Celery Beat **nie wykonuje** zadań. Jego jedynym celem jest wysyłanie sygnałów (komunikatów) do brokera w określonym czasie. Do wykonania tych zadań nadal niezbędny jest działający Worker.

**Architektura działania:**
`Celery Beat -> Redis (Broker) -> Celery Worker -> Wykonanie`

**Konfiguracja cyklicznego zadania**
Zdefiniujmy zadanie czyszczące stare i uszkodzone raporty.

```python
# reports/tasks.py

from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from .models import Report

@shared_task
def cleanup_old_reports():
    threshold = timezone.now() - timedelta(days=30)
    deleted, _ = Report.objects.filter(created_at__lt=threshold).delete()
    return f"Deleted {deleted} old reports."

```

Skonfiguruj harmonogram w `settings.py`. Używaj klas `crontab` do zadań zależnych od pory dnia oraz `timedelta` do interwałów. Nie używaj surowych wartości całkowitych (np. `86400`) do określania długich okresów czasu.

```python
# project/settings.py

from celery.schedules import crontab
from datetime import timedelta

CELERY_BEAT_SCHEDULE = {
    'cleanup-reports-every-night': {
        'task': 'reports.tasks.cleanup_old_reports',
        'schedule': crontab(hour=3, minute=0), # Codziennie o 3:00 w nocy
    },
    'ping-system-every-15-mins': {
        'task': 'reports.tasks.system_ping',
        'schedule': timedelta(minutes=15), # Co 15 minut
    }
}

```

Aby uruchomić system z harmonogramem, wymagane są dwa działające procesy w osobnych terminalach:

1. `celery -A project worker -l INFO`
2. `celery -A project beat -l INFO`

---

## Blok 5: Problemy produkcyjne (30 minut)

**1. Obsługa błędów i mechanizm Retry**
Połączenia z zewnętrznymi API bywają niestabilne. Task musi potrafić samodzielnie wznowić próbę wykonania w przypadku błędu. W tym celu należy użyć parametru `bind=True`, który wstrzykuje instancję aktualnego zadania jako pierwszy argument (`self`).

Nie używaj ogólnego przechwytywania `except Exception:`, ponieważ ukryje to błędy składniowe. Przechwytuj wyłącznie błędy infrastrukturalne (np. timeout połączenia).

```python
# reports/tasks.py

import requests
from requests.exceptions import RequestException
from celery import shared_task

@shared_task(bind=True, max_retries=3)
def fetch_external_data(self, endpoint_url):
    try:
        response = requests.get(endpoint_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except RequestException as exc:
        # Ponów próbę za 60 sekund
        raise self.retry(exc=exc, countdown=60)

```

**2. Idempotencja**
Idempotencja oznacza, że wielokrotne wykonanie tej samej operacji daje dokładnie taki sam rezultat końcowy jak jednokrotne jej wykonanie. W środowisku rozproszonym broker może w skrajnych przypadkach (np. restart sieci, timeout na potwierdzeniu komunikatu) wysłać to samo zadanie do workera dwukrotnie.

* **Zła implementacja:** `account.balance += 100` (Dwukrotne wywołanie doda 200).
* **Dobra implementacja:** `transaction.status = "PAID"` (Dwukrotne wywołanie nada ten sam status).

Zawsze projektuj zadania Celery tak, aby były idempotentne.

**3. Zjawisko Race Condition (Wyścig)**
Gdy istnieje wiele workerów, dwa z nich mogą pobrać ten sam zasób bazy danych jednocześnie, przetworzyć go i nadpisać nawzajem swoje wyniki.

Rozwiązaniem jest zablokowanie rekordu na poziomie bazy danych na czas transakcji przy użyciu `select_for_update()`. Funkcja ta zmusza proces do pobrania najnowszej wersji wiersza i zakłada na niego blokadę (lock), aż do zakończenia transakcji.

**Ważne:** Powyższy mechanizm działa poprawnie tylko dla systemów obsługujących współbieżne blokady na poziomie wierszy (PostgreSQL, MySQL). SQLite nie zapewnia takiego modelu blokad wierszy jak PostgreSQL/MySQL, dlatego nie powinien być używany do testowania scenariuszy wymagających współbieżności Celery, ALE na potrzeby demo będzie wystarczajacy.

```python
# reports/tasks.py

from django.db import transaction
from celery import shared_task
from .models import Report

@shared_task
def process_report_safely(report_id):
    with transaction.atomic():
        try:
            # Pobranie rekordu i zablokowanie go dla innych workerów
            report = Report.objects.select_for_update().get(id=report_id)
            
            if report.status != "PENDING":
                # Ktoś inny już zajął się tym raportem
                return "Already processed"
                
            report.status = "RUNNING"
            report.save(update_fields=["status"])
            
        except Report.DoesNotExist:
            return "Not found"
            
    # Dalsze generowanie raportu poza transakcją, aby nie blokować rekordu
    # w bazie na 20 sekund.

```

---

## Możliwości rozwoju i Limity Celery

**Możliwości rozwoju**

* **Wiele kolejek (Routing):** Zamiast jednej domyślnej kolejki, system operuje na kilku. E-maile wysyłane są na dedykowaną, szybką kolejkę (`emails`), a raporty na osobną, powolną (`reports`). Zapobiega to sytuacji, w której reset hasła musi czekać na wygenerowanie 100 raportów zeszłomiesięcznych.
* **Priorytetyzacja:** Broker (szczególnie RabbitMQ, w mniejszym stopniu Redis) pozwala nadawać priorytety komunikatom, np. zadania opłacenia faktury otrzymają wyższy priorytet niż aktualizacja statystyk.
* **Monitoring i skalowanie poziome:** Do kontroli workerów używa się narzędzia **Flower** (aplikacja webowa dająca wgląd w kolejki). Skalowanie polega na uruchamianiu procesów Celery na oddzielnych, niezależnych serwerach, które łączy tylko adres dostępowy do brokera Redis.

**Limity Celery (Czym Celery NIE jest)**

* **Nie służy do komunikacji w czasie rzeczywistym (Real-time).** Jeśli aplikacja wymaga powiadamiania użytkowników przez WebSockety o zdarzeniach natychmiastowych, używa się Django Channels lub rozwiązań takich jak zaimplementowane serwery Node.js/Go.
* **Nie jest bazą danych.** Nigdy nie przetrzymuj stanu biznesowego czy wyników operacji bezpośrednio w zadaniach Celery (backend wyników to rozwiązanie narzędziowe). Prawdziwy status i dane wynikowe zawsze muszą trafić do PostgreSQL.
* **Nie optymalizuje ciężkich obliczeń.** Jeśli zadanie wymaga gigantycznej mocy CPU (np. trenowanie ML, enkodowanie wideo w 4K), worker Celery jest wciąż jedynie programem Python i obciąży instancję w 100%. Takie operacje należy delegować do narzędzi natywnych w systemie (FFmpeg, klastry obliczeniowe Spark), używając Celery jedynie jako dyrygenta uruchamiającego ten podproces.

## Zadanie domowe
Zastanów się, w jaki sposób mógłbyś zintegrować Celery ze swoją aplikacją. 
Czy widzisz korzyści ze zintegrowania jej ze swoim projektem Django? 