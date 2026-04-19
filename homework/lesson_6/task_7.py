# # 7. Zwracanie wielu wartości: Stwórz funkcję analiza_listy(lista: list[int]) , która
# # przyjmuje listę liczb i zwraca krotkę zawierającą trzy wartości: minimum, maksimum i sumę
# # elementów z listy.

def list_analysis(*list: int) -> tuple:
    return min(list), max(list), sum(list)

print(list_analysis(1, 4, 6, 7, 44, 99, 100))