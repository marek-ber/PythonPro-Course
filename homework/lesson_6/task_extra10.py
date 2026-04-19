# Ćwiczenie S10: Mini-projekt: Kalkulator z historią
# Napisz kalkulator jako zestaw funkcji:
# dodaj(a, b), odejmij(a, b), pomnoz(a, b), podziel(a, b)
# wykonaj(a, b, op) — wywołuje odpowiednią funkcję na podstawie operacji
# W pętli while True: pobieraj dane, wykonuj operacje, wyświetlaj wyniki. Dodaj adnotacje typów i
# docstringi do wszystkich funkcji.
# Wskazówka: W wykonaj() użyj if/elif/else aby wywołać właściwą funkcję


def plus(a: float, b: float) -> float:
    """Zwraca sumę dwóch liczb"""
    return a + b

def minus(a: float, b: float) -> float:
    """Zwraca różnicę dwóch liczb"""
    return a - b

def multiplication(a: float, b: float) -> float:
    """Zwraca iloczyn dwóch liczb"""
    return a * b

def division(a: float, b: float) -> float:
    """Zwraca iloraz dwóch liczb"""
    if b == 0:
        return "Nie dzielimy przez 0"
    return a / b


def execute(a: float, b: float, op: str) -> float:
    """zwraca działanie matematyczne na podstawie symbolu"""
    if op == "+":
        return plus(a, b)
    if op == "-":
        return minus(a, b)
    if op == "*":
        return multiplication(a, b)
    if op == "/":
        return division(a, b)
    
history = []

while True:
    a = float(input("Podaj pierwszą liczbę: "))
    op = input("Podaj działanie matematyczne (+, -, *, /): ")
    b = float(input("Podaj drugą liczbę: "))

    result = execute(a, b, op)
    print(f"Wynik: {result}")

    history.append(f"{a} {op} {b} = {result}")

    next = input("Czy chcesz wykonać kolejne działanie (t / n): ")
    if next == "n":
        break

print("\nHistoria działań: ", *history, sep="\n")