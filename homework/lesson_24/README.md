# Lekcja 24 - Uwierzytelnianie i Autoryzacja Użytkowników w Django

Projekt zawiera komplet zadań z lekcji 24.

## Uruchomienie

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Plik .env

Utwórz samodzielnie plik `.env` w głównym katalogu projektu:

```env
DB_NAME=django4
DB_USER=postgres
DB_PASSWORD=twoje_haslo
DB_HOST=localhost
DB_PORT=5432
```

## Najważniejsze adresy

- `/register/` - rejestracja
- `/login/` - logowanie
- `/logout/` - wylogowanie
- `/profile/` - profil użytkownika, wymaga logowania
- `/password-change/` - zmiana hasła
- `/staff/users/` - lista użytkowników, tylko dla staff
- `/next-info/` - opis mechanizmu next
