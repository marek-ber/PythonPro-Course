# 3. Konfiguracja w JSON: Stwórz słownik Pythona z ustawieniami aplikacji, np.
# konfiguracja = {"uzytkownik": "admin", "motyw": "ciemny", "rozdzielczosc":
# [1920, 1080]} . Zapisz ten słownik do pliku config.json z wcięciami i poprawnym
# kodowaniem polskich znaków.


import json

konfiguracja = {
    "użytkownik": "admin",
    "motyw" : "ciemny",
    "rozdzielczość" : [1920, 1080]
}

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(konfiguracja, file, indent=4, ensure_ascii=False)