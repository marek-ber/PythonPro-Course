# . ✏ Zadanie 1 – Stwórz tabelę książek
# Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela
# powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)


import sqlite3

connection = sqlite3.connect('biblioteka.db')
cursor = connection.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS
               ksiazki (id INTEGER PRIMARY KEY, tytul TEXT NOT NULL, autor TEXT NOT NULL, rok_wydania INTEGER)
               """)

###### TASK 2 ######
# 2. ✏ Zadanie 2 – Dodaj książki
# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
# Użyj metody executemany do dodania wszystkich książek za jednym razem.

my_books = [
    ("Władca Pierścieni", "J. R. R. Tolkien", 1950),
    ("Wiedźmin", "Andrzej Sapkowski", 1986),
    ("Ogniem i mieczem", "Henryk Sienkiewicz", 1884)
]

cursor.executemany("""
                    INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)""", my_books)

###### TASK 3 ######
# 3. ✏ Zadanie 3 –# Wyświetl całą bibliotekę
# Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
# tabeli ksiazki.

cursor.execute("""
                SELECT * FROM ksiazki;
               """)

print(cursor.fetchall())

###### TASK 4 ######
# 4. ✏ Zadanie 4 – Wyszukaj książki autora
# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
# napisane przez Twojego ulubionego autora.

cursor.execute("""
                SELECT * FROM ksiazki WHERE autor = "Andrzej Sapkowski"
                """)

print(cursor.fetchall())

###### TASK 5 ######
# 5. ✏ Zadanie 5 – Zaktualizuj rok wydania
# Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
# inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
# powiodła.

cursor.execute("""
                UPDATE ksiazki SET rok_wydania = ? WHERE id = ?;
               """, (1949, 1))

cursor.execute("""
                SELECT * FROM ksiazki WHERE id = 1;
                """)

connection.commit()
connection.close()

