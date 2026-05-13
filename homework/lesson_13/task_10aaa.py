












# Zadanie 3 – Wyświetl całą bibliotekę
# conn = sqlite3.connect("biblioteka.db")
# cur = conn.cursor()

# cur.execute("SELECT * FROM ksiazki")
# for wiersz in cur.fetchall():
#     print(wiersz)

# conn.close()
# Zadanie 4 – Wyszukaj książki autora
# ulubiony_autor = "J.K. Rowling"

# conn = sqlite3.connect("biblioteka.db")
# cur = conn.cursor()

# cur.execute("SELECT * FROM ksiazki WHERE autor = ?", (ulubiony_autor,))
# for wiersz in cur.fetchall():
#     print(wiersz)

# conn.close()
# Zadanie 5 – Zaktualizuj rok wydania
# conn = sqlite3.connect("biblioteka.db")
# cur = conn.cursor()

# # zmieniamy rok wydania "Władca Pierścieni"
# cur.execute("UPDATE ksiazki SET rok_wydania = ? WHERE tytul = ?", (1955, "Władca Pierścieni"))

# # potwierdzamy zmianę
# cur.execute("SELECT * FROM ksiazki WHERE tytul = ?", ("Władca Pierścieni",))
# print(cur.fetchone())

# conn.commit()
# conn.close()
# Zadanie 6 – Dwie tabele: studenci i audytoria
# conn = sqlite3.connect("uczelnia.db")
# cur = conn.cursor()

# cur.execute("""
# CREATE TABLE IF NOT EXISTS studenci (
#     id_studenta INTEGER PRIMARY KEY,
#     imie TEXT,
#     nazwisko TEXT
# )
# """)

# cur.execute("""
# CREATE TABLE IF NOT EXISTS audytoria (
#     id_audytorium INTEGER PRIMARY KEY,
#     nazwa_budynku TEXT,
#     numer_sali INTEGER
# )
# """)

# conn.commit()
# conn.close()
# Zadanie 7 – Wypełnij dane uczelni
# conn = sqlite3.connect("uczelnia.db")
# cur = conn.cursor()

# studenci = [
#     ("Anna", "Kowalska"),
#     ("Piotr", "Nowak"),
#     ("Maria", "Wiśniewska"),
#     ("Jan", "Kowalczyk")
# ]

# audytoria = [
#     ("Budynek A", 101),
#     ("Budynek B", 202),
#     ("Budynek C", 303)
# ]

# cur.executemany("INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)", studenci)
# cur.executemany("INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)", audytoria)

# conn.commit()
# conn.close()
# Zadanie 8 – Połącz tabele (przypisania)
# conn = sqlite3.connect("uczelnia.db")
# cur = conn.cursor()

# cur.execute("""
# CREATE TABLE IF NOT EXISTS przypisania (
#     id_przypisania INTEGER PRIMARY KEY,
#     id_studenta INTEGER,
#     id_audytorium INTEGER,
#     FOREIGN KEY(id_studenta) REFERENCES studenci(id_studenta),
#     FOREIGN KEY(id_audytorium) REFERENCES audytoria(id_audytorium)
# )
# """)

# conn.commit()
# conn.close()
# Zadanie 9 – Dokonaj przypisań
# conn = sqlite3.connect("uczelnia.db")
# cur = conn.cursor()

# # pobieramy studentów i audytoria
# cur.execute("SELECT id_studenta FROM studenci")
# studenci_ids = [row[0] for row in cur.fetchall()]

# cur.execute("SELECT id_audytorium FROM audytoria")
# audytoria_ids = [row[0] for row in cur.fetchall()]

# # przypisujemy studentów do audytoriów w pętli
# przypisania = [(studenci_ids[i], audytoria_ids[i % len(audytoria_ids)]) for i in range(len(studenci_ids))]

# cur.executemany("INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)", przypisania)

# conn.commit()
# conn.close()
# Zadanie 10 – Funkcja wyszukująca z JOIN
# def znajdz_sale_studenta(nazwisko):
#     conn = sqlite3.connect("uczelnia.db")
#     cur = conn.cursor()

#     cur.execute("""
#         SELECT a.nazwa_budynku, a.numer_sali
#         FROM studenci s
#         JOIN przypisania p ON s.id_studenta = p.id_studenta
#         JOIN audytoria a ON p.id_audytorium = a.id_audytorium
#         WHERE s.nazwisko = ?
#     """, (nazwisko,))

#     wyniki = cur.fetchall()
#     if wyniki:
#         for budynek, sala in wyniki:
#             print(f"Student {nazwisko} jest przypisany do budynku {budynek}, sala {sala}")
#     else:
#         print(f"Nie znaleziono studenta o nazwisku {nazwisko}")

#     conn.close()

# # Przykład użycia:
# znajdz_sale_studenta("Kowalska")