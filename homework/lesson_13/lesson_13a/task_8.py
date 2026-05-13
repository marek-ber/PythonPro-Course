# Zadanie 8 – Połącz tabele (Relacja)
# To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do
# audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej
# samej bazie uczelnia.db. Tabela powinna mieć strukturę:
# id_przypisania (INTEGER, klucz główny)
# id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w
# tabeli studenci .
# id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli
# audytoria .

import sqlite3

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS przypisania
               (id_przypisania INTEGER PRIMARY KEY,
               id_studenta INTEGER REFERENCES studenci(id_studenta),
               id_audytorium INTEGER REFERENCES audytoria(id_audytorium)
               )
               """)



connection.commit()
connection.close()