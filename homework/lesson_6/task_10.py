# # 10. Mini-projekt: Walidator hasła: Stwórz funkcję sprawdz_haslo(haslo: str) -> bool .
# # Funkcja powinna sprawdzać, czy hasło spełnia następujące warunki i zwracać True lub
# # False :
# # Ma co najmniej 8 znaków.
# # Zawiera co najmniej jedną wielką literę.
# # Zawiera co najmniej jedną cyfrę. Napisz do niej pełną dokumentację (docstring i
# # adnotacje).

def check_password(password: str) -> bool:
    """
    Sprawdza, czy hasło spełnia wymagania bezpieczeństwa.
    
    :password: pobieram hasło od użytkownika
    :password: typ str
    
    :Zwraca: sprawdzone wartości hasła
    :False: jeśli nie spełnia wymagań:
        * ma co najmniej 8 znaków.
        * zawiera co najmniej jedną wielką literę.
        * zawiera co najmniej jedną cyfrę.
    :True: jeśli powyższe wymagania zostały spełnione

    """

    if len(password) < 8:
        return False
    big_letter = any(letter.isupper() for letter in password)
    one_digit = any(digit.isdigit() for digit in password)
    return big_letter and one_digit

user_password = input("Podaj hasło: ")
checked = check_password(user_password)

print(f"Twoje hasło to: {checked}")