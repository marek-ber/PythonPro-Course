# Zadanie 10 – Funkcja wyszukująca z JOIN
# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
# studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
# wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.Tip
# Aby rozwiązać to zadanie, będziesz potrzebować klauzuli JOIN w zapytaniu SELECT.
# Pozwala ona łączyć wiersze z dwóch lub więcej tabel na podstawie powiązanych
# kolumn.
# Przykład: SELECT t1.kolumna, t2.kolumna FROM tabela1 AS t1 JOIN tabela2 AS t2
# ON t1.id = t2.id_z_tabeli1


def znajdz_sale_studenta(nazwisko):

    import sqlite3

    connection = sqlite3.connect('uczelnia.db')
    cursor = connection.cursor()


    cursor.execute("""
                    SELECT a.nazwa_budynku, a.numer_sali
                    FROM przypisania p
                    JOIN audytoria a ON p.id_audytorium = a.id_audytorium
                    JOIN studenci s ON p.id_studenta = s.id_studenta
                    WHERE s.nazwisko = "Berny"
                    """)

    result = cursor.fetchall()
    print(result)

    connection.commit()
    connection.close()

znajdz_sale_studenta("Berny")