# 6. Import z CSV: Napisz program, który odczytuje plik produkty.csv i oblicza sumę cen
# wszystkich produktów. Użyj csv.DictReader , aby łatwiej odwoływać się do kolumn po
# nazwach.

import csv

suma = 0

with open("produkty.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    suma = sum(float(i["cena"]) for i in reader)
    
print(f"Suma cen: {suma} zł")
