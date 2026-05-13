# Zadanie 1 – Stwórz tabelę książek
# Napisz skrypt, który połączy się z bazą biblioteka.db 
# i stworzy w niej tabelę ksiazki. Tabela
# powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)

# Zadanie 2 – Dodaj książki
# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
# Użyj metody executemany do dodania wszystkich książek za jednym razem

### TASK 1

import sqlite3

connection = sqlite3.connect('biblioteka.db')
cursor = connection.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS ksiazki    
                (id INTEGER PRIMARY KEY, tytul TEXT NOT NULL,
                autor TEXT NOT NULL, rok_wydania INTEGER)
                """)

### TASK 2

my_books = [
    ("Władca Pierścieni", "Tolkien", 1960),
    ("Wiedźmin", "Sapkowski", 1980),
    ("Czarnoksiężnik", "LeGuin", 1970)
]

cursor.executemany("""
                INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)
                """, my_books)

## TASK 3


cursor.execute("""
                SELECT * FROM ksiazki;
                """)

print(cursor.fetchall())

## TASK 4

# Zadanie 4 – Wyszukaj książki autora
# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
# napisane przez Twojego ulubionego autora.
# 5. ✏ Zadanie 5 – Zaktualizuj rok wydania
# Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
# inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
# powiodła.

cursor.execute("""
                SELECT * FROM ksiazki WHERE autor = "Sapkowski"                
                """)

print(cursor.fetchall())

## TASK 5

cursor.execute("""
                UPDATE ksiazki SET rok_wydania = ? WHERE id = ?;          
                """, (1950, 1))

cursor.execute("""
                SELECT * FROM ksiazki WHERE id = 1;
                """)

print(cursor.fetchall())

connection.commit()
connection.close()