# 8. 🧠 Zadanie 8 – Hierarchia instrumentów muzycznych
# Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po
# Strunowy) i Trabka (dziedziczy po Dety). Klasa Instrument powinna mieć metodę graj(),
# która zwraca ogólny komunikat. Każda kolejna klasa w hierarchii powinna nadpisywać tę
# metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą
# super().graj().
# Instrument.graj() -> "Wydaje dźwięk."
# Strunowy.graj() -> "Wydaje dźwięk. [Szarpnięcie struny]"
# Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]" (challenge)


class Instrument:
    def graj(self):
        return "Wydaje dźwięk "

class Strunowy(Instrument):
    def graj(self):
        return super().graj() + "[Szarpnięcie struny] "
    
class Dety(Instrument):
    def graj(self):
        return super().graj() + "[Dmuchnięcie powietrza] "
    
class Gitara(Strunowy):
    def graj(self):
        return super().graj() + "[Akord G-dur]"

class Trabka(Dety):
    def graj(self):
        return super().graj() + "[Wysoki ton]"
    
gitara = Gitara()
trabka = Trabka()

print(gitara.graj())
print(trabka.graj())



    