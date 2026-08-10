# Wątki, Procesy i GIL w Pythonie

## 1. Wprowadzenie

Współbieżność w aplikacjach backendowych jest koniecznością wynikającą z architektury współczesnych systemów sieciowych. Serwer webowy rzadko wykonuje jedno zadanie na raz. W tym samym momencie musi obsługiwać zapytania HTTP od setek lub tysięcy unikalnych użytkowników, rozmawiać z bazą danych, wysyłać zapytania do zewnętrznych API oraz przetwarzać pliki.

Zrozumienie sposobu, w jaki system operacyjny i interpreter Pythona zarządzają zadaniami, pozwala uniknąć wąskich gardeł (bottlenecks) oraz błędów związanych z nieprawidłowym dostępem do danych.

### Współbieżność (Concurrency) a Równoległość (Parallelism)

Te dwa pojęcia są często błędnie używane zamiennie, podczas gdy określają inne zjawiska:

* **Współbieżność (Concurrency):** Dotyczy struktury aplikacji. To zdolność do zarządzania wieloma zadaniami jednocześnie poprzez przełączanie się między nimi. Zadania mogą startować, działać i kończyć się w pokrywających się przedziałach czasowych, ale niekoniecznie wykonują się w tym samym ułamku sekundy na poziomie sprzętowym. Przykładowo: procesor wykonuje fragment zadania A, przerywa, wykonuje fragment zadania B, po czym wraca do A.
* **Równoległość (Parallelism):** Dotyczy fizycznego wykonania. To sytuacja, w której co najmniej dwa zadania są przetwarzane w dokładnie tym samym momencie. Wymaga to fizycznie wielordzeniowego procesora (CPU) lub wielu procesorów, gdzie każdy rdzeń wykonuje instrukcje przypisanego do niego zadania.

```
Współbieżność (1 rdzeń, przełączanie kontekstu):
Zadanie A: [---]      [---]
Zadanie B:     [---]      [---]

Równoległość (Wiele rdzeni, jednoczesne działanie):
Rdzeń 1 (Zadanie A): [--------]
Rdzeń 2 (Zadanie B): [--------]

```

### Kontekst aplikacji backendowych (Django, FastAPI)

Tradycyjne serwery aplikacji, takie jak Gunicorn (obsługujący Django przez interfejs WSGI) lub Uvicorn (obsługujący FastAPI przez ASGI), wykorzystują różne modele obsługi ruchu wieloużytkowniczego.

Gdy użytkownik wysyła zapytanie do bazy danych, które zajmuje 200 ms, procesor serwera przez 99% tego czasu nie wykonuje żadnych obliczeń – czeka na odpowiedź z sieci. Bez mechanizmów współbieżności serwer byłby zablokowany i żaden inny użytkownik nie otrzymałby odpowiedzi, dopóki poprzednie zapytanie nie zostanie w pełni obsłużone. Wybór między wątkami a procesami decyduje o wydajności i zużyciu pamięci RAM na serwerze produkcyjnym.

---

## 2. Procesy i wątki

System operacyjny zarządza dwoma podstawowymi jednostkami wykonawczymi: procesami i wątkami.

### Proces (Process)

Proces to odizolowany program uruchomiony w systemie operacyjnym. Posiada on:

* Własną, całkowicie odseparowaną przestrzeń adresową pamięci RAM. Jeden proces nie ma bezpośredniego dostępu do zmiennych i obiektów drugiego procesu.
* Własną instancję interpretera Pythona.
* Własny mechanizm GIL (Global Interpreter Lock).
* Własne deskryptory plików i zasoby sieciowe.

Koszt utworzenia (fork/spawn) procesu jest wysoki pod kątem czasu procesora oraz zużycia pamięci RAM, ponieważ system musi zaalokować zupełnie nową przestrzeń dla struktur interpretera. W architekturze backendowej procesy reprezentowane są np. przez niezależne workery Gunicorna.

### Wątek (Thread)

Wątek to najmniejsza jednostka wykonawcza wewnątrz procesu. Czasami nazywany jest "lekkim procesem". Wątki uruchomione w ramach jednego procesu:

* **Współdzielą tę samą przestrzeń pamięci RAM.** Wszystkie wątki jednego procesu widzą te same zmienne globalne, obiekty i stan aplikacji.
* Dzielą ten sam interpreter Pythona i ten sam GIL.
* Są znacznie tańsze w tworzeniu i przełączaniu (Context Switching) niż procesy.

Współdzielenie pamięci jest największą zaletą wątków (brak konieczności skomplikowanej serializacji danych przy komunikacji), ale też największym zagrożeniem (ryzyko jednoczesnej modyfikacji tej samej struktury danych).

### Porównanie struktur pamięci

```
PROCES A                                PROCES B
+----------------------------------+    +----------------------------------+
| Pamięć procesu (Odizolowana)     |    | Pamięć procesu (Odizolowana)     |
| Zmienne globalne, obiekty        |    | Zmienne globalne, obiekty        |
|                                  |    |                                  |
|  Wątek 1      Wątek 2            |    |  Wątek 1                         |
|  [Kod]        [Kod]              |    |  [Kod]                           |
+----------------------------------+    +----------------------------------+

```

