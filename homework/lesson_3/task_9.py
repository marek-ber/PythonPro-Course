# Bramki logiczne: Napisz program, który poprosi o dwie wartości logiczne ( True lub
# False ). Niech użytkownik wprowadza 1 dla True i 0 dla False . Program powinien
# wyświetlić wyniki operacji AND oraz OR dla tych dwóch wartości.

a = int(input("Podaj pierwszą wartość (1 = True, 0 = False): "))
b = int(input("Podaj drugą wartość (1 = True, 0 = False): "))

a1 = bool(a)
b1 = bool(b)

print("and: ", a1 and b1, "\nor: ",  a1 or b1)
