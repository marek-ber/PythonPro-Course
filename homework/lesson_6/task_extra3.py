# Ćwiczenie S3: Pozdrowienie z domyślnym językiem
# Napisz funkcję pozdrow(imie, jezyk="pl"). Dla "pl" zwraca "Cześć, {imie}!", dla "en" — "Hello,
# {imie}!", dla "de" — "Hallo, {imie}!". Dla nieznanego języka: "Hi, {imie}!".
# Wskazówka: if/elif/else z return dla każdego języka.

def regard(name: str, language: str = "pl") -> str:
    if language == "pl":
        return f"Cześć, {name}!"
    if language == "en":
        return f"Hello, {name}!"
    if language == "de":
        return f"Hallo, {name}!"
    else:
        return f"Hi, {name}!"
    
name = input("Imię:  ")
language = input("Wybierz język (pl, en, de, other): ")

print(f"{regard(name, language)}")