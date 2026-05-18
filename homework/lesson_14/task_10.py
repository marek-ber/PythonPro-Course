# Zadanie 10 – Prosta symulacja ORM
# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
# Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
# pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
# jak ORM automatyzuje mapowanie wierszy na obiekty.


class Produkt:
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena
        
    def __str__(self):
        return f"{self.id_produktu}. {self.nazwa_produktu} - {self.cena}"

def pobierz_wszystkie_produkty():  

    import sqlite3

    connection = sqlite3.connect('sklep.db')
    cursor = connection.cursor()

    cursor.execute("""
                    SELECT id_produktu, nazwa_produktu, cena FROM produkty
                    """)

    result = cursor.fetchall()

    produkty = []

    for index in result:
        item = Produkt(index[0], index[1], index[2])
        produkty.append(item)



    connection.commit()
    connection.close()
    return produkty

lista_produkty = pobierz_wszystkie_produkty()

for i in lista_produkty:
    print(i)