## 1. Discovery / Product Definition

Prosta definicja produktu i sprawdzenie, czy problem jest realny i wart rozwiązania.

* aplikacja do szybkich notatek i kodu
* działa bez internetu
* zapis zmian dzieje się automatycznie
* priorytet: szybkość i prostota

---

## 2. Core Architecture Assumptions

Założenia, które wpływają na sposób budowy systemu.

* aplikacja działa w przeglądarce
* główny target: desktop
* praca offline musi być możliwa
* brak współpracy w czasie rzeczywistym
* obsługa klawiatury jest kluczowym sposobem interakcji
* dane nie wymagają poziomu bezpieczeństwa jak systemy krytyczne

---

## 3. User Requirements (User Stories)
`Jako [rola], chcę [cel], aby [korzyść/wartość].`
Co użytkownik chce robić w aplikacji.

* szybkie zapisywanie notatek i fragmentów kodu
* automatyczne zapisywanie bez przycisku „zapisz”
* wyszukiwanie w całej bazie notatek
* organizacja notatek w kategorie i tagi
* dostęp do notatek offline

---

## 4. Functional Specification

Co system ma robić.

* tworzenie i edycja notatek
* obsługa formatowania (Markdown + kod)
* automatyczny zapis w tle
* foldery do grupowania notatek
* tagi do elastycznej organizacji
* synchronizacja danych (w późniejszym etapie)

---

## 5. User Flow Specification

Jak użytkownik korzysta z aplikacji krok po kroku.

* użytkownik uruchamia aplikację
* logowanie lub tryb lokalny
* lista notatek i folderów
* tworzenie nowej notatki
* pisanie i automatyczny zapis
* przypisanie kategorii lub tagów
* przejście do innej notatki lub wyszukiwanie

---

## 6. Non-Functional Requirements

Wymagania dotyczące jakości działania systemu.

* bardzo szybkie przełączanie między notatkami
* brak zauważalnego opóźnienia przy pisaniu
* pełna obsługa klawiaturą
* stabilność zapisu danych
* możliwość rozwoju w kierunku szyfrowania end-to-end

---

## 7. Domain Model (Conceptual)

Jakie obiekty istnieją w systemie.

* użytkownik: właściciel danych
* notatka: tytuł, treść, historia zmian, przypisana do kategorii, może mieć tagi
* kategoria: grupuje notatki
* tag: dodatkowe oznaczenia do wyszukiwania i grupowania

---

## 8. Implementation Roadmap

Plan budowy aplikacji krok po kroku.

### 8.1. MVP (Core Value: Speed + Offline)

Sprawdzenie czy szybkie, offline narzędzie ma sens dla użytkowników.

* aplikacja działa bez logowania
* dane tylko lokalnie w przeglądarce
* tworzenie i edycja notatek
* wyszukiwanie notatek
* brak folderów i tagów
* prosty widok listy notatek

---

### 8.2. V1.0 (Sync + Organization)

Dodanie synchronizacji i porządkowania danych.

* logowanie użytkownika
* synchronizacja danych między urządzeniami
* foldery (kategorie)
* tagi
* przechowywanie danych na serwerze

---

### 8.3. V1.5+ (Desktop + Security)

Rozszerzenie systemu o wygodę i bezpieczeństwo.

* wersja desktopowa oparta na aplikacji webowej
* szyfrowanie danych end-to-end
* integracja z systemem operacyjnym
* poprawki wydajności i stabilności

---