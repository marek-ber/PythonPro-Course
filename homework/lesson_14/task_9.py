# Zadanie 9 - Funkcja do wyszukiwania produktów
# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
# produktów w tej kategorii.

def znajdz_produkty_w_kategorii(nazwa_kategorii):
    import sqlite3

    connection = sqlite3.connect('sklep.db')
    cursor = connection.cursor()

    cursor.execute("""
        SELECT nazwa_produktu, cena
        FROM Produkty AS p
        JOIN Kategorie AS k
            ON k.id_kategorii = p.id_kategorii
        WHERE LOWER(k.nazwa_kategorii) = LOWER(?)
        """, (nazwa_kategorii,))


    result = cursor.fetchall()

    

    connection.commit()
    connection.close()

    return result

# print(znajdz_produkty_w_kategorii("Elektronika"))

category = input("Podaj kategorie (Elektronika, Książki, Dom i ogród): ")

products = znajdz_produkty_w_kategorii(category)

if products:
    for index, (name, number) in enumerate(products, start=1):
        print(f"{index}. {name} - {number}")
else:
    print("Nie ma takiej kategorii.")