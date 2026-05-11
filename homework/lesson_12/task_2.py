# 2. ✏ Zadanie 2 – Walidator wieku
# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
# właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
# wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
# zmieniać wartości.


class Uzytkownik:
    def __init__(self, wiek):
        self._wiek = wiek

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, value):
        if 0 <= value <= 120:
            self._wiek = value
        else:
            print("Błąd wieku")


class Uzytkownik:
    def __init__(self, wiek):
        self._wiek = wiek

    @property
    def wiek(self):
        return self._wiek
    
    @wiek.setter
    def wiek(self, age):
        if age > 0 and age < 120:
            self._wiek = age
        else:
            print("Wiek nie jest w zakresie 0 : 120")
    

user = Uzytkownik(20)
user.wiek = 89
print(user.wiek)