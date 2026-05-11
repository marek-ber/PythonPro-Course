# 5. ✏ Zadanie 5 – Polimorficzna Figura
# Stwórz klasę bazową Figura z metodą oblicz_pole(), która pass (nic nie robi). Następnie
# stwórz dwie klasy potomne: Kwadrat (z atrybutem bok) i Kolo (z atrybutem promien). W obu
# klasach nadpisz metodę oblicz_pole() odpowiednimi wzorami matematycznymi (dla koła
# przyjmij PI=3.14159). Stwórz listę zawierającą jeden kwadrat i jedno koło, a następnie w
# pętli wydrukuj pole każdej figury.
# (proste)

PI = 3.14159

class Figura:
    def __init__(self):
        pass
    def oblicz_pole(self):
        print("Ta figura nie ma pola")
        pass

class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok
    def oblicz_pole(self):
        return self.bok * self.bok

class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien
    def oblicz_pole(self):
        return self.promien ** 2 * PI
    

moj_kwadrat = Kwadrat(10)
moje_kolo = Kolo(10)

moje_figury = [moj_kwadrat, moje_kolo]

for i in moje_figury:
    print(i.oblicz_pole())