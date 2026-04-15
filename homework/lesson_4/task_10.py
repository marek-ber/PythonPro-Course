# 10. Komentowanie kodu: Poniżej znajduje się fragment kodu. Dodaj do niego komentarze
# jednoliniowe oraz docstring dla funkcji, wyjaśniając, co robi każda część.
# def oblicz_pole_prostokata(a, b):
#  # Tutaj dodaj docstring
#  # Tutaj dodaj komentarz
#  pole = a * b
#  # Tutaj dodaj komentarz
#  return pole
# bok_a = 10
# bok_b = 20
# wynik = oblicz_pole_prostokata(bok_a, bok_b)
# print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")

def oblicz_pole_prostokata(a, b):
    """
    Funkcja oblicza pole prostokąta na podstawie długości jego boków.
    
    Parametry:
    a (int/float): długość pierwszego boku
    b (int/float): długość drugiego boku
    
    Zwraca:
    int/float: pole prostokąta
    """
    # Obliczamy pole prostokąta jako iloczyn długości boków
    pole = a * b
    # Zwracamy obliczone pole
    return pole

# Przypisanie wartości do zmiennych reprezentujących boki prostokąta
bok_a = 10
bok_b = 20

# Wywołanie funkcji i zapisanie wyniku
wynik = oblicz_pole_prostokata(bok_a, bok_b)

# Wyświetlenie wyniku w czytelnej formie
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")