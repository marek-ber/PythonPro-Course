# Zadania Praktyczne z Kursu Python

Poniżej znajduje się kompilacja zadań praktycznych z różnych modułów kursu Python, przetłumaczona na język polski i sformatowana do użytku w Obsidian.

## 1. Wykorzystanie Raw SQL i SQLAlchemy

> [!NOTE] Uwaga
> 
> Proponowane poniżej warianty są orientacyjne. Możesz użyć dowolnego wariantu w jego oryginalnej formie, zmodyfikować go lub wymyślić własny. W tych zajęciach ważna jest praktyka w pisaniu surowych zapytań SQL, łączeniu ich z kodem oraz w korzystaniu z ORM.

> [!TIP] Rekomendacja
> 
> Postaraj się poświęcić pierwszą połowę zajęć na napisanie programu z użyciem surowych zapytań SQL, a drugą część na wykorzystanie ORM.

### Wymagania Ogólne

- Implementacja aplikacji konsolowej przy użyciu **Raw SQL**.
    
- Implementacja analogicznej aplikacji z wykorzystaniem **SQLAlchemy** i **Alembic** do migracji.
    

### Projekty do wyboru

#### Wariant 1 - Biblioteka

**Funkcjonalność:**

- Opracowanie schematu bazy danych dla książek, gatunków i autorów.
    
- Proste operacje: dodawanie/usuwanie/edycja autora/książki/gatunku, wyświetlanie informacji o nich po nazwie/tytule.
    
- Złożone operacje: wyszukiwanie książek według autora lub gatunku, wyszukiwanie po częściowym dopasowaniu (tytułu/nazwiska itp.).
    

#### Wariant 2 - System Zarządzania Magazynem

**Funkcjonalność:**

- Zdefiniowanie tabel dla produktów, kategorii, dostawców i zamówień.
    
- Proste operacje: dodawanie/usuwanie/edycja produktów/dostawców/zamówień/kategorii, wyświetlanie informacji o nich.
    
- Tworzenie raportów o stanie magazynu i historii ruchu towarów.
    
- Złożone operacje: wyszukiwanie towaru według kategorii, wyszukiwanie po częściowym dopasowaniu nazwy.
    

#### Wariant 3 - Portal Edukacyjny

**Funkcjonalność:**

- Stworzenie modeli danych dla kursów, kierunków studiów/studentów, wykładowców i wyników studentów.
    
- Proste operacje: dodawanie/usuwanie/edycja kursów/wykładowców/kierunków/studentów/ocen.
    
- Analiza postępów studentów na podstawie ocen.
    
- Złożone operacje: wyszukiwanie kursu według kierunku, wyszukiwanie po częściowym dopasowaniu nazwy.
    

#### Wariant 4 - Serwis Rezerwacji Biletów

**Funkcjonalność:**

- Opracowanie schematu bazy danych dla wydarzeń, miejsc i biletów.
    
- Proste operacje: dodawanie/usuwanie/edycja wydarzeń/miejsc.
    
- Złożone operacje: wyszukiwanie wydarzenia według miejsca, wyszukiwanie po częściowym dopasowaniu nazwy.
    
- Funkcjonalność rezerwacji i anulowania biletów.
    

## 2. Flask - Zajęcia Praktyczne

> [!NOTE] Uwaga
> 
> Pierwsze zajęcia praktyczne są bardziej zorientowane na połączoną praktykę w opanowaniu frameworka i baz danych, a drugie - na praktykę używania ORM razem z frameworkami webowymi. Dlatego poniższe tematy pasują do obu zajęć.

> [!TIP] Rekomendacja
> 
> Zrealizuj oba zadania na jeden temat. W pierwszej wersji użyj surowych zapytań SQL, a w drugiej zaimplementuj to samo zadanie z użyciem ORM.

### Wymagania Ogólne

|   |   |
|---|---|
|**Zajęcia 19 (Raw SQL)**|**Zajęcia 20 (ORM)**|
|Framework: **Flask**|Framework: **Flask**|
|Baza danych: **PostgreSQL** z `psycopg2`|Baza danych: **PostgreSQL** z `psycopg2`|
|Zapytania: **Ręcznie pisany SQL**|Zapytania: **SQLAlchemy ORM**|
|Migracje: Brak (skrypt inicjalizujący)|Migracje: **Alembic**|
|Szablony: **Jinja2**|Szablony: **Jinja2**|
|Frontend: Prosty HTML, CSS (Bootstrap opcjonalnie)|Frontend: Prosty HTML, CSS (Bootstrap opcjonalnie)|
|Wersjonowanie: **Git**|Wersjonowanie: **Git**|
|Wdrożenie: Instrukcje deploymentu|Wdrożenie: Instrukcje deploymentu|

