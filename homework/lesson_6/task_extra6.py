# Ćwiczenie S6: Karta ucznia
# Napisz funkcję karta_ucznia(imie, klasa, **oceny) zwracającą słownik. Klucze: "imie", "klasa",
# "oceny" (słownik ocen), "srednia" (średnia z ocen). Np. karta_ucznia("Jan", "3B", matematyka=4,
# fizyka=5).
# Wskazówka: Średnia = sum(oceny.values()) / len(oceny).

def student_card(name: str, klasa: str, **grades: float) -> dict:
    average = sum(grades.values()) / len(grades)

    return {
        "Imię: ": name,
        "Klasa: ": klasa,
        "Oceny: ": grades,
        "Średnia: ": average
    }

# print(student_card("Jan", "3B", matematyka = 4, fizyka = 5, biologia =3 ))

name = input("Podaj imię i Nazwisko: ")
klasa = input("Klasa: ")
student_grades = {}

while True:
    subject = input("Podaj przedmiot (jeśli koniec wpisz: end): ")
    if subject == "end":
        break
    grade = float(input("Wpisz ocene: "))
    student_grades[subject] = grade

card = student_card(name, klasa, **student_grades)
for i, v in card.items():
    print(f"{i} {v}")

