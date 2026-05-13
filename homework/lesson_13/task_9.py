# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
# do tabeli przypisania, łącząc go z jednym z audytoriów.

import sqlite3
connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
                INSERT INTO przypisania (id_studenta, id_audytorium)
                SELECT s.id_studenta, a.id_audytorium
                FROM studenci s
                JOIN audytoria a
                ON a.id_audytorium = (
                    SELECT id_audytorium FROM audytoria ORDER BY RANDOM() LIMIT 1
                )
                """)

cursor.execute("""
                SELECT id_studenta, id_audytorium FROM przypisania
                """)

result = cursor.fetchall()

for index, (s, a) in enumerate(result, start=1):
    print(f"{index}. {s} - {a}")


connection.commit()
connection.close()