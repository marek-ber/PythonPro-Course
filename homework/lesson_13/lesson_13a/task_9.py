# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
# do tabeli przypisania, łącząc go z jednym z audytoriów.

import sqlite3

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


przypisania = [
    (1, 2),
    (2, 1),
    (2, 3),
    (3, 1),
    (4, 1)
]

cursor.executemany("""
                INSERT INTO przypisania (id_studenta, id_audytorium)
                VALUES (?, ?)
                """, przypisania)




connection.commit()
connection.close()