| Cecha                       | Wątek (Thread)                                  | Proces (Process)                               |
| --------------------------- | ----------------------------------------------- | ---------------------------------------------- |
| **Przestrzeń pamięci**      | Współdzielona w ramach jednego procesu          | Całkowicie odizolowana                         |
| **Koszt utworzenia**        | Niski (lekki)                                   | Wysoki (ciężki)                                |
| **Omijanie GIL w Pythonie** | Nie                                             | Tak (każdy proces ma swój GIL)                 |
| **Komunikacja (IPC)**       | Bezpośrednia (przez pamięć)                     | Wymaga IPC (Queue, Pipes, Sockets)             |
| **Awarie**                  | Awaria jednego wątku może uszkodzić cały proces | Awaria procesu nie wpływa bezpośrednio na inne |

---

## 3. Threading

Do obsługi wątków w Pythonie służy wbudowany moduł standardowy `threading`. Klasa `Thread` pozwala na delegowanie zadań do nowych wątków.

### Podstawowe mechanizmy i API

* `target`: Funkcja, która ma zostać wykonana w wątku.
* `args`: Krotka (tuple) zawierająca argumenty przekazywane do funkcji docelowej.
* `start()`: Metoda inicjalizująca wątek i uruchamiająca funkcję `target`.
* `join()`: Blokuje wykonanie wątku głównego do momentu, aż wątek, na rzecz którego wywołano `join()`, zakończy swoje działanie.

### Przykład kodu: Podstawowe operacje wątkowe

```python
import threading
import time
import requests

def fetch_api_data(endpoint_id: int):
    print(f"[Wątek {threading.current_thread().name}] Rozpoczęto pobieranie ID: {endpoint_id}")
    # Symulacja blokującego zapytania HTTP I/O
    response = requests.get(f"https://httpbin.org/delay/1")
    print(f"[Wątek {threading.current_thread().name}] Zakończono. Status: {response.status_code}")

if __name__ == "__main__":
    start_time = time.time()
    threads = []

    # Tworzenie i uruchamianie 3 wątków
    for i in range(3):
        t = threading.Thread(target=fetch_api_data, args=(i,), name=f"Worker-{i}")
        threads.append(t)
        t.start()  # Uruchomienie wątku bez blokowania pętli głównej

    # Oczekiwanie na zakończenie wszystkich wątków
    for t in threads:
        t.join()  # Wątek główny czeka tutaj

    end_time = time.time()
    print(f"Całkowity czas wykonania: {end_time - start_time:.2f} sekund.")

```

### Cykl życia wątku (Lifecycle)

```
[Utworzenie: Thread()] ---> [Uruchomienie: start()] ---> [Stan: Gotowy/Uruchomiony]
                                                                  |
                                                      (Wykonanie operacji I/O)
                                                                  |
[Zniszczenie wątku]   <--- [Koniec funkcji target]   <--- [Stan: Zablokowany]

```

### Kiedy używać modułu threading?

Wątków używamy wyłącznie do zadań typu **I/O-bound** (ograniczonych operacjami wejścia/wyjścia). Przykłady zastosowań w backendzie:

* Wysyłanie równoległych zapytań HTTP do zewnętrznych mikroserwisów (REST API, GraphQL).
* Odczyt i zapis dużych plików na dysku (np. generowanie logów).
* Komunikacja z bazą danych lub serwerem cache (Redis, Memcached), jeśli sterownik nie wspiera asynchroniczności.

---

## 4. Daemon Threads (Wątki demona)

Wątek demona (Daemon thread) to wątek działający w tle, którego istnienie nie powstrzymuje programu głównego przed zakończeniem działania.

### Różnica między wątkiem zwykłym a demonem

* **Zwykły wątek (Non-daemon):** Python czeka na zakończenie wszystkich zwykłych wątków, zanim zamknie cały proces aplikacji.
* **Wątek demona (Daemon):** Kiedy kończy się wątek główny (oraz inne wątki niebędące demonami), Python gwałtownie zabija wszystkie istniejące wątki demona i kończy proces systemu operacyjnego.

Ustawienie wątku jako demon odbywa się poprzez przekazanie flagi `daemon=True` w konstruktorze lub ustawienie właściwości `t.daemon = True` przed wywołaniem `start()`.

### Przykład kodu: Wątek monitorujący stan aplikacji

```python
import threading
import time
import sys

def background_monitor():
    while True:
        print("[DEMON] Sprawdzanie zużycia pamięci i stanu połączeń...")
        time.sleep(0.5)

if __name__ == "__main__":
    # Uruchomienie wątku tła jako demon
    monitor_thread = threading.Thread(target=background_monitor, daemon=True)
    monitor_thread.start()

    # Symulacja głównej pracy serwera
    print("[MAIN] Serwer uruchomiony...")
    time.sleep(1.2)
    print("[MAIN] Koniec pracy serwera. Wyjście.")
    # W tym miejscu program kończy działanie. Wątek demona background_monitor zostanie przerwany natychmiast.

```

### Zastosowanie w backendzie

Wątki demona stosuje się do powtarzalnych zadań pomocniczych, które nie zapisują krytycznego stanu aplikacji:

