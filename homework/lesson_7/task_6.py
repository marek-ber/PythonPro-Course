# 6. Licznik wywołań: Stwórz domknięcie (closure). Napisz funkcję stworz_licznik() , która
# zwraca funkcję. Każde wywołanie zwróconej funkcji powinno zwiększać wewnętrzny licznik i
# zwracać jego aktualną wartość.


def counter():
    number = 0

    def in_counter():
        nonlocal number
        number += 1
        return number
    return in_counter

counter_2 = counter()

print(counter_2())
print(counter_2())
print(counter_2())