# 1. Mini-kalkulator: Napisz program, który prosi użytkownika o podanie dwóch liczb, a
# następnie wyświetla wynik ich dodawania, odejmowania, mnożenia i dzielenia. Pamiętaj o
# konwersji typów z input() .

a = float(input("Podaj pierwszą liczbe: "))
b = float(input("Podaj druga liczbę: "))
operation = input("Podaj działanie (+, - , *, /): ")

if operation == "+":
    result = a + b
    print(result)
elif operation == "-":
    result = a - b
    print(result)
elif operation == "*":
    result = a * b
    print(result)
elif operation == "/":
    if b != 0:
        result = a / b
        print(result)
    else:
        print("Nie dzielimy przez zero.")