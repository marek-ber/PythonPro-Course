# Ćwiczenie S1: Notatnik jednorazowy
# Napisz program, który pobiera od użytkownika tekst (wiele linii — do wpisania "koniec") i
# zapisuje go do pliku "notatka.txt" w trybie "w". Po zapisaniu wyświetl komunikat z liczbą
# zapisanych linii.
# Wskazówka: Zbieraj linie do listy, potem zapisz "\\n".join(linie) do pliku. Liczba linii to len(linie).
# Ćwiczenie S2: Zliczanie znaków
# Napisz program, który czyta plik i wyświetla: liczbę znaków, liczbę słów i liczbę linii. Obsłuż
# FileNotFoundError.
# Wskazówka: Znaki: len(tekst), slowa: len(tekst.split()), linie: len(tekst.splitlines()).
# Ćwiczenie S3: Kopiowanie pliku
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# Napisz program kopiujący zawartość jednego pliku do drugiego. Pobierz nazwy plików od
# użytkownika. Obsłuż FileNotFoundError.
# Wskazówka: Przeczytaj plik zrodlowy (.read()), zapisz do docelowego (.write()).
# Poziom 2: JSON, CSV, pathlib
# Ćwiczenie S4: Lista kontaktów w JSON
# Napisz program przechowujący kontakty (imie, telefon, email) w pliku JSON. Funkcje: dodaj
# kontakt, wyświetl wszystkie, wyszukaj po imieniu. Dane = lista słowników.
# Wskazówka: Wczytaj listę z JSON przy starcie, zapisz po każdej zmianie. Wyszukiwanie: pętla for
# z if.
# Ćwiczenie S5: Konwerter CSV na JSON
# Napisz program, który czyta plik CSV (z nagłówkami) i zapisuje dane jako JSON. Użyj
# csv.DictReader do odczytu i json.dump do zapisu.
# Wskazówka: csv.DictReader daje słowniki. Zbierz je do listy: dane = list(reader). Zapisz listę jako
# JSON.
# Ćwiczenie S6: Raport z folderu
# Używając pathlib, napisz program który dla podanego folderu wyświetla: liczbę plików, liczbę
# podfolderów, łączny rozmiar plików. Użyj Path.iterdir(), .is_file(), .is_dir(), .stat().st_size.
# Wskazówka: Path("folder").iterdir() daje wszystkie elementy folderu. Sprawdzaj .is_file() i .is_dir()
# w pętli.
# Ćwiczenie S7: Filtrowanie CSV
# Masz plik "uczniowie.csv" z kolumnami: imie, klasa, srednia. Napisz program, który czyta plik i
# tworzy nowy "najlepsi.csv" zawierający tylko uczniów ze średnią powyżej 4.0.
# Wskazówka: DictReader do odczytu, DictWriter do zapisu. Filtruj: if float(wiersz\["srednia"\]) >
# 4.0.
# Poziom 3: łączenie koncepcji
# Ćwiczenie S8: Menedżer wydatków
# Stwórz program z menu:
# Dodaj wydatek (nazwa + kwota)
# Wyświetl wszystkie wydatki
# Pokaż sumę wydatków
# Eksportuj do CSV
# Zapisz i wyjdź
# Dane przechowuj w JSON (lista słowników). Eksport do CSV z nagłówkami "nazwa" i "kwota".
# Wskazówka: Łączysz wzorce z sekcji 2.2, 2.6 i 2.7. Menu w while True, dane w JSON, eksport z
# csv.DictWriter.
# Ćwiczenie S9: Analizator logów
# •
# •
# •
# •
# •
# Napisz program, który czyta plik "log.txt" i generuje raport:
# Ile linii z "ERROR"
# Ile linii z "WARNING"
# Ile linii z "INFO"
# Zapisz raport do pliku "raport.json" jako słownik: {"ERROR": N, "WARNING": N, "INFO": N}.
# Wskazówka: Dla każdej linii sprawdzaj "in". Zliczaj w słowniku. Na koniec json.dump().
# Ćwiczenie S10: Mini-projekt: Książka adresowa z wieloma formatami
# Stwórz program książki adresowej (imie, telefon, email) z menu:
# Dodaj kontakt
# Wyświetl kontakty
# Zapisz jako JSON
# Eksportuj jako CSV
# Eksportuj jako Excel (openpyxl)
# Wczytaj z JSON i wyjdź
# Dane w pamięci jako lista słowników. Trzy formaty eksportu do wyboru.
# Wskazówka: To synteza wszystkich technik z lekcji. Każdy format eksportu to osobna funkcja.
# Menu w while True, dane wczytywane z JSON przy starcie


