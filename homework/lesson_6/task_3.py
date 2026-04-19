# 3. Średnia ocen: Napisz funkcję oblicz_srednia(*args) , która przyjmuje dowolną liczbę
# ocen (argumentów pozycyjnych) i zwraca ich średnią arytmetyczną. Jeśli nie podano żadnej
# oceny, powinna zwrócić 0.

def average_grade(*grades: float) -> float:
    return sum(grades) / len(grades) if grades else 0

print(average_grade(1, 3, 5, 6, 3))