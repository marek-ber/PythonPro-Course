# Tematy prac dyplomowych: Python Web Development

> [!summary] Spis treści
> 
> 1. Sklep internetowy
>     
> 2. Agregator newsów
>     
> 3. Bot na Telegramie (pizzeria)
>     
> 4. Bot na Telegramie (architektura funeralna)
>     
> 5. Serwis do wymiany plików

### 1. Sklep internetowy

> [!abstract] Opis
> 
> Należy napisać aplikację internetową, w której można przeglądać listę produktów z podstawowymi informacjami, a także szczegółowe informacje o każdym z nich, dodawać produkty do koszyka i dokonywać zakupu (bez podłączania systemu płatności). Dodawać i kupować produkty mogą tylko zalogowani użytkownicy. Dodawanie / usuwanie produktów w systemie jest realizowane wyłącznie przez administratora.

**Wymagania:**

1. Użyć dowolnego frameworka z listy: Django, Flask, FastAPI, Aiohttp.
    
2. Użyć dowolnego systemu DBMS z listy: MySQL, PostgreSQL, MongoDB.
    
3. Zaimplementować rejestrację i logowanie jednym z następujących sposobów: Session, Access Token, JWT.
    
4. Każdy przypadek wyjątkowy musi zwracać odpowiedź z odpowiednim statusem.
    
5. Przed zapisaniem lub aktualizacją dane od użytkownika muszą być walidowane, a w przypadku błędów należy zwrócić użytkownikowi odpowiedź z odpowiednimi komunikatami dla każdego z nieprawidłowych pól.
    
6. Dodać testy (wystarczą testy jednostkowe i integracyjne).
    

### 2. Agregator newsów

> [!abstract] Opis
> 
> Należy napisać aplikację internetową, która będzie parsować i wyświetlać listę artykułów z istniejących serwisów informacyjnych (minimum 2). Każdy news powinien mieć plakat, tytuł i krótki opis, a na stronie konkretnego newsa będzie można uzyskać wszystkie niezbędne informacje (treść tekstową, obrazki, linki do źródła itp.). Aby publikować własne artykuły, użytkownik musi się zarejestrować i, po stworzeniu artykułu, wysłać go do publikacji. Administrator będzie przeglądał prośby o publikację i podejmował decyzję. W przypadku odrzucenia, administrator musi podać przyczynę.

**Wymagania:**

1. Użyć dowolnego frameworka z listy: Django, Flask, FastAPI, Aiohttp.
    
2. Do parsowania użyć: selenium, scrapy, beautiful-soup.
    
3. Do zadań w tle użyć: celery, cron, threading, BackgroundTasks.
    
4. Użyć dowolnego systemu DBMS z listy: MySQL, PostgreSQL, MongoDB.
    
5. Zaimplementować rejestrację i logowanie jednym z następujących sposobów: Session, Access Token, JWT.
    
6. Każdy przypadek wyjątkowy musi zwracać odpowiedź z odpowiednim statusem.
    
7. Przed zapisaniem lub aktualizacją dane od użytkownika muszą być walidowane, a w przypadku błędów należy zwrócić użytkownikowi odpowiedź z odpowiednimi komunikatami dla każdego z nieprawidłowych pól.
    
8. Dodać testy (wystarczą testy jednostkowe i integracyjne).
    

### 3. Bot na Telegramie (pizzeria)

> [!abstract] Opis
> 
> Należy napisać bota na Telegramie, który pozwala przeglądać katalog pizz, dodawać je do koszyka, wskazując odpowiednie rozmiary i rodzaj, oraz składać zamówienie. Dodawanie i edycja dostępnych opcji, cen itp. musi odbywać się w panelu administracyjnym aplikacji internetowej, do którego klienci nie mają dostępu.

**Wymagania:**

1. Użyć dowolnego frameworka z listy: Django, Flask, FastAPI, Aiohttp.
    
2. Użyć Telegram API: telebot, aiogram.
    
3. Użyć dowolnego systemu DBMS z listy: MySQL, PostgreSQL, MongoDB.
    
4. Zaimplementować rejestrację i logowanie jednym z następujących sposobów: Session, Access Token, JWT.
    
5. Każdy przypadek wyjątkowy musi zwracać odpowiedź z odpowiednim statusem.
    
6. Przed zapisaniem lub aktualizacją dane od użytkownika muszą być walidowane, a w przypadku błędów należy zwrócić użytkownikowi odpowiedź z odpowiednimi komunikatami dla każdego z nieprawidłowych pól.
    
7. Dodać testy (wystarczą testy jednostkowe i integracyjne).
    

### 4. Bot na Telegramie (architektura funeralna)

> [!abstract] Opis
> 
> Należy napisać bota na Telegramie, który pozwala przeglądać katalog produktów, dodawać je do koszyka i składać zamówienie, po czym administrator powinien otrzymać powiadomienie oraz dane kontaktowe do связи z kupującym. Dodawanie i edycja dostępnych opcji, cen itp. musi odbywać się w panelu administracyjnym aplikacji internetowej, do którego klienci nie mają dostępu.

**Wymagania:**

1. Użyć dowolnego frameworka z listy: Django, Flask, FastAPI, Aiohttp.
    
2. Użyć Telegram API: telebot, aiogram.
    
3. Użyć dowolnego systemu DBMS z listy: MySQL, PostgreSQL, MongoDB.
    
4. Zaimplementować rejestrację i logowanie jednym z następujących sposobów: Session, Access Token, JWT.
    
5. Każdy przypadek wyjątkowy musi zwracać odpowiedź z odpowiednim statusem.
    
6. Przed zapisaniem lub aktualizacją dane od użytkownika muszą być walidowane, a w przypadku błędów należy zwrócić użytkownikowi odpowiedź z odpowiednimi komunikatami dla każdego z nieprawidłowych pól.
    
7. Dodać testy (wystarczą testy jednostkowe i integracyjne).
    

### 5. Serwis do wymiany plików

> [!abstract] Opis
> 
> Należy napisać aplikację internetową, która pozwala przesyłać pliki dowolnych formatów, generować tymczasowy link do pliku, za pomocą którego użytkownicy posiadający ten link mogą go pobrać. Należy również dodać funkcjonalność, która pozwoli na zezwolenie na pobieranie pliku określonej liście użytkowników, a wszystkim pozostałym zabronić.

**Wymagania:**

1. Użyć dowolnego frameworka z listy: Django, Flask, FastAPI, Aiohttp.
    
2. Użyć dowolnego systemu DBMS z listy: MySQL, PostgreSQL, MongoDB.
    
3. Zaimplementować rejestrację i logowanie jednym z następujących sposobów: Session, Access Token, JWT.
    
4. Każdy przypadek wyjątkowy musi zwracać odpowiedź z odpowiednim statusem.
    
5. Przed zapisaniem lub aktualizacją dane od użytkownika muszą być walidowane, a w przypadku błędów należy zwrócić użytkownikowi odpowiedź z odpowiednimi komunikatami dla każdego z nieprawidłowych pól.
    
6. Dodać testy (wystarczą testy jednostkowe i integracyjne).