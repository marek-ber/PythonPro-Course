# Mini-projekt "Formater danych": Napisz program, który poprosi użytkownika o jego imię i
# nazwisko w jednej linii (np. " jan kowalski "). Program powinien:
# Oczyścić zbędne białe znaki.
# Sprawić, aby każde słowo zaczynało się wielką literą (metoda .title() ).
# Wyświetlić sformatowane dane oraz ich długość.

full_name = input("Podaj imię i nazwisko: ")

full_name1 = full_name.strip().title()

print(f"Sformatowane: ", {full_name1}, "długość: ", {len(full_name1)})
