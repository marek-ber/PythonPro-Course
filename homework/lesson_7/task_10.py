# 10. Mini-projekt: Przetwarzanie danych: Masz listę słowników reprezentujących
# użytkowników:
# Napisz jednolinijkowy kod (używając kombinacji filter , map lub list comprehension),
# który zwróci listę imion aktywnych użytkowników, którzy mają 18 lat lub więcej, pisanych
# wielkimi literami.
# uzytkownicy = [
# {"imie": "Jan", "wiek": 30, "aktywny": True},
# {"imie": "Anna", "wiek": 17, "aktywny": False},
# {"imie": "Piotr", "wiek": 25, "aktywny": True}


users = [
{"imie": "Jan", "wiek": 30, "aktywny": True},
{"imie": "Anna", "wiek": 17, "aktywny": False},
{"imie": "Piotr", "wiek": 25, "aktywny": True}]

on_line = [ok["imie"].upper() for ok in users if ok["aktywny"] and ok["wiek"] >= 18]

print(on_line)

