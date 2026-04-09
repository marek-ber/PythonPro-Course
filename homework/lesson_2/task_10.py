# 10. Mini-projekt "Konwerter Temperatury": Napisz program, który poprosi użytkownika o
# temperaturę w stopniach Celsjusza, przekonwertuje ją na stopnie Fahrenheita według
# wzoru F = C * 9/5 + 32 i wyświetli wynik z wyjaśnieniem.

temp = float(input("Podaj temp. w Celsjuszach: "))

fahr = temp * 9/5 + 32

print(f"Twoja temperatura to {fahr} stopni Fahrenheita. Została ona obliczona według wzoru: F = C * 9/5 + 32")