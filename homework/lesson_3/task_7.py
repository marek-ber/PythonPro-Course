# Niemutowalność krotki:
# Utwórz krotkę punkt = (10, 20, 30) .
# Spróbuj zmienić pierwszy element krotki на 15 .
# Wyjaśnij w komentarzu do kodu, dlaczego wystąpił błąd.



point = (10, 20, 30)

# point[0] = 15  # TypeError
# point[0] = 15

# print(point)

# Krotki są niemutowalne, dlatego nie można zmieniać ich elementów
# po utworzeniu. Próba przypisania nowej wartości do elementu
# powoduje błąd TypeError.

# Jeżeli chciałbyś mieć (15, 20, 30), musisz utworzyć nową krotkę:

point = (10, 20, 30)

point = (15, point[1], point[2])

print(point)
