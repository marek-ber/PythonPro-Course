# 10. Mini-projekt: Lista zadań: Stwórz prostą aplikację do zarządzania listą zadań. Program
# powinien:
# Przy starcie próbować wczytać zadania z pliku zadania.json .
# Pozwalać użytkownikowi dodać nowe zadanie.
# Pozwalać wyświetlić wszystkie zadania.
# Przy zamknięciu (lub na polecenie) zapisywać aktualną listę zadań do pliku
# zadania.json 

import json
from pathlib import Path

plik = Path("zadania.json")


if plik.exists():
    with open(plik, "r", encoding="utf-8") as f:
        zadania = json.load(f)
else:
    zadania = []

def zapisz():
    with open(plik, "w", encoding="utf-8") as f:
        json.dump(zadania, f, indent=4, ensure_ascii=False)

while True:
    print("\n1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Zapisz i wyjdź")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        nowe = input("Treść zadania: ")
        zadania.append(nowe)
        print("Dodano zadanie.")
    elif wybor == "2":
        print("\nLista zadań:")
        for i, zad in enumerate(zadania, start=1):
            print(f"{i}. {zad}")
    elif wybor == "3":
        zapisz()
        print("Zapisano zadania. Koniec programu.")
        break
    else:
        print("Nieprawidłowa opcja.")