# S1 — Notatnik jednorazowy
# # s1_notatnik.py

# linie = []

# while True:
#     tekst = input("Wpisz linię (lub 'koniec'): ")
#     if tekst.lower() == "koniec":
#         break
#     linie.append(tekst)

# with open("notatka.txt", "w", encoding="utf-8") as plik:
#     plik.write("\n".join(linie))

# print(f"Zapisano {len(linie)} linii do pliku notatka.txt")
# S2 — Zliczanie znaków
# # s2_zliczanie.py

# nazwa = input("Podaj nazwę pliku: ")

# try:
#     with open(nazwa, "r", encoding="utf-8") as plik:
#         tekst = plik.read()

#     print("Liczba znaków:", len(tekst))
#     print("Liczba słów:", len(tekst.split()))
#     print("Liczba linii:", len(tekst.splitlines()))

# except FileNotFoundError:
#     print("Błąd: Plik nie istnieje.")
# S3 — Kopiowanie pliku
# # s3_kopiowanie.py

# zrodlowy = input("Podaj nazwę pliku źródłowego: ")
# docelowy = input("Podaj nazwę pliku docelowego: ")

# try:
#     with open(zrodlowy, "r", encoding="utf-8") as src:
#         zawartosc = src.read()

#     with open(docelowy, "w", encoding="utf-8") as dst:
#         dst.write(zawartosc)

#     print("Plik został skopiowany.")

# except FileNotFoundError:
#     print("Błąd: Plik źródłowy nie istnieje.")
# 🔹 Poziom 2 — JSON, CSV, pathlib
# S4 — Lista kontaktów w JSON
# # s4_kontakty.py

# import json
# from pathlib import Path

# plik = Path("kontakty.json")

# if plik.exists():
#     with open(plik, "r", encoding="utf-8") as f:
#         kontakty = json.load(f)
# else:
#     kontakty = []

# def zapisz():
#     with open(plik, "w", encoding="utf-8") as f:
#         json.dump(kontakty, f, indent=4, ensure_ascii=False)

# while True:
#     print("\n1. Dodaj kontakt")
#     print("2. Wyświetl wszystkie")
#     print("3. Wyszukaj po imieniu")
#     print("4. Wyjdź")

#     wybor = input("Wybór: ")

#     if wybor == "1":
#         imie = input("Imię: ")
#         telefon = input("Telefon: ")
#         email = input("Email: ")

#         kontakty.append({
#             "imie": imie,
#             "telefon": telefon,
#             "email": email
#         })
#         zapisz()

#     elif wybor == "2":
#         for k in kontakty:
#             print(k)

#     elif wybor == "3":
#         szukane = input("Podaj imię: ")
#         for k in kontakty:
#             if k["imie"].lower() == szukane.lower():
#                 print(k)

#     elif wybor == "4":
#         break
# S5 — Konwerter CSV → JSON
# # s5_csv_na_json.py

# import csv
# import json

# csv_plik = input("Podaj nazwę pliku CSV: ")
# json_plik = input("Podaj nazwę pliku JSON do zapisu: ")

# with open(csv_plik, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     dane = list(reader)

# with open(json_plik, "w", encoding="utf-8") as f:
#     json.dump(dane, f, indent=4, ensure_ascii=False)

# print("Konwersja zakończona.")
# S6 — Raport z folderu
# # s6_raport_folderu.py

# from pathlib import Path

# folder = Path(input("Podaj ścieżkę do folderu: "))

# liczba_plikow = 0
# liczba_folderow = 0
# rozmiar = 0

# for element in folder.iterdir():
#     if element.is_file():
#         liczba_plikow += 1
#         rozmiar += element.stat().st_size
#     elif element.is_dir():
#         liczba_folderow += 1

# print("Liczba plików:", liczba_plikow)
# print("Liczba folderów:", liczba_folderow)
# print("Łączny rozmiar plików (bajty):", rozmiar)
# S7 — Filtrowanie CSV
# # s7_filtrowanie_csv.py

# import csv

# with open("uczniowie.csv", "r", encoding="utf-8") as src, \
#      open("najlepsi.csv", "w", newline="", encoding="utf-8") as dst:

