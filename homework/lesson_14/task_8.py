# Zadanie 8 – Kategorie z liczbą produktów
# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
# do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.

import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

query = """
        SELECT k.nazwa_kategorii, COUNT(p.id_produktu)
        FROM Kategorie AS k
        JOIN Produkty AS p
            ON k.id_kategorii = p.id_kategorii
        GROUP BY k.id_kategorii
        """

cursor.execute(query)

result = cursor.fetchall()

for nazwa, liczba in result:
    print(f"{nazwa} - {liczba} produkty")


connection.commit()
connection.close()