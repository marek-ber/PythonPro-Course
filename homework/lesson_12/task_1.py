# 1. ✏ Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
# reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je.


from dataclasses import dataclass



@dataclass
class Film:
    tytul: str
    rezyser: str # (string)
    rok_produkcji: int

syfy = Film("Terminator", "Cameron", "1984")

komedia = Film ("Chłopaki nie płaczą", "Lubaszenko", 1997 )

print(syfy)

print(komedia)