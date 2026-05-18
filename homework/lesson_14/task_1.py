# Zadanie 1 – Liczba produktów
# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
# tabeli Produkty. Użyj funkcji COUNT().


import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

cursor.execute("""
                SELECT COUNT(id_produktu) FROM Produkty
                """)

result = cursor.fetchone()

print(result)

connection.commit()
connection.close()