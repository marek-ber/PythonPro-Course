# 6. Konwerter systemów liczbowych:
# Utwórz plik task6_converter.py .
# Poproś użytkownika o liczbę całkowitą i wyświetl ją w formacie dwójkowym i
# szesnastkowym.

integer = input("Podaj liczbę cakowitą: ")
integer = int(integer)
print(bin(integer))
print(hex(integer))