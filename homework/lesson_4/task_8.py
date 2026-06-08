# 8. Obliczanie wieku psa: Przyjmuje się, że pierwszy rok życia psa to 15 ludzkich lat, drugi to
# 9, a każdy kolejny to 5. Napisz program, który pyta o wiek psa w latach, a następnie oblicza
# i wyświetla jego wiek w "ludzkich" latach.

dog_age = int(input("Podaj wiek psa: "))

if dog_age == 1:
    human_age = 15
elif dog_age == 2:
    human_age = 24
elif dog_age > 2:
    human_age = 15 + 9 + (dog_age - 2) * 5
else:
    human_age = 0

print(f"Twój pies ma {human_age} ludzkich lat")