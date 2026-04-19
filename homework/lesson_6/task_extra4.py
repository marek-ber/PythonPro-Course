# Ćwiczenie S4: Statystyki listy
# Napisz funkcję statystyki(*args) zwracającą krotkę: (ilość, suma, średnia). Obsłuż przypadek
# pustych argumentów (zwróć 0, 0, 0).
# Wskazówka: len(args), sum(args), sum/len. Rozpakuj wynik: ilosc, suma, sr = statystyki(1, 2, 3).

def statistic(*numbers: int) -> tuple:
    if len(numbers) == 0:
        return (0, 0, 0)
    
    quantity = len(numbers)
    suma = sum(numbers)
    average = suma / quantity
    return quantity, suma, average

quantity, suma, average = statistic(5, 6, 7)

print(f"Ilość: {quantity}")
print(f"Suma: {suma}")
print(f"Średnia: {average}")