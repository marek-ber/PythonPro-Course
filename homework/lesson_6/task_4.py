# # 4. Sprawdzanie zakresu: Zdefiniuj zmienną globalną POZIOM_DOSTEPU = "user" . Napisz
# # funkcję, która próbuje zmienić tę zmienną na "admin" bez użycia słowa kluczowego
# # global . Wewnątrz funkcji stwórz zmienną lokalną o tej samej nazwie. Wyświetl wartość
# # zmiennej wewnątrz i na zewnątrz funkcji, aby zobaczyć różnicę.

ACCESS_LEVEL = "user"

def login():
    ACCESS_LEVEL = "admin"
    return print(f"Wewnątrz funkcji, {ACCESS_LEVEL}")
        

print(f"Na zewnątrz funkcji: {ACCESS_LEVEL}")

print(login())