* **Monitoring i metryki:** Wysyłanie co 10 sekund stanu zajętości pamięci RAM do zewnętrznego systemu (np. Prometheus/Grafana).
* **Background cleanup:** Czyszczenie lokalnego cache'u in-memory ze starych, nieużywanych wpisów.
* **Log rotation agent:** Odświeżanie deskryptorów plików z logami.

### Kiedy NIE używać wątków demona?

Nigdy nie należy stosować wątków demona do zadań, których nagłe przerwanie doprowadzi do niespójności danych lub strat finansowych. Ponieważ demon może zostać zabity w połowie wykonywania dowolnej linijki kodu, nie nadaje się do:

* Procesowania płatności (Payment Gateways).
* Wysyłania wiadomości e-mail / SMS (klient może nie otrzymać powiadomienia, bądź transakcja zostanie przerwana w połowie).
* Zapisywania transakcyjnych danych do baz danych lub operacji na systemie plików wymagających zachowania spójności.

---

## 5. Race Condition i synchronizacja

Współdzielenie pamięci przez wątki rodzi problem wyścigu (**Race Condition**). Sytuacja ta zachodzi, gdy co najmniej dwa wątki próbują jednocześnie odczytać i zmodyfikować tę samą komórkę pamięci, a ostateczny wynik zależy od kolejności i czasu wykonania operacji przez system operacyjny.

### Dlaczego operacja `+=` nie jest bezpieczna wątkowo?

W Pythonie operacja `counter += 1` wydaje się być pojedynczą instrukcją. W rzeczywistości interpreter CPython kompiluje ją do kilku instrukcji kodu bajtowego (bytecode):

1. `LOAD_GLOBAL` (odczytaj wartość licznika z pamięci).
2. `LOAD_CONST` (załaduj wartość 1).
3. `BINARY_OP` (dodaj wartości do siebie).
4. `STORE_GLOBAL` (zapisz nowy wynik z powrotem do pamięci).

Jeśli dwa wątki wykonają krok 1 w tym samym czasie, oba odczytają tę samą wartość początkową (np. 0). Następnie oba dodadzą 1 i zapiszą wynik 1. Ostateczna wartość wyniesie 1 zamiast prawidłowego 2. Zjawisko to ilustruje poniższy kod:

```python
import threading

shared_counter = 0

def increment_counter():
    global shared_counter
    for _ in range(100000):
        shared_counter += 1

if __name__ == "__main__":
    t1 = threading.Thread(target=increment_counter)
    t2 = threading.Thread(target=increment_counter)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    # Wynik rzadko wyniesie dokładnie 200000 z powodu race condition
    print(f"Końcowa wartość shared_counter: {shared_counter}")

```

### Lock (Blokada)

Aby zabezpieczyć sekcję krytyczną (fragment kodu, który może być wykonywany tylko przez jeden wątek naraz), stosuje się obiekt `threading.Lock`. Posiada on metody `acquire()` (pobierz blokadę) oraz `release()` (zwolnij blokadę). Rekomendowanym podejściem w Pythonie jest używanie menedżera kontekstu (`with lock:`), który gwarantuje zwolnienie blokady nawet w przypadku wystąpienia wyjątku.

```python
import threading

shared_counter = 0
counter_lock = threading.Lock()

def safe_increment_counter():
    global shared_counter
    for _ in range(100000):
        # with automatycznie wywołuje acquire() i na końcu release()
        with counter_lock:
            shared_counter += 1

if __name__ == "__main__":
    t1 = threading.Thread(target=safe_increment_counter)
    t2 = threading.Thread(target=safe_increment_counter)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Bezpieczna końcowa wartość: {shared_counter}")  # Zawsze 200000

```

### RLock (Reentrant Lock)

Standardowy `Lock` nie może zostać pobrany ponownie przez ten sam wątek, dopóki nie zostanie zwolniony. Wywołanie `acquire()` dwa razy z rzędu w tym samym wątku zablokuje ten wątek na zawsze. `RLock` (blokada wielokrotna) pozwala temu samemu wątkowi na wielokrotne pobieranie tej samej blokady. Jest przydatna przy wywołaniach rekurencyjnych lub metodach klasy, które wewnętrznie wywołują inne metody tej samej klasy zabezpieczone tym samym `RLock`.

### Semaphore (Semafor)

Semafor zarządza wewnętrznym licznikiem. Każde wywołanie `acquire()` zmniejsza licznik, a `release()` zwiększa go. Jeśli licznik spadnie do zera, kolejne wątki blokują się do momentu zwolnienia semafora.

Zastosowanie backendowe: Ograniczenie liczby jednoczesnych połączeń do zewnętrznego API o restrykcyjnym Rate Limit.

```python
import threading
import time

# Zezwól maksymalnie 2 wątkom na jednoczesny dostęp
api_semaphore = threading.Semaphore(2)

def call_external_rate_limited_api(worker_id: int):
    with api_semaphore:
        print(f"Worker {worker_id} uzyskał dostęp do API.")
        time.sleep(1)  # Symulacja zapytania
    print(f"Worker {worker_id} zwolnił slot API.")

for i in range(4):
    threading.Thread(target=call_external_rate_limited_api, args=(i,)).start()

```

