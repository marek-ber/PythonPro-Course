# 6. Prawda czy fałsz?: Napisz program, który prosi użytkownika o wpisanie dowolnego tekstu.
# Następnie, używając konwersji na bool , sprawdź, czy wpisany tekst jest "prawdziwy"
# (niepusty) i wyświetl odpowiedni komunikat.

sentence1 = input("Napisz dowolne zdanie: ")

sentence2 = bool(sentence1)

if sentence2:
    print("Tekst jest prawdziwy (niepusty).")
else:
    print("Tekst jest fałszywy (pusty).")