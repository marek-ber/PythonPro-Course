# 4. Literowanie słowa: Poproś użytkownika o podanie słowa. Użyj pętli for , aby wyświetlić
# każdą literę tego słowa w osobnej linii, poprzedzoną jej indeksem. Przykład dla "Kot": 0:
# K , 1: o , 2: t .

word = input("Podaj słowo: ")

for i in range(len(word)):
    print(f"{i}: {word[i]}")