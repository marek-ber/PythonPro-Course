# 4. Kody znaków: Używając funkcji ord() , znajdź i wyświetl kody liczbowe ASCII dla
# pierwszej litery Twojego imienia (wielką i małą literą).

litera = input("Podaj pierwszą litere swojego imienia: ")

mala = litera.lower()
duza = litera.capitalize()

print(f"Duża litera w kodzie ASCII to : {ord(duza)}")
print(f"Mała litera w kodzie ASCII to : {ord(mala)}")