### Projekty do wyboru

#### Wariant 1 - Blog

- **Wymagane:**
    
    - Strona główna z listą wszystkich postów.
        
    - Strona do przeglądania pełnego tekstu artykułu.
        
    - Wyświetlanie komentarzy pod artykułem.
        
    - Formularz do tworzenia nowego artykułu.
        
    - Formularz do dodawania komentarzy.
        
    - Możliwość edycji i usuwania istniejącego artykułu.
        
- **Opcjonalne:**
    
    - Rejestracja i uwierzytelnianie.
        
    - Możliwość odpowiadania na komentarze.
        
    - System oceniania artykułów.
        

#### Wariant 2 - Menedżer Przepisów

- **Wymagane:**
    
    - Formularz dodawania przepisów (nazwa, kategoria, opis, czas, składniki, instrukcje, zdjęcia).
        
    - Lista przepisów z sortowaniem po kategoriach.
        
    - Wyszukiwarka przepisów.
        
    - Strona z pełnymi informacjami o przepisie.
        
    - System komentarzy.
        
    - Edycja i usuwanie przepisów.
        
- **Opcjonalne:**
    
    - Rejestracja i uwierzytelnianie.
        
    - Odpowiadanie na komentarze.
        
    - Ocenianie przepisów.
        

#### Wariant 3 - System Zarządzania Zadaniami (ToDo List)

- **Wymagane:**
    
    - Strona główna z listą zadań i sortowaniem.
        
    - Strona z pełnym opisem zadania.
        
    - Formularz tworzenia zadania (kategoria, nazwa, tekst, priorytet, status).
        
    - Edycja i usuwanie zadań.
        
- **Opcjonalne:**
    
    - Rejestracja i uwierzytelnianie.
        
    - Przypisywanie zadań do konkretnych osób.
        
    - Tworzenie list zadań (np. "na dziś", "ukończone").
        
    - Dołączanie plików do zadań.
        

#### Wariant 4 - Serwis Ankiet i Głosowań

- **Wymagane:**
    
    - Strona główna z listą ankiet.
        
    - Strona do głosowania w konkretnej ankiecie.
        
    - Tworzenie ankiet z dowolną liczbą odpowiedzi.
        
    - Anonimowe głosowanie.
        
    - Usuwanie ankiet.
        
    - Przeglądanie wyników po zagłosowaniu.
        
- **Opcjonalne:**
    
    - Rejestracja i uwierzytelnianie.
        
    - Głosowanie nieanonimowe.
        
    - Zapobieganie wielokrotnemu głosowaniu z jednego konta.
        

## 3. Django - Prosta Aplikacja

> [!NOTE] Uwaga
> 
> W tych zajęciach ważna jest praktyka w używaniu frameworka Django oraz wbudowanego systemu rejestracji i uwierzytelniania.

### Wymagania Ogólne

- Framework: **Django**
    
- Baza danych: **PostgreSQL**
    
- Konfiguracja: Zmienne środowiskowe
    
- Szablony: **Jinja2**
    
- Frontend: Prosty HTML, CSS (Bootstrap opcjonalnie)
    
- Wersjonowanie: **Git**
    
- Wdrożenie: Instrukcje deploymentu
    

### Projekty do wyboru

#### Wariant 1 - Blog

- Rejestracja i uwierzytelnianie.
    
- Strona główna z listą postów.
    
- Strona z pełnym tekstem artykułu i komentarzami.
    
- Tworzenie, edycja i usuwanie artykułów (tylko dla autora).
    
- Dodawanie komentarzy (tylko dla zalogowanych).
    
- **Opcjonalnie:** Odpowiadanie na komentarze, ocenianie artykułów.
    

#### Wariant 2 - Platforma Kursów Online

- Rejestracja użytkowników i śledzenie ich postępów.
    
- Tworzenie kursów z materiałami, tekstami i quizami.
    
- Strona główna z listą aktywnych kursów użytkownika.
    
- Strona z informacjami o kursie i formularzem zapisu.
    
- System nagród i certyfikatów po ukończeniu kursów.
    

#### Wariant 3 - System Zarządzania Nieruchomościami

- Katalog nieruchomości ze zdjęciami i opisami.
    
- Rejestracja z rolami: poszukujący lub właściciel.
    
- Dodawanie, edycja, usuwanie ofert (tylko dla właściciela).
    
- Wyszukiwanie i filtrowanie obiektów.
    
- Formularz zapytania o transakcję (wynajem/kupno).
    

