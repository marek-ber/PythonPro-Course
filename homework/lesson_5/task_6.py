# 6. Gra "Zgadnij liczbę":
# Program "myśli" o liczbie (np. sekret = 42 ).
# Użyj pętli while True , aby w nieskończoność prosić użytkownika o podanie liczby.
# Wewnątrz pętli, sprawdź, czy podana liczba jest równa sekretnej. Jeśli tak, wyświetl
# gratulacje i użyj break , aby zakończyć grę. Jeśli nie, poinformuj, że to zła liczba.

sekret = 42

while True:
    number = int(input("Podaj liczbę: "))
    if number == sekret:
        print("Gratulacje")
        break
    else:
        print("Zła liczba próbuj dalej")

