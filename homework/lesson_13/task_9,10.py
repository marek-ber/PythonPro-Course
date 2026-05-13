# 6. Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).

import sqlite3

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()

# cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS studenci (id_studenta INTEGER PRIMARY KEY, imie TEXT NOT NULL, nazwisko TEXT NOT NULL)
#                 """)

# cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS audytoria (id_audytorium INTEGER PRIMARY KEY, nazwa_budynku TEXT NOT NULL, numer_sali INTEGER)
#                 """)

###### TASK 7 ######
#Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
# najmniej 4 studentów i 3 audytoria.

students = [
    ("Marek", "Berny"),
    ("Jan", "Kowalski"),
    ("Adam", "Nowak"),
    ("Piotr", "Kamiński")
]

# cursor.executemany("""
#                     INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)
#                     """, students)

audytories = [
    ("Budynek A", 11),
    ("Budynek B", 23),
    ("Budynek C", 5)
]

# cursor.executemany("""
#                     INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)
#                     """, audytories)

# cursor.execute("""
#                 SELECT * FROM studenci
#                 """)

# print(cursor.fetchall())

# cursor.execute("""
#                 SELECT * FROM audytoria
#                 """)

# print(cursor.fetchall())

###### TASK 8 ######
#Zadanie 8 – Połącz tabele (Relacja)
# To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do
# audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej
# samej bazie uczelnia.db. Tabela powinna mieć strukturę:
# id_przypisania (INTEGER, klucz główny)
# id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w
# tabeli studenci .
# id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli
# audytoria .

# cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS przypisania (
#                id_przypisania INTEGER PRIMARY KEY, 
#                id_studenta INTEGER, id_audytorium INTEGER, 
#                FOREIGN KEY(id_studenta) REFERENCES studenci(id_studenta),
#                FOREIGN KEY(id_audytorium) REFERENCES audytoria(id_audytorium))
#                 """)

###### TASK 9 ######
# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
# do tabeli przypisania, łącząc go z jednym z audytoriów.

# cursor.execute("""
#                 INSERT INTO przypisania (id_studenta, id_audytorium)
#                 SELECT s.id_studenta, a.id_audytorium
#                 FROM studenci s
#                 JOIN audytoria a
#                 ON a.id_audytorium = (
#                     SELECT id_audytorium FROM audytoria ORDER BY RANDOM() LIMIT 1
#                 )
#                 """)

cursor.execute("""
                SELECT id_studenta, id_audytorium FROM przypisania
                """)

result = cursor.fetchall()

for index, (s, a) in enumerate(result, start=1):
    print(f"{index}. {s} - {a}")




###### TASK 10 ######
# Zadanie 10 – Funkcja wyszukująca z JOIN
# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
# studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
# wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.Tip
# Aby rozwiązać to zadanie, będziesz potrzebować klauzuli JOIN w zapytaniu SELECT.
# Pozwala ona łączyć wiersze z dwóch lub więcej tabel na podstawie powiązanych
# kolumn.
# Przykład: SELECT t1.kolumna, t2.kolumna FROM tabela1 AS t1 JOIN tabela2 AS t2
# ON t1.id = t2.id_z_tabeli1


connection.commit()
connection.close()