#     reader = csv.DictReader(src)
#     writer = csv.DictWriter(dst, fieldnames=reader.fieldnames)
#     writer.writeheader()

#     for wiersz in reader:
#         if float(wiersz["srednia"]) > 4.0:
#             writer.writerow(wiersz)

# print("Utworzono plik najlepsi.csv")
# 🔹 Poziom 3 — Łączenie koncepcji
# S8 — Menedżer wydatków
# # s8_menedzer_wydatkow.py

# import json
# import csv
# from pathlib import Path

# plik = Path("wydatki.json")

# if plik.exists():
#     with open(plik, "r", encoding="utf-8") as f:
#         wydatki = json.load(f)
# else:
#     wydatki = []

# def zapisz():
#     with open(plik, "w", encoding="utf-8") as f:
#         json.dump(wydatki, f, indent=4, ensure_ascii=False)

# while True:
#     print("\n1. Dodaj wydatek")
#     print("2. Wyświetl wydatki")
#     print("3. Pokaż sumę")
#     print("4. Eksport do CSV")
#     print("5. Zapisz i wyjdź")

#     wybor = input("Wybór: ")

#     if wybor == "1":
#         nazwa = input("Nazwa: ")
#         kwota = float(input("Kwota: "))
#         wydatki.append({"nazwa": nazwa, "kwota": kwota})

#     elif wybor == "2":
#         for w in wydatki:
#             print(w)

#     elif wybor == "3":
#         suma = sum(w["kwota"] for w in wydatki)
#         print("Suma wydatków:", suma)

#     elif wybor == "4":
#         with open("wydatki.csv", "w", newline="", encoding="utf-8") as f:
#             writer = csv.DictWriter(f, fieldnames=["nazwa", "kwota"])
#             writer.writeheader()
#             writer.writerows(wydatki)
#         print("Wyeksportowano do wydatki.csv")

#     elif wybor == "5":
#         zapisz()
#         break
# S9 — Analizator logów
# # s9_analizator_logow.py

# import json

# liczniki = {"ERROR": 0, "WARNING": 0, "INFO": 0}

# with open("log.txt", "r", encoding="utf-8") as f:
#     for linia in f:
#         for klucz in liczniki:
#             if klucz in linia:
#                 liczniki[klucz] += 1

# with open("raport.json", "w", encoding="utf-8") as f:
#     json.dump(liczniki, f, indent=4)

# print("Raport zapisany do raport.json")
# S10 — Mini-projekt: Książka adresowa (JSON + CSV + Excel)

# Wymaga:

# pip install openpyxl
# # s10_ksiazka_adresowa.py

# import json
# import csv
# from pathlib import Path
# from openpyxl import Workbook

# plik = Path("ksiazka.json")

# if plik.exists():
#     with open(plik, "r", encoding="utf-8") as f:
#         kontakty = json.load(f)
# else:
#     kontakty = []

# def zapisz_json():
#     with open(plik, "w", encoding="utf-8") as f:
#         json.dump(kontakty, f, indent=4, ensure_ascii=False)

# def eksport_csv():
#     with open("ksiazka.csv", "w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=["imie", "telefon", "email"])
#         writer.writeheader()
#         writer.writerows(kontakty)

# def eksport_excel():
#     wb = Workbook()
#     ws = wb.active
#     ws.append(["Imię", "Telefon", "Email"])
#     for k in kontakty:
#         ws.append([k["imie"], k["telefon"], k["email"]])
#     wb.save("ksiazka.xlsx")

# while True:
#     print("\n1. Dodaj kontakt")
#     print("2. Wyświetl kontakty")
#     print("3. Zapisz jako JSON")
#     print("4. Eksportuj jako CSV")
#     print("5. Eksportuj jako Excel")
#     print("6. Wyjdź")

#     wybor = input("Wybór: ")

#     if wybor == "1":
#         kontakty.append({
#             "imie": input("Imię: "),
#             "telefon": input("Telefon: "),
#             "email": input("Email: ")
#         })

#     elif wybor == "2":
#         for k in kontakty:
#             print(k)

#     elif wybor == "3":
#         zapisz_json()

#     elif wybor == "4":
#         eksport_csv()

#     elif wybor == "5":
#         eksport_excel()

#     elif wybor == "6":
#         zapisz_json()
#         break