# 10. Wstęp do parku rozrywki:
# Utwórz plik task10_access.py .
# Zasada: wpuszczane są dzieci o wzroście od 120 cm I z osobą dorosłą, LUB młodzież
# o wzroście od 160 cm.
# Zapytaj o wzrost i czy jest opiekun ( "tak" / "nie" ).
# Używając and i or , określ, czy można wpuścić gościa, i wyświetl True lub False 

wzrost = int(input("Podaj wzrost (cm): "))
opiekun = input("Czy jest opiekun? (tak/nie): ").lower()

print((wzrost >= 120 and opiekun == "tak") or wzrost >= 160)