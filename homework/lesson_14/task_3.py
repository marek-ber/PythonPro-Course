# Zadanie 3 – Suma wartości
# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
# SUM() oraz klauzuli WHERE z JOIN.

import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

cursor.execute("""
               SELECT SUM(cena) FROM Produkty AS p
               JOIN Kategorie AS k
                ON k.id_kategorii = p.id_kategorii
               WHERE k.nazwa_kategorii = 'Elektronika'
                """)

result = cursor.fetchone()
print(result[0])

connection.commit()
connection.close()