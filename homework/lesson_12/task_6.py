# 6. 🧠 Zadanie 6 – Własny wyjątek InvalidPasswordError
# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
# która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
# (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
# testuje tę funkcję w bloku try...except.


class InvalidPasswordError(Exception):
    pass


def ustaw_haslo(password: str):
    if len(password) < 8:
        raise InvalidPasswordError("Hasło jest za krótkie. Minimum 8 znaków")
    
    return True


try:
    print(ustaw_haslo("admin1234"))
    print(ustaw_haslo("123"))
except InvalidPasswordError as error:
    print(f"Wystąpił błąd - {error}")
