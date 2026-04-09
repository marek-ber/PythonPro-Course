# 2. Interaktywny dialog: Napisz program, który zapyta użytkownika o jego imię, wiek i miasto
# zamieszkania. Następnie wyświetl podsumowanie w jednej linijce, np.: "A więc, masz на
# imię [Imię], masz [Wiek] lat i mieszkasz w mieście [Miasto]."

imie = input("Podaj swoje imię: ")
wiek = int(input("Podaj swoj wiek: "))
miasto = input("Podaj miasto zamieszkania: ")

print(f"A więc masz na imię {imie}, masz {wiek} lat i mieszkasz w mieście {miasto}")