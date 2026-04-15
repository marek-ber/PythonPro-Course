# 4. Formatowanie print() : Napisz program, który wyświetli listę zakupów:
# "jajka,mleko,chleb" . Użyj funkcji print() z trzema argumentami tekstowymi i
# odpowiednio ustawionym parametrem sep .

item1 = "jajka"
item2 = "mleko"
item3 = "chleb"

print(item1, item2, item3, sep=",")

shopping_list = ["jajka", "mleko", "chleb"]
print(*shopping_list, sep=",")

print(*(item.lower() for item in shopping_list), sep=",")
print(*(item.capitalize() for item in shopping_list), sep=",")
print(*(item.title() for item in shopping_list), sep=",")