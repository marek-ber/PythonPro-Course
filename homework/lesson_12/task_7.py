# 7. 🧠 Zadanie 7 – Alternatywny konstruktor dla Daty
# Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o
# nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i
# tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int.


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def ze_stringa(cls, input: str):
        splitted_input = input.split(sep="-")
        return cls(int(splitted_input[0]), int(splitted_input[1]), int(splitted_input[2]))

example = Data.ze_stringa("12-10-1990")
print(example.year)