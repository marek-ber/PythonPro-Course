# # 8. Tworzenie profilu: Napisz funkcję stworz_profil(imie, **dane_dodatkowe) , która
# # przyjmuje imię oraz dowolną liczbę nazwanych argumentów (np. wiek=30 ,
# # miasto="Warszawa" ). Funkcja powinna zwrócić słownik z profilem użytkownika, gdzie
# # klucz 'imie' jest obowiązkowy, a reszta danych jest pobierana z **dane_dodatkowe .

def profile(name: str, **additional_data: str) -> dict:
    if name == "":
        print("Imię jest obowiązkowe")
    else:
        return f"Profil użytkownika: {name}, dane dodatkowe: {additional_data}"


print(profile("Marek", lastname = "Berny", wiek = 37, city = "Krzeszowice"))