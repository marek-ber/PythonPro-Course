# Zadanie 5 – Lista klientów
# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.

import sqlite3
connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

users = "SELECT imie, email FROM Klienci"

cursor.execute(users)

result = cursor.fetchall()

for index, (imie, email) in enumerate(result, start=1):
    print(f"{index}. {imie} - {email}")

connection.commit()
connection.close()