#### Wariant 4 - Portal z Ofertami Pracy

- Rejestracja z rolami: firma lub kandydat.
    
- Firmy mogą publikować, edytować i usuwać ogłoszenia.
    
- Kandydaci mogą tworzyć CV i aplikować na oferty.
    
- Filtrowanie ofert i rekomendacje na podstawie profilu.
    

## 4. Django - Praktyka 2

### Wymagania Obowiązkowe dla Wszystkich Projektów

- **Rejestracja i uwierzytelnianie** (standardowe Django).
    
- **Rozbudowany panel admina:** pola wyszukiwania, inline, czytelne wyświetlanie danych.
    
- Odporność na błędy i estetyczny interfejs użytkownika.
    
- Generowanie danych testowych za pomocą **Seeder/Faker**.
    
- Komenda `management` do generowania danych.
    
- Kilka testów jednostkowych dla projektu.
    

### Projekty do wyboru

#### 1. Strona Kina

- **Modele:** Filmy, aktorzy, reżyserzy, gatunki, użytkownicy, seanse.
    
- **Funkcjonalność:** Rezerwacja biletów, przeglądanie repertuaru, informacje o filmach.
    
- **Wymagane:** `ImageField` dla zdjęć filmów, aktorów i reżyserów.
    

#### 2. Strona Muzeum

- **Modele:** Eksponaty, autorzy, epoki, użytkownicy, kategorie.
    
- **Funkcjonalność:** Przeglądanie informacji o eksponatach, wirtualne wycieczki, wyszukiwarka.
    
- **Wymagane:** `ImageField` dla zdjęć eksponatów i autorów.
    

#### 3. Portal Muzyczny

- **Modele:** Artyści, albumy, piosenki, użytkownicy, gatunki.
    
- **Funkcjonalność:** Słuchanie muzyki, przeglądanie informacji o artystach, tworzenie playlist.
    
- **Wymagane:** `ImageField` dla zdjęć albumów i artystów.
    

#### 4. Strona Biblioteki

- **Modele:** Autorzy, gatunki, książki, egzemplarze, użytkownicy.
    
- **Funkcjonalność:** Przeglądanie katalogu, informacje o książkach, rezerwacja książki na 2 tygodnie.
    
- **Wymagane:** `ImageField` dla okładek książek i zdjęć autorów.
    

## 5. DRF + Celery + Docker + CI/CD

> [!INFO]
> 
> Zadanie jest rozpisane tak, aby objąć tematy Celery, Docker i CI/CD. Projektuj funkcjonalność zgodnie z postępem w nauce, ponieważ zadanie jest przewidziane na kilka zajęć.

### Wymagania Techniczne

- **Python** >= 3.10
    
- **Django** >= 4.0
    
- **Baza danych:** PostgreSQL
    
- **Kolejki:** Celery + Redis (lub RabbitMQ)
    
- **Wersjonowanie:** Git (ważna jakość repozytorium: branche, commity, README, .gitignore)
    
- **Duży plus:** Użycie `poetry`, wdrożenie przez `docker-compose`.
    

### Zadanie

1. Zaimplementuj jeden z poniższych projektów.
    
2. "Zapakuj" go w Dockera.
    
3. Skonfiguruj CI/CD.
    

### Projekty do wyboru

#### 1. Sklep Internetowy (wersja mini)

- **Użytkownicy:** Klient, gość, menedżer.
    
- **Funkcjonalność:**
    
    - Menedżer zarządza produktami.
        
    - Gość przegląda produkty.
        
    - Klient dodaje produkty do koszyka i je usuwa.
        
    - Menedżer dodaje zniżki i kody promocyjne.
        
    - Klient może subskrybować cotygodniowy newsletter o zniżkach.
        
    - Formularz zamówienia z powiadomieniami email o dostawie.
        
- **Dodatkowo:**
    
    - Rejestracja z potwierdzeniem email.
        
    - Edycja ilości produktów w koszyku.
        
    - System cashback.
        

#### 2. Aplikacja do Monitorowania Roślin

- **Użytkownicy:** Gość, użytkownik, administrator.
    
- **Funkcjonalność:**
    
    - Gość przegląda rośliny.
        
    - Użytkownik dodaje swoje rośliny i dane o pielęgnacji (podlewanie, nawożenie).
        
    - Administrator zarządza bazą roślin i dodaje porady.
        
    - System przypomnień o pielęgnacji.
        
- **Dodatkowo:**
    
    - Rejestracja z potwierdzeniem email.
        
    - Galeria zdjęć do śledzenia wzrostu.
        
    - Dziennik do notatek.
        

#### 3. Aplikacja do Rejestrowania Treningów

