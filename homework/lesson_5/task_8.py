# 8. Wyszukiwarka w liście: Stwórz listę imion: imiona = ["Anna", "Jan", "Piotr",
# "Kasia"] . Poproś użytkownika o podanie imienia do wyszukania. Użyj pętli for z
# instrukcją break oraz blokiem else , aby:
# Jeśli imię zostanie znalezione, wyświetlić "Znaleziono!" i przerwać pętlę.
# Jeśli pętla zakończy się bez znalezienia imienia, wyświetlić "Nie znaleziono imienia na
# liście."

names = ["Anna", "Jan", "Piotr", "Kasia"]

user = input("Podaj imię: ").capitalize()

for name in names:
    if user == name:
        print("Znaleziono!")
        break
else:
    print("Nie znaleziono imienia na liście.")
