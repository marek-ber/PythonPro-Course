# Ćwiczenie S5: Budowanie zdania
# Napisz funkcję buduj_zdanie(*slowa, separator=" ") zwracającą string ze wszystkich słów
# połączonych separatorem. Np. buduj_zdanie("Ala", "ma", "kota") daje "Ala ma kota".
# Wskazówka: Użyj separator.join(slowa).

def sentence(*words: str, separator: str =" ") -> str:
    return separator.join(words)

print(sentence("Ala", "ma", "kota"))

