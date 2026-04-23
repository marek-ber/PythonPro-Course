# 9. Dekorator z argumentem: Stwórz dekorator @powtorz(n) , który przyjmuje argument n i
# powoduje, że udekorowana funkcja zostanie wykonana n razy.


def powtorz(n):
    def dekorator(funkcja):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funkcja(*args, **kwargs)
        return wrapper
    return dekorator


@powtorz(3)
def powiedz_czesc():
    print("Cześć!")


powiedz_czesc()