### Event (Zdarzenie)

`threading.Event` to najprostszy mechanizm komunikacji flagowej między wątkami. Jeden wątek ustawia flagę (`set()`), a inne wątki czekają na jej ustawienie (`wait()`). Flagę można wyczyścić za pomocą `clear()`.

Zastosowanie: Sterowanie cyklem życia workerów tła (np. powiadomienie o konieczności natychmiastowego zatrzymania przetwarzania przy zamykaniu serwera).

---

## 6. Deadlock (Zakleszczenie)

Deadlock to sytuacja awaryjna, w której dwa lub więcej wątków zostaje permanentnie zablokowanych, ponieważ każdy z nich czeka na zwolnienie blokady trzymanej przez ten drugi.

### Jak powstaje deadlock?

Klasyczny przypadek (problem krzyżowy):

1. Wątek A przejmuje Lock 1.
2. Wątek B przejmuje Lock 2.
3. Wątek A próbuje przejąć Lock 2 (i blokuje się, bo trzyma go Wątek B).
4. Wątek B próbuje przejąć Lock 1 (i blokuje się, bo trzyma go Wątek A).

```
Wątek A ----(trzyma)----> Lock 1 <----(czeka na)---- Wątek B
   |                                                    |
(czeka na)                                           (trzyma)
   v                                                    v
Lock 2 <------------------------------------------------+

```

### Przykład kodu generującego Deadlock

```python
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_one_worker():
    with lock_a:
        print("Thread 1: Pobrał Lock A, czeka na Lock B...")
        time.sleep(0.1)  # Wymuszenie przełączenia kontekstu
        with lock_b:
            print("Thread 1: Pobrał oba locki.")

def thread_two_worker():
    with lock_b:
        print("Thread 2: Pobrał Lock B, czeka na Lock A...")
        time.sleep(0.1)
        with lock_a:
            print("Thread 2: Pobrał oba locki.")

if __name__ == "__main__":
    t1 = threading.Thread(target=thread_one_worker)
    t2 = threading.Thread(target=thread_two_worker)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Ten napis nigdy się nie pojawi - aplikacja wisi.")

```

### Jak zapobiegać zakleszczeniom?

* **Zasada spójnej kolejności blokad:** Wszystkie wątki w systemie muszą pozyskiwać te same blokady w identycznej kolejności (np. zawsze najpierw Lock A, potem Lock B).
* **Używanie timeoutów:** Zamiast bezwarunkowego blokowania za pomocą `with lock`, można używać metody `lock.acquire(timeout=2.0)`. Jeśli nie uda się pobrać blokady w wyznaczonym czasie, wątek powinien wycofać się, zwolnić swoje obecne blokady i spróbować ponownie po losowym czasie.

---

## 7. Queue i wzorzec Producer-Consumer

Najbezpieczniejszym sposobem przekazywania danych między wątkami jest eliminacja bezpośredniego dostępu do współdzielonych zmiennych na rzecz bezpiecznych wątkowo struktur danych. Klasa `queue.Queue` implementuje mechanizmy blokowania wewnętrznie, dzięki czemu nie wymaga ręcznego stosowania obiektów `Lock`.

### Wzorzec Producent-Konsument (Producer-Consumer)

* **Producer (Producent):** Generuje zadania (np. pobiera zdarzenia sieciowe lub żądania wygenerowania raportów od klientów) i umieszcza je w kolejce za pomocą `queue.put()`.
* **Consumer (Konsument/Worker):** Pobiera zadania z kolejki za pomocą `queue.get()`, przetwarza je, a po zakończeniu informuje kolejkę przez `queue.task_done()`.

### Przykład kodu: Przetwarzanie zadań w tle

```python
import threading
import queue
import time

task_queue = queue.Queue(maxsize=10)

def producer():
    for i in range(1, 6):
        print(f"[PRODUCER] Generowanie raportu dla klienta ID: {i}")
        task_queue.put(f"Raport-{i}")
        time.sleep(0.2)

def worker_consumer():
    while True:
        # get() blokuje wątek, jeśli kolejka jest pusta
        task = task_queue.get()
        print(f"[CONSUMER] Przetwarzanie: {task} przez {threading.current_thread().name}")
        time.sleep(1.0)  # Symulacja ciężkiej pracy I/O
        
        task_queue.task_done()  # Sygnał, że zadanie zostało w pełni obsłużone

if __name__ == "__main__":
    # Uruchomienie wątków konsumentów
    for i in range(2):
        t = threading.Thread(target=worker_consumer, name=f"Worker-{i}", daemon=True)
        t.start()

    # Uruchomienie producenta
    p = threading.Thread(target=producer)
    p.start()
    p.join()

    # Oczekiwanie, aż wszystkie zadania z kolejki zostaną oznaczone jako task_done()
    task_queue.join()
    print("[MAIN] Wszystkie zadania zostały przetworzone.")

```

### Zastosowanie w backendzie

Wzorzec ten jest podstawą systemów asynchronicznego przetwarzania zadań. Wewnątrz jednego procesu serwera możemy w ten sposób realizować miniaturowe potoki przetwarzania (pipeline) dla:

