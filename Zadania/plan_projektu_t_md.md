## 9. Frontend Architecture & UI Foundation

Fundament aplikacji w przeglądarce oraz struktura interfejsu.

* aplikacja jako SPA (Single Page Application)
* podział na moduły: editor, sidebar, search, settings
* edytor jako główny komponent (wysoka responsywność)
* routing lokalny (bez przeładowań strony)
* minimalizacja opóźnień renderowania
* centralny stan aplikacji (np. store / state manager)

---

## 10. Data Layer & Local Persistence

Warstwa odpowiedzialna za przechowywanie danych lokalnie.

* lokalna baza danych w przeglądarce (np. IndexedDB)
* model danych: notes, tags, folders
* zapis zmian w trybie „auto-save”
* wersjonowanie notatek (history tracking opcjonalnie)
* mechanizm cache dla szybkiego dostępu
* obsługa działania offline jako domyślny tryb

---

## 11. Search & Indexing System

System wyszukiwania działający lokalnie.

* indeksowanie treści notatek po zapisie
* wyszukiwanie pełnotekstowe (full-text search)
* aktualizacja indeksu w tle
* szybkie filtrowanie wyników (bez zapytań do serwera)
* opcjonalne filtrowanie po tagach i folderach

---

## 12. Sync Architecture (Cloud Layer)

Warstwa synchronizacji danych między urządzeniami.

* synchronizacja oparta o konto użytkownika
* mechanizm merge zmian (rozwiązywanie konfliktów)
* wersjonowanie danych na serwerze
* kolejka zmian offline → online
* synchronizacja w tle bez blokowania UI
* fallback: lokalna kopia zawsze priorytetowa

---

## 13. Authentication & User Management

System kont użytkowników.

* logowanie (OAuth lub email/password)
* sesje użytkownika (token-based auth)
* separacja danych per użytkownik
* podstawowe zarządzanie kontem
* możliwość pracy bez konta (tryb lokalny)

---

## 14. API Layer (Backend Contract)

Definicja komunikacji frontend ↔ backend.

* REST lub GraphQL API
* operacje CRUD dla notatek
* endpointy dla sync
* endpointy dla auth
* obsługa batch updates (dla synchronizacji)
* minimalizacja liczby requestów

---

## 15. Performance & Optimization Strategy

Strategia utrzymania wysokiej wydajności.

* lazy loading komponentów
* virtualizacja list notatek
* debounce dla wyszukiwania
* minimalizacja rerenderów edytora
* lokalne przetwarzanie danych zamiast requestów
* prefetching danych aktywnych notatek

---

## 16. Security Model

Model bezpieczeństwa danych (szczególnie pod przyszłe E2E).

* separacja danych użytkowników
* szyfrowanie danych w tranzycie (HTTPS)
* przygotowanie pod E2E encryption
* brak logowania treści po stronie serwera (docelowo)
* lokalna kontrola nad danymi użytkownika

---

## 17. Deployment & Distribution Model

Sposób dostarczania aplikacji użytkownikowi.

* web app hostowana w chmurze
* CI/CD dla automatycznych wdrożeń
* statyczny frontend + backend API
* możliwość opakowania jako desktop app (Electron / Tauri)
* wersjonowanie release’ów

---

## 18. Observability & Maintenance

Monitorowanie działania systemu.

* logi błędów frontend + backend
* tracking wydajności (czas odpowiedzi, render)
* monitoring sync failures
* analiza użycia funkcji (bez treści notatek)
* system alertów dla backendu

---