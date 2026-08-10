# 2. ✏ Asynchroniczny licznik
# Napisz korutynę licznik(n), która przyjmuje liczbę n i co sekundę wypisuje kolejne liczby od
# 1 do n. Użyj asyncio.sleep(1).

import asyncio


async def licznik(n):
    for i in range(1, n + 1):
        print(i)
        await asyncio.sleep(1)


asyncio.run(licznik(5))
