# 3. Konwersja na wielkie litery: Użyj funkcji map() , aby przekształcić listę imion imiona =
# ["anna", "piotr", "kasia"] w listę imion pisanych wielką literą.

names = ["anna", "piotr", "kasia"]

big_names = list(map(lambda w: w.capitalize(), names))

very_big = list(map(lambda w: w.upper(), names))

print(names)

print(big_names)

print(very_big)
