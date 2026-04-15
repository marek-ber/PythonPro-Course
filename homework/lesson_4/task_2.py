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