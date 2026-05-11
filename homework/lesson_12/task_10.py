# 10. 🧠 Zadanie 10 – Metaklasa walidująca
# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
# wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
# docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
# informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
# niepoprawnie udokumentowanymi metodami.


class MetaWalidujMetody(type):
    def __new__(cls, name, bases, dct):

        for nazwa, wartosc in dct.items():

            if nazwa.startswith("__"):
                continue

            if callable(wartosc):
                if wartosc.__doc__ is None:
                    raise TypeError(f"Metoda {nazwa} w klasie {name}")
                
        return super().__new__(cls, name, bases, dct)
    

class DobraKlasa(metaclass=MetaWalidujMetody):

    def metoda1(self):
        print("Metoda 1")

    def metoda2(self):
        print("Metoda 2")

class ZlaKlasa(metaclass=MetaWalidujMetody):

    def metoda1(self):
        print("OK")

    def metoda2(self):
        print("Brak opisu")