* Generowania plików PDF/Excel na żądanie użytkownika.
* Zapisywania logów audytowych do bazy danych w sposób nieblokujący głównego wątku żądania HTTP.
* Wysyłania webhooków do systemów zewnętrznych.

---

## 8. GIL (Global Interpreter Lock)

GIL to globalna blokada interpretera używana w **CPythonie** (standardowej i najpopularniejszej implementacji języka Python). Zapewnia ona, że **tylko jeden wątek systemu operacyjnego może wykonywać kod bajtowy Pythona w danym momencie**, nawet jeśli procesor posiada wiele fizycznych rdzeni.

### Dlaczego GIL istnieje?

GIL został wprowadzony w celu uproszczenia zarządzania pamięcią w CPythonie. CPython używa mechanizmu zliczania referencji (Reference Counting) do śledzenia alokacji obiektów. Bez globalnej blokady, operacje modyfikacji liczników referencji przez wiele wątków jednocześnie prowadziłyby do wycieków pamięci lub przedwczesnego usuwania obiektów (Memory Corruption). Wprowadzenie GIL zabezpieczyło struktury danych C i ułatwiło integrację z bibliotekami napisanymi w C/C++.

### Wpływ GIL na zadania CPU-bound i I/O-bound

Zrozumienie zachowania GIL determinuje architekturę kodu:

#### CPU-bound (Zadania ograniczone procesorem)

Mowa o zadaniach wykonujących intensywne obliczenia matematyczne, transformacje danych, kompresję, obróbkę grafiki czy parsowanie dużych obiektów JSON.

* **Wpływ GIL:** Ponieważ wątki bez przerwy rywalizują o wykonywanie kodu bajtowego Pythona, użycie modułu `threading` do zadań CPU-bound **nie przyspieszy programu**. Co więcej, program będzie działał wolniej z powodu kosztu ciągłego przełączania kontekstu blokady GIL między wątkami.

#### I/O-bound (Zadania ograniczone operacjami wejścia/wyjścia)

Mowa o zadaniach oczekujących na pakiety sieciowe, zapytania SQL do bazy danych, odpowiedzi z API zewnętrznych lub operacje dyskowe.

* **Wpływ GIL:** W momencie, gdy wątek wykonuje operację systemową wejścia/wyjścia (np. wywołanie `socket.recv()` lub `time.sleep()`), **interpreter CPython automatycznie zwalnia blokadę GIL**. Dzięki temu inny wątek może natychmiast przejąć GIL i wykonywać swój kod. Dlatego wątki w Pythonie doskonale sprawdzają się w operacjach sieciowych.

```
Wątki przy operacjach I/O (GIL uwalniany podczas czekania):

Wątek 1: [Wykonuje Python] -> [Żądanie HTTP (Zwolnienie GIL)] --------------------> [Odebranie danych (Czeka na GIL)] -> [Wykonuje Python]
Wątek 2:                       [Czeka na GIL]                 -> [Wykonuje Python] -> [Zapis na dysk (Zwolnienie GIL)]

```

---

## 9. ThreadPoolExecutor

W środowisku produkcyjnym rzadko tworzy się wątki ręcznie za pomocą klasy `Thread`. Zarządzanie powoływaniem i niszczeniem wątków generuje niepotrzebny narzut. Zamiast tego stosuje się pulę wątków z modułu standardowego `concurrent.futures`.

### Dlaczego ThreadPoolExecutor jest standardem produkcyjnym?

* **Reużywalność wątków:** Pula tworzy określoną liczbę wątków (`max_workers`) na starcie i używa ich wielokrotnie do przetwarzania napływających zadań.
* **Ograniczenie zasobów:** Zapobiega sytuacji, w której serwer tworzy tysiące wątków pod wpływem nagłego skoku ruchu, co mogłoby doprowadzić do wyczerpania pamięci RAM serwera i awarii całego systemu operacyjnego (OOM Killer).
* **Interfejs Futures:** Pozwala na łatwe pobieranie wyników i obsługę wyjątków rzuconych wewnątrz wątków.

### Metody API

* `submit(fn, *args, kwargs)`: Rejestruje funkcję do wykonania i natychmiast zwraca obiekt `Future`.
* `map(fn, *iterables)`: Odpowiednik wbudowanej funkcji `map`, wykonuje funkcję asynchronicznie na każdym elemencie iterowalnym, zachowując kolejność wyników.
* `Future.result()`: Blokuje wykonanie do momentu zakończenia zadania i zwraca wynik lub rzuca wyjątek, który wystąpił wewnątrz wątku.

### Przykład kodu: Pobieranie danych z wielu API

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import time

URLS = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/201",
    "https://httpbin.org/status/404"
]

def check_status(url: str) -> int:
    response = requests.get(url, timeout=5)
    return response.status_code

