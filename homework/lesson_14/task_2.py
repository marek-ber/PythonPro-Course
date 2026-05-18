# Zadanie 2 – Najdroższy produkt
# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
# MAX().

import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

cursor.execute("""
                SELECT MAX(cena), nazwa_produktu FROM Produkty
                """)

result = cursor.fetchone()
print(result)

connection.commit()
connection.close()