# 5. Logowanie błędów: Zmodyfikuj zadanie 1. tak, aby każdy napotkany wyjątek (wraz z jego
# treścią) był zapisywany do pliku log.txt , a program kontynuował działanie. Użyj bloku
# finally , aby upewnić się, że plik z logami jest zawsze zamykany.s


while True:
    log_file = open("log.txt", "a")

    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        operacja = input("Podaj operację (+, -, *, /): ")

        if operacja == "+":
            wynik = a + b
        elif operacja == "-":
            wynik = a - b
        elif operacja == "*":
            wynik = a * b
        elif operacja == "/":
            wynik = a / b
        else:
            raise ValueError("Nieznana operacja")

    except (ValueError, ZeroDivisionError) as e:
        print("Błąd:", e)
        log_file.write(str(e) + "\n")
    else:
        print("Wynik:", wynik)
    finally:
        log_file.close()
        choice = input("Kolejna operacja? (y / n): ")
        if choice == "n":
            break