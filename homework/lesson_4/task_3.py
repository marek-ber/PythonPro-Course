# 3. Porównanie is vs == : Utwórz dwie różne listy lista1 = [1, 1] i lista2 = [1, 1] .
# Sprawdź wynik porównania lista1 is lista2 oraz lista1 == lista2 . Wyświetl wyniki
# i w komentarzu wyjaśnij, dlaczego są różne.

list1 = [1, 1]
list2 = [1, 1]

print(list1 is list2)
print(list1 == list2)

# Operator == porównuje wartości obiektów.
# Operator is sprawdza, czy zmienne wskazują na ten sam obiekt w pamięci.
# list1 i list2 mają taką samą zawartość, dlatego list1 == list2 zwraca True.
# Są jednak dwoma różnymi listami utworzonymi w pamięci, dlatego
# list1 is list2 zwraca False.