# zad 2
# Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii.

class Produkt:
    def __init__(self, nazwa, cena, kategoria ):
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria



p = Produkt("Chleb", 3.5, "Pieczywo")

print(p.cena)
print(p.kategoria)
print(p.nazwa)