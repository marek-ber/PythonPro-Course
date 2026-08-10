# 5. ✏ Korutyna zwracająca wartość
# Napisz korutynę oblicz_potege(liczba, potega), która po 2 sekundach opóźnienia zwraca
# wynik potęgowania. W main wywołaj ją i wydrukuj otrzymany wynik.



import asyncio


async def oblicz_potege(liczba, potega):
    await asyncio.sleep(2)
    return liczba ** potega


async def main():
    wynik = await oblicz_potege(2, 5)
    print(wynik)


asyncio.run(main())
