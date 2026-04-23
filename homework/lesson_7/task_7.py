# 7. Dekorator logujący: Napisz dekorator @loguj , który przed wywołaniem udekorowanej
# funkcji wypisze komunikat Uruchamiam funkcję [nazwa_funkcji]... , a po jej
# zakończeniu Zakończono funkcję [nazwa_funkcji]. .



def loguj(funkcja):
    def wrapper(*args, **kwargs):
        print(f"Uruchamiam funkcję {funkcja.__name__}...")
        wynik = funkcja(*args, **kwargs)
        print(f"Zakończono funkcję {funkcja.__name__}.")
        return wynik
    return wrapper


@loguj
def przyklad():
    print("Wykonuję funkcję.")
