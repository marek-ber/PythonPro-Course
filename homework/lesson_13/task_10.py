# Zadanie 10 – Funkcja wyszukująca z JOIN
# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
# studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
# wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.Tip
# Aby rozwiązać to zadanie, będziesz potrzebować klauzuli JOIN w zapytaniu SELECT.
# Pozwala ona łączyć wiersze z dwóch lub więcej tabel na podstawie powiązanych
# kolumn.
# Przykład: SELECT t1.kolumna, t2.kolumna FROM tabela1 AS t1 JOIN tabela2 AS t2
# ON t1.id = t2.id_z_tabeli1

def znajdz_sale_studenta(nazwisko):

    import sqlite3

    connection = sqlite3.connect('uczelnia.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    query = "SELECT "



    connection.commit()
    connection.close()



import sqlite3
from turtle import st

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute("""
               CREATE TABLE IF NOT EXISTS studenci (
                   id_studenta INTEGER PRIMARY KEY,
                   imie TEXT,
                   nazwisko TEXT
               )
               
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS audytoria (
                   id_audytorium INTEGER PRIMARY KEY,
                   nazwa_budynku TEXT,
                   numer_sali INTEGER
               )
               """)

students = [
    ('Paweł', 'Wyżykowski'),
    ('Jan', "Kowalski"),
    ('Janusz', 'Nowak'),
    ('Czesław', 'Michniewicz')
]


# cursor.executemany("""
#                    INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)
#                    """, students)


auditories = [
    ('Budynek Główny', 1),
    ('Kotłownia', 11),
    ('Wydział Fizyki', 22)
]

# cursor.executemany("""
#                    INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)
#                    """, auditories)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS studenci_audytoria (
                   id_przypisania INTEGER PRIMARY KEY,
                   student_id INTEGER REFERENCES studenci(id_studenta),
                   id_audytorim INTEGER REFERENCES audytoria(id_audytorium)
                   )
               """)

students_auditories = [
    (1, 2),
    (2, 1),
    (2, 3),
    (3, 1),
    (3, 1)
]

# SELECT *
# FROM studenci_audytoria as sa
# JOIN audytoria as a ON sa.id_audytorim = a.id_audytorium
# JOIN studenci as s ON s.id_studenta = sa.student_id
# WHERE s.nazwisko = 'Wyżykowski'
cursor.execute("""
               SELECT audytoria.nazwa_budynku, audytoria.numer_sali
FROM studenci_audytoria 
JOIN audytoria ON studenci_audytoria.id_audytorim = audytoria.id_audytorium
JOIN studenci ON studenci.id_studenta = studenci_audytoria.student_id
WHERE studenci.nazwisko = 'Wyżykowski'
               """, 
               students_auditories)

result = cursor.fetchall()
print(result)
connection.commit()
connection.close()