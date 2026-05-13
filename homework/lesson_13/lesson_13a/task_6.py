# Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).

import sqlite3

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()

query1 = """
        CREATE TABLE IF NOT EXISTS studenci (id_studenta INTEGER PRIMARY KEY, imie TEXT NOT NULL, nazwisko TEXT NOT NULL)
        """
cursor.execute(query1)

query2 = """
        CREATE TABLE IF NOT EXISTS audytoria (id_audytorium INTEGER PRIMARY KEY, nazwa_budynku TEXT NOT NULL, numer_sali INTEGER)
        """

cursor.execute(query2)

connection.commit()
connection.close()