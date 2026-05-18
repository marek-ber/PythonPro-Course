# Zadanie 6 – Produkty droższe od średniej
# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
# niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie.

import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

query = """
        SELECT nazwa_produktu, cena FROM Produkty
        WHERE cena > (SELECT AVG(cena) FROM Produkty)
        """

cursor.execute(query)

result = cursor.fetchall()

for index, (nazwa, cena) in enumerate(result, start=1):
    print(f"{index}. {nazwa} - {cena}")

connection.commit()
connection.close()