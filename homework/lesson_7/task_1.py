# 1. Filtrowanie słów: Mając listę słów slowa = ["jabłko", "banan", "kiwi", "gruszka",
# "truskawka"] , użyj list comprehension, aby stworzyć nową listę zawierającą tylko te
# słowa, które mają więcej niż 5 liter.


slowa = ["jabłko", "banan", "kiwi", "gruszka", "truskawka"]

words = [owoc for owoc in slowa if len(owoc) > 5]

print(words)

