# 6. 🧠 Zadanie 6 – Wektor 2D i przeciążanie operatorów
# Stwórz klasę Wektor2D z atrybutami x i y. Przeciąż następujące operatory:
# __add__(self, other) : do dodawania dwóch wektorów (dodajemy odpowiadające
# sobie współrzędne).
# __sub__(self, other) : do odejmowania wektorów.
# eq(self, other): do porównywania, czy dwa wektory są równe (mają te same x i y).
# Dodatkowo zaimplementuj str do ładnego wyświetlania. Przetestuj działanie, tworząc
# dwa wektory i wykonując na nich wszystkie zaimplementowane operacje. (challenge)


class Wektor2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Wektor2D(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Wektor2D(x, y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
punkt_1 = Wektor2D(5, 6)
punkt_2 = Wektor2D(4, 3)

print(f"Dodawanie: {punkt_1 + punkt_2}")
print(f"Odejmowanie: {punkt_1 - punkt_2}")
print(f"Porównanie: {punkt_1 == punkt_2}")


class Wektor2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

# przeciążanie operacji +
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return(x, y)

    # przeciążanie operacji -
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return (x, y)

    # przeciążanie operacji ==
    def __eq__(self, other):
        #return self.x == other.x and self.y == other.y
        if self.x == other.x and self.y == other.y:
            return True

        return False

wektor_1 = Wektor2d(3, 3)
wektor_2 = Wektor2d(2, 3)

print(f"Dodawanie {wektor_1 + wektor_2}")
print(f"Odejmowanie {wektor_1 - wektor_2}")
print(f"Porównanie {wektor_1 == wektor_2}")
print(wektor_1)
print(wektor_2)