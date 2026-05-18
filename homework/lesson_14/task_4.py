# Zadanie 4 – Średnia cena książki
# Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().

import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

cursor.execute("""
                SELECT AVG(cena) FROM Produkty AS p
               JOIN Kategorie AS k
                ON k.id_kategorii = p.id_kategorii
               WHERE k.nazwa_kategorii = 'Książki'
                """)

result = cursor.fetchone()

print(result[0])

connection.commit()
connection.close()