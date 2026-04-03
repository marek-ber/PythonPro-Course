wzrost = int(input("Podaj wzrost (cm): "))
opiekun = input("Czy jest opiekun? (tak/nie): ").lower()

print((wzrost >= 120 and opiekun == "tak") or wzrost >= 160)