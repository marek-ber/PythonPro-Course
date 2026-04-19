# Ćwiczenie S1: Pole trójkąta
# Napisz funkcję pole_trojkata(podstawa, wysokosc) zwracającą pole trójkąta (podstawa *
# wysokosc / 2). Przetestuj z różnymi wartościami.
# Wskazówka: Jeden return z wyrażeniem.

def triangle_area(base: float, height: float) -> float:
    return (base * height) / 2

base = float(input("Podstawa trójkąta: "))
height = float(input("Wysokość trójkąta: "))


print(f"Pole trójkąta wynosi: {triangle_area(base, height)}")

