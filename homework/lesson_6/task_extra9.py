# Ćwiczenie S9: Walidator emaila
# Napisz funkcję sprawdz_email(email: str) -> bool, która zwraca True jeśli email zawiera
# dokładnie jeden znak "@" i co najmniej jedną kropkę po "@". Dodaj docstring.
# Wskazówka: Sprawdź email.count("@") == 1. Podziel przez "@" (split) i sprawdź czy po prawej
# jest kropka.


def check_email(email: str) -> bool:
    """
    Sprawdza, czy podany adres email ma poprawny format:
    zawiera dokładnie jeden znak '@' i co najmniej jedną kropkę po nim.
    """

    if email.count("@") != 1:
        return False
    parts = email.split("@")
    dot = parts[1]

    return "." in dot

user = input("Podaj maila: ")
checker = check_email(user)

if checker:
    print("Twój email jest poprawny.")
else:
    print("Email niepoprawny")