# 9. 🧠 Zadanie 9 – Klasa KontoBankowe z property i wyjątkami
# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
# ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.

from dataclasses import dataclass

class BrakSrodkowError(Exception):
    pass


@dataclass

class KontoBankowe:
    _saldo: float

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota nie może być ujemna")
        else:
            self._saldo += kwota
        
    def wyplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota do wypłaty nie może być ujemna.")
        
        if kwota > self._saldo:
            raise BrakSrodkowError("Brak środków na koncie.")
        else:
            self._saldo -= kwota



konto = KontoBankowe(5000)

konto.wplac(2000)
print(konto.saldo)

konto.wplac(-1000)
print(konto.saldo)

konto.wyplac(-1000)
print(konto.saldo)

konto.wyplac(1000)
print(konto.saldo)

konto.wyplac(8000)
print(konto.saldo)
