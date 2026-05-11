# 4. ✏ Zadanie 4 – Bezpieczne dzielenie
# Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj bloku
# try...except, aby obsłużyć błąd ZeroDivisionError. Jeśli wystąpi ten błąd, funkcja powinna
# zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!".

def bezpieczne_dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero")
        return None

result= bezpieczne_dzielenie(10,2)
print(f"{result}\n")
result2 = bezpieczne_dzielenie(10,0)
print(result2)