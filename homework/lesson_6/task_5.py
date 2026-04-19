# # 5. Adnotacje i docstring: Weź funkcję kalkulator z zadania 1. Dodaj do niej pełne
# # adnotacje typów dla wszystkich parametrów i wartości zwracanej. Napisz również
# # kompletny docstring opisujący jej działanie.

def calculator(a: float, b: float, operation: str) -> float | None:
    """
    Docstring for calculator
    
    :Wykonuje podstawową operacje matematyczną pobierając od użytkownika dwie liczby
    
    :Parametry:
    :a (float): pierwsza liczba
    :b (float): druga liczba
    :operation (str): operator matematyczny

    :Zwraca: 
    :Wynik działania (float)
    
    :Sprawdza czy dzielenie nie jest przy użyciu wartości 0
    """
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            return None
        return a / b
    
a = float(input("Podaj pierwszą cyfrę: "))
b = float(input("Podaj drugą cyfrę: "))
operation = input("Podaj działanie (+, -, *, /): ")

result = calculator(a, b, operation)
print(result)