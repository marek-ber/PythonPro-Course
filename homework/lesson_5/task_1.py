# 1. Analiza wieku: Napisz program, który pobiera od użytkownika wiek. Używając instrukcji
# if-elif-else , wyświetl jeden z komunikatów: "Niemowlę" (0-1), "Dziecko" (2-12),
# "Nastolatek" (13-17), "Dorosły" (18-64), "Senior" (65+).

age = int(input("Podaj wiek: "))

if age <= 1:
    print("Niemowlę")
elif age <= 12:
    print("Dziecko")
elif age <= 17:
    print("Nastolatek")
elif age <= 64:
    print("Dorosły") 
else:
    print("Senior")