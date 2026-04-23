# 2. Sortowanie słownika: Masz słownik oceny = {"Jan": 4, "Anna": 5, "Piotr": 3,
# "Kasia": 4} . Użyj funkcji sorted() i funkcji lambda, aby posortować elementy
# słownika (klucz, wartość) według ocen (od najwyższej do najniższej).

grades = {"Jan": 4, "Anna": 5, "Piotr": 3, "Kasia": 4}

from_top = sorted(grades.items(), key=lambda grades: grades[1], reverse=True)

print(grades)
print(from_top)

