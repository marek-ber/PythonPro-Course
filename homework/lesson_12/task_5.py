# 5. ✏ Zadanie 5 – Odczyt pliku
# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
# try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
# użytkownikowi.


try:
    file = open("config.json")
    print(file.read())
except FileNotFoundError:
    print('Plik o podanej nazwie nie istnieje')