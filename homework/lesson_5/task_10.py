# 10. Mini-projekt: Prosty kalkulator walut:
# Zdefiniuj kursy w słowniku, np. kursy = {"USD": 4.0, "EUR": 4.3} .
# W pętli while True zapytaj użytkownika o kwotę w PLN i walutę (USD/EUR).
# Użyj if-elif-else , aby sprawdzić wybraną walutę i obliczyć wynik.
# Sformatuj wynik do dwóch miejsc po przecinku, używając f-stringa.
# Zapytaj użytkownika, czy chce kontynuować. Jeśli odpowie "nie", użyj break .

kursy = {
    "USD": 3.6,
    "EUR": 4.2
}

while True:
    kwota = float(input("Podaj kwotę w PLN: "))
    waluta = input("Podaj walutę (USD/EUR): ").upper()

    if waluta == "USD":
        wynik = kwota / kursy["USD"]
        print(f"Otrzymasz: {wynik:.2f} USD")
    elif waluta == "EUR":
        wynik = kwota / kursy["EUR"]
        print(f"Otrzymasz: {wynik:.2f} EUR")
    else:
        print("Nieznana waluta!")

    kontynuuj = input("Czy chcesz kontynuować? (tak/nie): ").lower()
    if kontynuuj == "nie":
        break