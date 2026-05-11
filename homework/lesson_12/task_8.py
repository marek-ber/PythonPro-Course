# 8. 🧠 Zadanie 8 – Kalkulator z pełną obsługą błędów
# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec
# obliczeń.".

def plus(a: float, b: float) -> float:
    return a + b

def minus(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    return a / b


def execute(a: float, b: float, op: str) -> float:
    if op == "+":
        return plus(a, b)
    if op == "-":
        return minus(a, b)
    if op == "*":
        return multiplication(a, b)
    if op == "/":
        return division(a, b)
    else:
        raise ValueError("Nieznana operacja")


history = []

while True:
    try:
        a = float(input("Podaj pierwszą liczbę: "))
        op = input("Podaj działanie matematyczne (+, -, *, /): ")
        b = float(input("Podaj drugą liczbę: "))

        result = execute(a, b, op)

    except ValueError:
        print("Musisz podać liczby lub poprawną operację.")

    except ZeroDivisionError:
        print("Błąd: Dzielenie przez 0")

    else:
        print(f"Wynik: {result}")
        history.append(f"{a} {op} {b} = {result}")

    finally:
        print("Koniec obliczeń.")

    next_op = input("Czy chcesz wykonać kolejne działanie (t / n): ")
    if next_op == "n":
        break

print("\nHistoria działań:", *history, sep="\n")