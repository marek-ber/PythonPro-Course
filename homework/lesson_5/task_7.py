# 7. Tylko samogłoski: Poproś użytkownika o zdanie. Użyj pętli for oraz instrukcji continue ,
# aby wyświetlić tylko samogłoski z tego zdania. (Wskazówka: if litera not in
# "aeiouy": continue ).

vowel = "aeiouy"

sentence = input("Podaj swoje zdanie: ").lower()

print("Samogłoski w zdaniu: ")

for letter in sentence:
    if letter not in vowel:   
        continue
    print(letter, end=" ")