if __name__ == "__main__":
    # max_workers jest zazwyczaj dobierane jako wielokrotność liczby rdzeni dla I/O-bound
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Mapowanie zadań
        results = executor.map(check_status, URLS)
        
        print("Wyniki z metody map():")
        for res in results:
            print(f"Status: {res}")

        # Podejście z jawny submit i as_completed
        print("\nPodejście z metodą submit():")
        futures = {executor.submit(check_status, url): url for url in URLS}
        
        for future in as_completed(futures):
            url = futures[future]
            try:
                data = future.result()
                print(f"URL: {url} zwrócił status: {data}")
            except Exception as exc:
                print(f"URL: {url} wygenerował wyjątek: {exc}")

```

### Wykorzystanie w Django i FastAPI

* **Django:** Gdy zachodzi potrzeba wysłania np. powiadomień push do 5 różnych tokenów użytkownika w widoku Django, przekazanie tych zadań do `ThreadPoolExecutor` zapobiega wydłużaniu czasu odpowiedzi dla klienta (TTFB - Time to First Byte).
* **FastAPI:** Jeśli deklarujesz endpoint za pomocą standardowego synchronicznego `def` zamiast `async def`, FastAPI pod spodem automatycznie uruchamia tę funkcję w dedykowanym `ThreadPoolExecutor` (pochodzącym z biblioteki `anyio`), aby chronić asynchroniczną pętlę zdarzeń przed zablokowaniem.

---

## 10. Multiprocessing

Aby ominąć ograniczenia narzucane przez GIL i wykorzystać pełną moc wielordzeniowych procesorów do zadań obliczeniowych, należy porzucić wątki na rzecz procesów. Służy do tego moduł `multiprocessing`.

### Podstawowe użycie i struktura

Klasa `multiprocessing.Process` naśladuje interfejs modułu `threading`, lecz pod spodem wykonuje systemowe operacje klonowania procesów.

### Kluczowy wymóg: `if __name__ == "__main__":`

W systemach Windows i macOS (od wersji Python 3.8 domyślnym mechanizmem tworzenia procesu jest `spawn`), nowy proces uruchamia interpreter Pythona od zera i importuje skrypt główny. Brak warunku `if __name__ == "__main__":` doprowadzi do nieskończonej pętli tworzenia nowych podprocesów i szybkiego zawieszenia systemu operacyjnego.

### Przykład kodu: Równoległe obliczenia CPU-bound

```python
import multiprocessing
import time

def heavy_cpu_calculation(number: int) -> int:
    print(f"[Proces: {multiprocessing.current_process().pid}] Obliczanie dla {number}")
    count = 0
    for i in range(number):
        count += i
    return count

if __name__ == "__main__":
    start_time = time.time()
    processes = []
    numbers = [50000000, 50000000, 50000000]

    for num in numbers:
        p = multiprocessing.Process(target=heavy_cpu_calculation, args=(num,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    print(f"Zakończono procesy. Czas: {end_time - start_time:.2f} sekund.")

```

---

## 11. ProcessPoolExecutor i multiprocessing.Pool

Podobnie jak w przypadku wątków, do zarządzania procesami w produkcji wykorzystuje się gotowe pule procesów: `concurrent.futures.ProcessPoolExecutor` lub tradycyjne `multiprocessing.Pool`.

### Metody Pool

* `map(func, iterable)`: Blokuje do momentu zebrania wszystkich wyników, przesyła dane porcjami.
* `starmap(func, iterable)`: Podobna do `map`, ale oczekuje iterowalnej struktury z krotkami elementów jako argumenty funkcji.
* `imap(func, iterable)`: Zwraca iterator, który natychmiast udostępnia wyniki w miarę ich kończenia przez procesy (oszczędność pamięci).
* `map_async(func, iterable)`: Wersja nieblokująca, zwraca obiekt asynchroniczny.

### Przykład kodu: Przetwarzanie danych za pomocą ProcessPoolExecutor

```python
from concurrent.futures import ProcessPoolExecutor
import math
import time

def process_chunk(n: int) -> float:
    # Ciężka operacja matematyczna
    return sum(math.sqrt(i) for i in range(n))

if __name__ == "__main__":
    tasks = [10000000, 11000000, 12000000, 13000000]
    
    start = time.time()
    # Domyślnie max_workers dobiera liczbę rdzeni CPU maszyny
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_chunk, tasks))
        
    print(f"Wyniki obliczeń: {[round(r, 2) for r in results]}")
    print(f"Czas wykonania w puli procesów: {time.time() - start:.2f} s")

```

### Zastosowania backendowe

Pule procesów są niezbędne w aplikacjach backendowych przetwarzających duże wolumeny danych:

* Generowanie okresowych raportów finansowych (agregacja milionów rekordów z DB).
* Przetwarzanie grafik przesyłanych przez użytkowników (kadrowanie, kompresja zdjęć profilowych na serwerze).
* Predykcja modeli Machine Learning (uruchamianie modeli Scikit-learn/Inference).

---

## 12. IPC — komunikacja między procesami

Ponieważ procesy są całkowicie odizolowane przez system operacyjny, standardowe zmienne globalne nie mogą posłużyć do wymiany informacji. Próba modyfikacji listy globalnej w podprocesie zmieni jedynie jej kopię w pamięci tego podprocesu – proces główny nie zarejestruje zmian. Wymiana danych wymaga mechanizmów IPC (Inter-Process Communication).

### Narzędzia IPC w module multiprocessing

#### 1. `multiprocessing.Queue`

Kolejka wieloprocesowa. Dane umieszczane w kolejce są automatycznie serializowane (za pomocą biblioteki `pickle`) do bajtów, przesyłane przez potok systemowy i deserializowane w procesie odbierającym.

```python
import multiprocessing

