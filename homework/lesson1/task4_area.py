# 4. Kalkulator pola powierzchni:
# Utwórz plik task4_area.py .
# Program powinien poprosić o długość i szerokość prostokąta.
# Oblicz i wyświetl jego pole powierzchni.
# Nie zapomnij o int() lub float() .

width = input("Podaj szerokość: ")
lenght = input("Podaj długość: ")

width = int(width)
lenght = int(lenght)

area = width * lenght

print("Pole powierzchni to:", area)