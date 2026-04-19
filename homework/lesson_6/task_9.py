# # 9. Silnia (rekurencja): Napisz funkcję silnia(n: int) -> int , która oblicza silnię liczby n
# # w sposób rekurencyjny (czyli wywołując samą siebie). Pamiętaj o warunku bazowym: silnia
# # z 0 to 1. (Wzór: n! = n * (n-1)! ).

def factorial(n: int) -> int:
    if n < 0:
        return -1
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

n = int(input("Podaj liczbę: "))
result = factorial(n)

print(f"Silnia liczby {n}: {result}")
