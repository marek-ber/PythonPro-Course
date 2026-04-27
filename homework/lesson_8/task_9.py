# 9. Kontekstowy menedżer with : Pokaż, jak instrukcja with open(...) as f: upraszcza
# kod z zadania 3, eliminując potrzebę jawnego używania bloku finally do zamykania
# pliku.





def czytaj_plik(nazwa):
    try:
        with open(nazwa, "r") as f:
            tresc = f.read()
            print(tresc)
    except FileNotFoundError:
        print("Plik nie istnieje.")
    except PermissionError:
        print("Brak uprawnień do odczytu pliku.")

