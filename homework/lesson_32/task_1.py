# 1. ✏ (Proste) Kalkulator opóźnień: Napisz główną korutynę main , która uruchomi 3
# symulowane zadania asyncio.sleep (z opóźnieniami 1, 4, 2 sekundy) używając
# asyncio.gather . Program powinien wypisać całkowity czas wykonania (powinien być
# bliski 4 sekund).


import asyncio
import time

async def main():
    start = time.time()

    await asyncio.gather(
        asyncio.sleep(1),
        asyncio.sleep(4),
        asyncio.sleep(2),
    )

    end = time.time()

    print(f"Czas wykonania: {end - start:.2f} sekundy")

asyncio.run(main())