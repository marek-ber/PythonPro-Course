# 2. Identyfikator obiektu: Utwórz trzy zmienne ( a , b , c ) z tą samą wartością 256 . Sprawdź
# i wyświetl ich id() . Następnie utwórz trzy zmienne z wartością 257 i również sprawdź ich
# id() . Czy widzisz różnicę w zachowaniu Pythona? Wyjaśnij dlaczego w komentarzu.

a = 256
b = 256
c = 256

print(id(a))
print(id(b))
print(id(c))


d = 257
e = 257
f = 257

print(id(d))
print(id(e))
print(id(f))

# Dla nas są to cyfry które wystepują po sobie dla pythona cyfry powyżej 256 nie są buforowane i wtedy tworzy nowe obiekty.

# Python przechowuje w pamięci (cache) małe liczby całkowite z zakresu od -5 do 256.
# Dlatego zmienne a, b i c wskazują na ten sam obiekt i mają takie samo id().
# Dla liczby 257 Python może tworzyć osobne obiekty, więc id() może być różne.
# Mechanizm ten pozwala oszczędzać pamięć i przyspiesza działanie programu.