- **Użytkownicy:** Gość, użytkownik, trener.
    
- **Funkcjonalność:**
    
    - Gość przegląda informacje o trenerach.
        
    - Użytkownik tworzy plany treningowe i zapisuje wyniki.
        
    - Trener tworzy programy dla użytkowników i śledzi ich postępy.
        
    - Statystyki i analiza wyników.
        
    - Przypomnienia o treningach.
        
- **Dodatkowo:**
    
    - Rejestracja z potwierdzeniem email.
        
    - Dziennik treningowy.
        
    - System ocen i opinii dla trenerów.
        

#### 4. Aplikacja do Zarządzania Finansami

- **Użytkownicy:** Gość, użytkownik, administrator.
    
- **Funkcjonalność:**
    
    - Gość poznaje możliwości aplikacji.
        
    - Użytkownik dodaje kategorie dochodów/wydatków, tworzy budżety.
        
    - Administrator zarządza kategoriami i dostarcza raporty analityczne.
        
    - Wizualizacja danych finansowych (wykresy).
        
    - Przypomnienia o płatnościach.
        
- **Dodatkowo:**
    
    - Rejestracja z potwierdzeniem email.
        
    - Eksport i import danych.
        

## 6. Aiohttp

### Wymagania Techniczne

- **Python** >= 3.10
    
- **Aiohttp** >= 3.8
    
- **Baza danych:** PostgreSQL
    
- **Frontend:** HTML/CSS/JS lub testowanie API przez Postman
    
- **Duży plus:** Użycie `poetry`, wdrożenie przez `docker-compose`.
    

### Zadanie

1. Zaimplementuj jeden z poniższych projektów.
    
2. "Zapakuj" go w Dockera.
    

### Projekty do wyboru

#### 1. Prosty System Zarządzania Zadaniami (To-Do List)

- **Funkcjonalność:**
    
    - Tworzenie nowych zadań.
        
    - Oznaczanie zadań jako wykonane.
        
    - Usuwanie zadań.
        
    - Filtrowanie zadań po statusie.
        

#### 2. API dla Biblioteki

- **Funkcjonalność:**
    
    - Operacje CRUD dla książek.
        
    - Wyszukiwanie książek po autorze, tytule, gatunku.
        

#### 3. Aplikacja Webowa do Rezerwacji

- **Funkcjonalność:**
    
    - Wyszukiwanie dostępnych usług (hotele, restauracje) po dacie i lokalizacji.
        
    - Rezerwacja z potwierdzeniem email.
        
    - Zarządzanie rezerwacjami (anulowanie, zmiana).
        

#### 4. Aplikacja do Nauki Języków

- **Funkcjonalność:**
    
    - Tworzenie i zarządzanie fiszkami.
        
    - Quizy i testy.
        
    - Śledzenie postępów użytkownika.
        

## 7. WebSockets

### Wymagania Techniczne

- **Python** >= 3.10
    
- **FastAPI**, **uvicorn**, **websockets**
    
- **Duży plus:** Użycie `poetry`, wdrożenie przez `docker-compose`.
    

### Projekty do wyboru

```
graph TD
    A[Wybierz Projekt] --> B{Panel Monitoringu};
    A --> C{Edytor Tekstu Online};
    A --> D{Czat w Czasie Rzeczywistym};
    A --> E{Gra Online (np. Kółko i Krzyżyk)};

    subgraph "Opis"
        B_desc("Wyświetlanie danych w czasie rzeczywistym (np. metryki serwera, kursy walut).");
        C_desc("Synchronizacja zmian w tekście między wieloma użytkownikami.");
        D_desc("Prosty czat do wymiany wiadomości w czasie rzeczywistym.");
        E_desc("Gra dla dwóch graczy w czasie rzeczywistym.");
    end

    B --> B_desc;
    C --> C_desc;
    D --> D_desc;
    E --> E_desc;
```

1. **Panel monitoringu w czasie rzeczywistym**
    
    - Tworzenie panelu, który wyświetla dane w czasie rzeczywistym (np. metryki serwera, kursy walut, współrzędne itp.).
        
2. **Edytor tekstu online**
    
    - Tworzenie edytora tekstu online z synchronizacją zmian w czasie rzeczywistym między użytkownikami.
        
3. **Czat w czasie rzeczywistym**
    
    - Stworzenie prostego czatu, w którym użytkownicy mogą wymieniać się wiadomościami w czasie rzeczywistym.
        
4. **Aplikacja do gier online (np. kółko i krzyżyk)**
    
    - Stworzenie aplikacji do gry w kółko i krzyżyk w czasie rzeczywistym.