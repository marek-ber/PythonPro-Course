# Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
# najmniej 4 studentów i 3 audytoria.

import sqlite3

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()

studenci = [
    ("Marek", "Berny"),
    ("Jan", "Kowalski"),
    ("Adam", "Nowak"),
    ("Piotr", "Kamiński")
]

cursor.executemany("""
                INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)
                """, studenci)

audytoria = [
    ("Budynek A", 11),
    ("Budynek B", 23),
    ("Budynek C", 5)
]

cursor.executemany("""
                INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?,?)
                """, audytoria)

connection.commit()
connection.close()