# 2. Licznik słów: Stwórz program, który pyta o nazwę pliku, odczytuje go, a następnie zlicza i
# wyświetla całkowitą liczbę słów w tym pliku. Obsłuż błąd FileNotFoundError , jeśli plik nie
# istnieje.

ask = input("Podaj nazwę pliku z rozszerzeniem: ")

try:
    with open(ask, encoding="UTF-8", mode="r") as file:

        counter = 0

        for i in file.readlines():
            counter += len(i.strip().split())

except FileNotFoundError:
    print("Nie znaleziono pliku")
else:
    print(f"Ilość słów w pliku: {counter}")
finally:
    print("Koniec programu")

