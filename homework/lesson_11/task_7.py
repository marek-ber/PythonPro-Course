# 7. 🧠 Zadanie 7 – Enkapsulacja w Telewizorze
# Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal
# (domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False). Stwórz publiczne
# metody do zarządzania telewizorem:
# wlacz() i wylacz()
# zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
# glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV
# jest włączony.
# info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). Przetestuj, czy
# nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej
# 100. (challenge)



class Telewizor:
    def __init__(self):
        self.kanal = 1
        self.glosnosc = 10
        self.__wlaczony = False

    def wlacz(self):
        self.__wlaczony = True

    def wylacz(self):
        self.__wlaczony = False
    
    def zmien_kanal(self, numer):
        if self.__wlaczony:
            self.kanal = numer
        else:
            print("Telewizor jest wylączony!")
    
    def glosniej(self):
        if self.__wlaczony:
            if self.glosnosc + 10 <= 100:
                self.glosnosc += 10
        else:
            print("Telewizor jest wylączony!")

    def ciszej(self):
        if self.__wlaczony:
            if self.glosnosc - 10 >= 0:
                self.glosnosc -=10
        else:
            print("Telewizor jest wylączony!")


    def info(self):
        print(f"Status {self.__wlaczony}, kanał: {self.kanal}, poziom głośności: {self.glosnosc} ")

tv = Telewizor()

tv.wlacz()
tv.info()
tv.ciszej()
tv.info()
tv.ciszej()
tv.info()
tv.glosniej()
tv.info()
tv.zmien_kanal(3)
tv.info()
tv.wylacz()
tv.info()
tv.glosniej()
tv.info()
tv.zmien_kanal(5)