# 6. Prawda czy fałsz?: Napisz program, który prosi użytkownika o wpisanie dowolnego tekstu.
# Następnie, używając konwersji na bool , sprawdź, czy wpisany tekst jest "prawdziwy"
# (niepusty) i wyświetl odpowiedni komunikat.

sentence = input("Napisz dowolne zdanie: ")

if sentence:
    print("Tekst jest prawdziwy (niepusty).")
else:
    print("Tekst jest fałszywy (pusty).")