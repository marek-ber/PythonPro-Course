# 9. Identyfikator po zmianie: Utwórz zmienną x = 10 . Wyświetl jej id() . Następnie
# przypisz do x nową wartość x = x + 1 . Ponownie wyświetl id() . Czy identyfikator się
# zmienił? Dlaczego? Odpowiedz w komentarzu.

x = 10

print(id(x))

x = x +1

print(id(x))

# Tak, identyfikator (id) się zmienił.
# Dzieje się tak dlatego, że liczby całkowite (int) w Pythonie są niemutowalne (immutable),
# czyli nie można zmienić ich wartości „w miejscu”.
# Operacja x = x + 1 tworzy nowy obiekt w pamięci o wartości 11,
# a zmienna x zaczyna wskazywać na ten nowy obiekt.
# Dlatego jego identyfikator (adres w pamięci) jest inny niż wcześniej.