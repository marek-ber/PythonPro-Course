import database_raw as db


def pokaz_zadania(zadania=None):
    if zadania is None:
        zadania = db.pobierz_zadania()

    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "✓" if zadanie[2] else "✗"
        print(
            f"[{status}] ID: {zadanie[0]}, "
            f"Opis: {zadanie[1]}, Priorytet: {zadanie[3]}"
        )
    print("------------------------\n")


def main():
    db.init_db()

    while True:
        print("Menu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadanie")
        print("6. Edytuj zadanie")
        print("7. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_zadania()

        elif wybor == "2":
            opis = input("Podaj opis zadania: ")

            try:
                priorytet = int(input("Podaj priorytet, np. 1-5: "))
            except ValueError:
                print("Błędny priorytet. Ustawiam domyślnie 1.")
                priorytet = 1

            db.dodaj_zadanie(opis, priorytet)
            print("Zadanie dodane!")

        elif wybor == "3":
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                db.oznacz_jako_zrobione(id_zadania)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == "4":
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                db.usun_zadanie(id_zadania)
                print("Zadanie usunięte!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == "5":
            fraza = input("Podaj szukaną frazę: ")
            wyniki = db.wyszukaj_zadania(fraza)
            pokaz_zadania(wyniki)

        elif wybor == "6":
            try:
                id_zadania = int(input("Podaj ID zadania do edycji: "))
                nowy_opis = input("Podaj nowy opis: ")
                db.edytuj_zadanie(id_zadania, nowy_opis)
                print("Zadanie edytowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == "7":
            print("Do zobaczenia!")
            break

        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()