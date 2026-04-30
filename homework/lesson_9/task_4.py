# 4. Odczyt konfiguracji: Napisz program, który odczytuje plik config.json z poprzedniego
# zadania i wyświetla komunikat: Witaj, [uzytkownik]! Twój motyw to [motyw].


import json

with open("config.json", "r", encoding="utf-8") as file:
    konfiguracja = json.load(file)

print(f"Witaj, {konfiguracja["użytkownik"]}, Twój moty to {konfiguracja["motyw"]}.")
