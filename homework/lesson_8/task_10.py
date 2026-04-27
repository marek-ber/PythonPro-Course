# 10. Mini-projekt: Sumator liczb z pliku: Napisz program, który:
# a. Pyta użytkownika o nazwę pliku.
# b. Otwiera plik i czyta go linia po linii.
# c. Każdą linię próbuje przekonwertować na liczbę i dodać do sumy.
# d. Ignoruje linie, których nie da się przekonwertować na liczbę (obsługa ValueError).
# e. Obsługuje FileNotFoundError, jeśli plik nie istnieje.
# f. Na końcu, w bloku finally, wyświetla obliczoną sumę (nawet jeśli wystąpiły błędy po
# drodze).


suma = 0
nazwa = input("Podaj nazwę pliku: ")

try:
    with open(nazwa, "r") as f:
        for linia in f:
            try:
                liczba = float(linia.strip())
                suma += liczba
            except ValueError:
                
                continue

except FileNotFoundError:
    print("Plik nie istnieje.")

finally:
    print("Suma wynosi:", suma)