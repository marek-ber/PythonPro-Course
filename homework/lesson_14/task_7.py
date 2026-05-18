# Zadanie 7 – Zamówienia Anny Nowak
# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
# imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
# Zamowienia, Zamowienia_Produkty i Produkty.

import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

order = """
        SELECT nazwa_produktu FROM Produkty AS p
        JOIN Zamowienia_Produkty AS zp
         ON p.id_produktu = zp.id_produktu
        JOIN Zamowienia AS z
         ON z.id_zamowienia = zp.id_zamowienia
        JOIN Klienci AS k
         ON k.id_klienta = z.id_klienta 
         WHERE imie = 'Anna Nowak'
        """

cursor.execute(order)

result = cursor.fetchall()

for index, (nazwa, ) in enumerate(result, start=1):
    print(f"{index}. {nazwa}")

connection.commit()
connection.close()