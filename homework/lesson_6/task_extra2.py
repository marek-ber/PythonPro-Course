# Ćwiczenie S2: Zamiana temperatury
# Napisz dwie funkcje: celsius_na_fahrenheit(c) i fahrenheit_na_celsius(f). Wzory: F = C * 9/5 + 32
# i C = (F - 32) * 5/9. Przetestuj obie.
# Wskazówka: Każda funkcja to jedno obliczenie i return.


def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


temp_c = float(input("Podaj temp w C: "))
temp_f = float(input("Podaj temp w F: "))

print(f"{temp_c}°C = {celsius_to_fahrenheit(temp_c)}°F")
print(f"{temp_f}°F = {fahrenheit_to_celsius(temp_f)}°C")