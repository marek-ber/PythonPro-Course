#   Kalkulator BMI: Napisz program, który zapyta użytkownika o jego wagę w #    kilogramach i
#   wzrost w metrach. Oblicz i wyświetl wskaźnik masy ciała (BMI) według wzoru: #   BMI = waga
#   / (wzrost * wzrost) .

weight = float(input("Podaj wagę [kg]: "))
height = float(input("Podaj wzrost [cm]:"))

bmi = weight / (height**2)
print(f"BMI wynosi {round(bmi, 2)}")
