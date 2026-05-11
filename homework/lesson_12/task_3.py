# 3. ✏ Zadanie 3 – Konwerter Walut
# Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie
# usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij
# stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.
# Zadania-wyzwania (challenge)

class KalkulatorWalut:

    @staticmethod
    def usd_na_pln(usd):
        return usd / 4.0
    
print(KalkulatorWalut.usd_na_pln(20))