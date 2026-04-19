 # 2. Informacje o książce: Stwórz funkcję opis_ksiazki(tytul, autor,
# # rok_wydania=2024) . Funkcja powinna zwracać sformatowany string, np. "Książka
# # '[Tytuł]' została napisana przez [Autor] i wydana w roku [Rok wydania]." .
# # Przetestuj ją, wywołując z argumentami pozycyjnymi i nazwanymi.

# def book_descr(book_title: str, author: str, realise_year: int=2024) -> str:
#     return f"Ksiązka '{book_title}' została napisana przez '{author}' i wydana w roku '{realise_year}'."

# print(book_descr(author = "Eric Matthes", realise_year = 2027, book_title = "Python Instrukcja dla programisty"))
# print(book_descr("Python Instrukcja dla programisty", "Eric Matthes", 2025))

def book_descr(book_title: str, author: str, realise_year: int = 2026) -> str:
    return f"Książka '{book_title}, autorstwa '{author}', została wydana w '{realise_year}"

print(book_descr("Rozdroże kruków", "Andrzej Sapkowski", 2024))