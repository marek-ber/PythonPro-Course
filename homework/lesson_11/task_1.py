# Zadanie 1 – Klasa Film
# Zadania z gwiazdką (challenge)
# Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i
# rok_produkcji. Dodaj metodę informacje(), która będzie zwracać string z pełnymi
# informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. Stwórz dwa
# obiekty tej klasy i wydrukuj informacje o nich

class Film():
    def __init__(self, tytul, rezyser, rok_produkcji):
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok_produkcji = rok_produkcji

    def informacje(self):
        return f"Tytuł: {self.tytul} ({self.rok_produkcji}), reżyseria: {self.rezyser}"
    
film_1 = Film("Tytul_1", "Rez_1", "Rok_1")
film_2 = Film("Tytul_2", "Rez_2", "Rok_2")

print(film_1.informacje())
print(film_2.informacje())