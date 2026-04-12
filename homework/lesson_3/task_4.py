# 4. Praca z f-stringami: Poproś użytkownika o jego imię i rok urodzenia. Oblicz jego
# przybliżony wiek i wyświetl komunikat w formacie: "Cześć, [Imię]! W 2025 roku
# będziesz mieć około [Wiek] lat."

name = input("Podaj swoje imię: ")
birth_year = int(input("Podaj rok urodzenia: "))

age = 2026 - birth_year

print(f"Cześć {name}! w 2026 roku będziesz mieć około {age} lat.")