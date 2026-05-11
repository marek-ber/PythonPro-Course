# 9. 🧠 Zadanie 9 – Walidacja danych w init
# Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
# Wewnątrz konstruktora dodaj walidację:
# Sprawdź, czy email zawiera znak @ . Jeśli nie, podnieś wyjątek ValueError z
# odpowiednim komunikatem.
# Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. Użyj bloku
# try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi
# danymi. (challenge)

class RejestracjaUzytkownika:
    def __init__(self, email, haslo):
        if "@" not in email:
            raise ValueError("Email musi zawierać '@'.")
        if len(haslo) < 8:
            raise ValueError("Hasło jest za krótkie.")    
        
        self.email = email
        self.haslo = haslo
    
try:
    user = RejestracjaUzytkownika("marek@gmail.com", "marekmarek")
    print("Rejestracja zakończona sukcesem.")

except ValueError as e:
    print("Błąd:", e)

