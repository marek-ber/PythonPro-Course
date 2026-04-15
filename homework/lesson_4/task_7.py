# 7. Błąd konwersji: Napisz program, który świadomie spróbuje przekonwertować słowo
# "Python" na liczbę całkowitą. Uruchom go, zobacz błąd ValueError , a następnie
# "napraw" program, umieszczając błędną linię w komentarzu i dodając wyjaśnienie, dlaczego
# kod nie działał.

word = int("Python")

# Kod nie działał, ponieważ funkcja int() może konwertować tylko napisy,
# które reprezentują liczby (np. "123"), a nie dowolny tekst.