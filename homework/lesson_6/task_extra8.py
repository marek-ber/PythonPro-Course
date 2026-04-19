# Ćwiczenie S8: Suma rekurencyjna
# Napisz funkcję suma_do(n) obliczającą sumę liczb od 1 do n rekurencyjnie. Przypadek bazowy: n
# == 1 daje 1. Krok: n + suma_do(n - 1).
# Wskazówka: Analogicznie do silni, ale zamiast mnożenia jest dodawanie.

def suma_do(n):
    if n == 1:
        return 1
    else:
        return n + suma_do(n-1)
    
n = int(input("Podaj cyfrę: "))

print(f"Suma rekurencyjna: {suma_do(n)}")