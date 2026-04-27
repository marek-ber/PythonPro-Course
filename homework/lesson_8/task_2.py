# 2. Walidator wieku: Stwórz funkcję rejestruj_uzytkownika(wiek) , która rzuca własnym,
# zdefiniowanym przez Ciebie wyjątkiem WiekNiepoprawnyError , jeśli wiek jest mniejszy niż
# 18. Napisz kod, który wywołuje tę funkcję i obsługuje ten wyjątek.




class WiekNiepoprawnyError(Exception):
    pass


def rejestruj_uzytkownika(wiek):
    if wiek < 18:
        raise WiekNiepoprawnyError("Użytkownik musi mieć co najmniej 18 lat.")
    print("Rejestracja zakończona sukcesem.")


try:
    wiek = int(input("Podaj wiek: "))
    rejestruj_uzytkownika(wiek)
except WiekNiepoprawnyError as e:
    print("Błąd:", e)