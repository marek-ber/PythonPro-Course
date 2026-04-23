# 4. Znajdowanie liczb pierwszych: Użyj funkcji filter() , aby z listy liczb od 1 do 30 wybrać
# tylko liczby pierwsze. (Wskazówka: napisz pomocniczą funkcję czy_pierwsza(n) , która
# sprawdza, czy liczba jest pierwsza).

# numbers = list(range(1, 31))

# is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# prime_numbers = list(filter(is_prime, numbers))

# print(numbers)
# print(prime_numbers)


def czy_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = [i for i in range(1, 31)]

filtered_numbers = list(filter(czy_pierwsza, numbers))

print(f"Liczy pierwsze: {filtered_numbers}")