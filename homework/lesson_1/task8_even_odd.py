# 8. Sprawdzanie parzystości:
# Utwórz plik task8_even_odd.py .
# Poproś o liczbę całkowitą i sprawdź, czy jest parzysta.
# Wskazówka: operator % 2 

num = int(input("Podaj liczbę całkowitą: "))

if num % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")