# 8. Obliczanie wieku psa: Przyjmuje się, że pierwszy rok życia psa to 15 ludzkich lat, drugi to
# 9, a każdy kolejny to 5. Napisz program, który pyta o wiek psa w latach, a następnie oblicza
# i wyświetla jego wiek w "ludzkich" latach.

dog_age = int(input("Podaj wiek psa: "))

if dog_age <= 1:
    print("Twój pies ma 15 lat")
elif dog_age <= 2:
    print("Twój pies ma 24 lata")
elif dog_age > 2:
    older_dog = 15 + 9 + (dog_age - 2) * 5
    print(f"Twój pies ma {older_dog} lat")