def worker(q: multiprocessing.Queue):
    q.put({"status": "SUCCESS", "data": [1, 2, 3]})

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    print(f"Odebrano z podprocesu: {q.get()}")
    p.join()

```

#### 2. `multiprocessing.Pipe`

Zwraca parę połączeń `(conn1, conn2)`, reprezentującą dwukierunkowy tunel (duplex). Jest szybszy niż kolejka, ale przeznaczony wyłącznie do komunikacji typu punkt-punkt (między dokładnie dwoma procesami).

#### 3. `multiprocessing.Value` / `Array`

Pozwalają na alokację współdzielonej pamięci operacyjnej (Shared Memory) dla prymitywnych typów danych języka C (np. liczby całkowite, zmiennoprzecinkowe, tablice o stałym rozmiarze). Dostęp do nich jest chroniony wbudowaną blokadą niskopoziomową.

#### 4. `multiprocessing.Manager`

Uruchamia dedykowany proces serwera (Server Process), który zarządza natywnymi obiektami Pythona (listy, słowniki). Inne procesy manipulują tymi obiektami za pomocą proxy. Jest to podejście najbardziej elastyczne, ale wolniejsze ze względu na narzut sieciowo-potokowy IPC.

---

## 13. Django i FastAPI — zastosowania praktyczne

Zarządzanie współbieżnością na poziomie kodu Pythona musi współgrać z architekturą serwerów aplikacyjnych.

### Django

Django domyślnie opiera się na architekturze synchronicznej (standard WSGI).

```
[Klient] ---> [Nginx/Caddy] ---> [Gunicorn Master Process]
                                        |
                 +----------------------+----------------------+
                 v                                             v
       [Worker Process 1]                             [Worker Process 2]
     (Thread 1)  (Thread 2)                         (Thread 1)  (Thread 2)

