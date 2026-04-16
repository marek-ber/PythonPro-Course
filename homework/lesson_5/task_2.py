# 2. Kalkulator zniżek: Napisz program, który oblicza cenę biletu. Cena bazowa to 100 PLN.
# Jeśli użytkownik jest studentem ( tak/nie ) LUB ma mniej niż 18 lat, przysługuje mu 50%
# zniżki. Użyj operatorów or i and .

TICKET_PRICE = 100
age = int(input("Podaj wiek: "))
student = input("Student (tak / nie): ").lower()

if student == "tak" or age < 18:
    print("Cena biletu to:", TICKET_PRICE / 2)
else:
    print("Cena biletu to:", TICKET_PRICE)
