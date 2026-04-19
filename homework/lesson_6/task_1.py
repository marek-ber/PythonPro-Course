# # Kalkulator: Napisz funkcję kalkulator(a, b, operacja) , która przyjmuje dwie liczby i
# # string z operacją ( "+" , "-" , "*" lub / "). Funkcja powinna zwracać wynik
# # odpowiedniego działania.

# 1. Kalkulator
# def kalkulator(a, b, operacja):
#     if operacja == "+":
#         return a + b
#     elif operacja == "-":
#         return a - b
#     elif operacja == "*":
#         return a * b
#     elif operacja == "/":
#         if b == 0:
#             raise ValueError("Nie można dzielić przez zero.")
#         return a / b
#     else:
#         raise ValueError("Nieznana operacja.")

# def calcutale(x: float, y: float, operation: str ) -> float | None:
#     if operation == "+":
#         return x + y
#     elif operation == "-":
#         return x - y
#     elif operation == "*":
#         return x * y
#     elif operation == "/":
#         if(y == 0):
#             return None
#         return x / y
#     return None

# print("+", calcutale(12, 6, "+"))
# print("-",calcutale(12, 6, "-"))
# print("/ z 0: ", calcutale(12, 0, "/"))
# print("/ z: ", calcutale(12, 3, "/"))


def calculator(a: float, b: float, operation: str) -> float | None:
    
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