```

* **Gunicorn i statystyki wątków:** Gunicorn zazwyczaj uruchamia model wieloprocesowy (konfiguracja `--workers`). Opcjonalnie można włączyć obsługę wątków wewnątrz każdego workera (`--threads`).
* **Global State:** Trzymanie danych w zmiennych globalnych modułów (np. `CACHE_DICT = {}`) w Django jest antywzorcem. Jeśli Worker 1 zmodyfikuje tę strukturę, Worker 2 nic o tym nie wie. Stan aplikacji musi być współdzielony przez zewnętrzne systemy (Redis, PostgreSQL).
* **Długie zadania:** Jeśli widok (view) Django potrzebuje więcej niż 1-2 sekund na wykonanie operacji tła, blokuje to zasoby workera. Takie zadania należy bezwzględnie delegować na zewnątrz procesu serwera WWW przy użyciu dedykowanych systemów kolejkowych, takich jak **Celery** lub **RQ**.

### FastAPI

FastAPI opiera się na architekturze asynchronicznej (ASGI, serwer Uvicorn).

* **Zagrożenie blokowaniem pętli zdarzeń:** Uvicorn działa w pojedynczym wątku obsługującym pętlę zdarzeń (Event Loop). Jeśli zadeklarujesz endpoint jako `async def`, a w środku wykonasz ciężkie obliczenia procesora (CPU-bound) lub użyjesz blokującej, synchronicznej biblioteki (np. starego klienta bazy danych lub `time.sleep()`), **zablokujesz cały serwer dla wszystkich użytkowników jednocześnie**.
* **Kiedy `def` a kiedy `async def`:**
* Jeśli używasz czysto asynchronicznych bibliotek (np. `httpx`, `Tortoise ORM`): stosuj `async def`.
* Jeśli musisz użyć biblioteki synchronicznej (np. `requests`, `psycopg2`): stosuj zwykłe `def`. FastAPI automatycznie przeniesie wykonanie tej funkcji do wewnętrznej puli wątków (`ThreadPoolExecutor`), dzięki czemu główna pętla zdarzeń będzie mogła dalej przetwarzać zapytania innych klientów.
* Jeśli wykonujesz operacje ciężkich obliczeń (CPU-bound): Musisz jawnie przekazać to zadanie do zewnętrznego `ProcessPoolExecutor`, niezależnie od sposobu deklaracji endpointu.



---

## 14. Podsumowanie wyboru narzędzia

Poniższa tabela stanowi jednoznaczny drogowskaz przy doborze mechanizmu współbieżności w projektowaniu backendu:

| Problem architektoniczny                      | Charakterystyka zadania       | Rekomendowane rozwiązanie                      |
| --------------------------------------------- | ----------------------------- | ---------------------------------------------- |
| **Zapytania HTTP do API, Webhooki**           | I/O-bound (Sieć)              | `ThreadPoolExecutor` (lub asynchroniczność)    |
| **Odczyt/Zapis rozproszonych logów**          | I/O-bound (Dysk)              | `ThreadPoolExecutor`                           |
| **Kompresja zdjęć, Generowanie PDF**          | CPU-bound (Procesor)          | `ProcessPoolExecutor`                          |
| **Przetwarzanie struktur DataFrame (Pandas)** | CPU-bound (Pamięć/Obliczenia) | `ProcessPoolExecutor` / `multiprocessing`      |
| **Długotrwałe zadania (powyżej 5s)**          | Praca asynchroniczna tła      | Zewnętrzna kolejka zadań (**Celery** / **RQ**) |
| **Cykliczny monitoring/Zbiór metryk**         | Praca pomocnicza w tle        | Zwykły wątek z flagą `daemon=True`             |

---

## 15. Zadania praktyczne

Wymagane jest samodzielne zaimplementowanie poniższych systemów w czystym Pythonie przy użyciu poznanych modułów standardowych.

### Projekt 1: Wielowątkowy Downloader Plików z Licznikiem Postępu

Napisz skrypt, który pobiera zawartość z zestawu testowych adresów URL w sposób współbieżny. System musi zliczać globalną liczbę pobranych bajtów i bezpiecznie aktualizować licznik.

1. **Konfiguracja infrastruktury bazowej:** Krok 1.
Zdefiniuj listę 5-10 testowych adresów URL (można wykorzystać zasób `[https://httpbin.org/bytes/1024](https://httpbin.org/bytes/1024)` generujący losowe bajty o określonej długości). Przygotuj zmienną globalną `TOTAL_BYTES_DOWNLOADED = 0` oraz obiekt typu `Lock`.


2. **Implementacja funkcji pobierającej:** Krok 2.
Stwórz funkcję wykonującą pojedyncze zapytanie przy pomocy biblioteki `requests`. Funkcja musi odczytać wielkość pobranej zawartości z nagłówka `Content-Length` lub zmierzyć długość `response.content`, a następnie wewnątrz sekcji krytycznej (`with lock:`) zaktualizować globalny licznik pobranych danych.


3. **Zarządzanie pulą wykonawczą:** Krok 3.
Użyj `ThreadPoolExecutor` z jawnym ograniczeniem `max_workers=3` do przetworzenia listy adresów. Zbierz wyniki przy użyciu `as_completed()`, aby przechwycić ewentualne błędy połączeń sieciowych (zamknięte w bloku `try-except`). Wydrukuj końcowy raport zawierający sumaryczną liczbę pobranych bajtów.


#### Kod szkieletowy do uzupełnienia dla Projektu 1:

```python
import concurrent.futures
import requests
import threading

total_bytes_downloaded = 0
bytes_lock = threading.Lock()

URLS = [f"https://httpbin.org/bytes/{size}" for size in [500, 1200, 3500, 800, 2400]]

def download_url(url: str):
    global total_bytes_downloaded
    # TODO: Zaimplementuj pobieranie, wyznacz długość danych i zaktualizuj total_bytes_downloaded przy użyciu bytes_lock
    pass

if __name__ == "__main__":
    # TODO: Uruchom ThreadPoolExecutor, przekaż zadania i wyświetl total_bytes_downloaded po zakończeniu pracy
    pass

```

---

### Projekt 2: Równoległy Generator Paczek Raportowych (CPU-bound)

Zaprojektuj system dzielący duży zakres liczb na paczki (chunks) i wyznaczający dla każdej liczby, czy jest ona liczbą pierwszą. Obliczenia muszą zostać zrównoleglone na wszystkie rdzenie procesora maszyny.

#### Wymagania implementacyjne:

1. Zaimplementuj czysto matematyczną, nieoptymalną funkcję `is_prime(n)`, która sprawdza podzielność liczby pętlą `for` od 2 do $\sqrt{n}$ (klasyczne zadanie obciążające CPU).
2. Przygotuj funkcję `process_range(start, end)`, która iteruje po podanym przedziale i zwraca listę znalezionych liczb pierwszych.
3. W funkcji głównej przygotuj duży zakres (np. od 1 000 000 do 1 500 000) i podziel go na równe fragmenty odpowiadające liczbie rdzeni CPU w systemie (pobierz ją przez `multiprocessing.cpu_count()`).
4. Wykorzystaj `ProcessPoolExecutor` do równoległego uruchomienia obliczeń dla wszystkich fragmentów.
5. Złącz wyniki cząstkowe z procesów w jedną listę końcową i zmierz całkowity czas wykonania obliczeń.

#### Kod szkieletowy do uzupełnienia dla Projektu 2:

```python
from concurrent.futures import ProcessPoolExecutor
import math
import time
import multiprocessing

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def process_range(bounds: tuple) -> list:
    start, end = bounds
    # TODO: Przetwórz przedział i zwróć listę znalezionych liczb pierwszych
    return []

if __name__ == "__main__":
    start_num = 1_000_000
    end_num = 1_300_000
    cpus = multiprocessing.cpu_count()
    
    # TODO: Przygotuj listę krotek z przedziałami (bounds) dopasowaną do liczby procesorów (cpus)
    # TODO: Uruchom ProcessPoolExecutor, przetwórz dane i porównaj czas pracy ze schematem jednowątkowym
    pass

```