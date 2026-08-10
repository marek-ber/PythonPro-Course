# 4. ✏ Dwa zadania współbieżnie
# Zmodyfikuj kod z poprzedniego zadania. Uruchom obie korutyny współbieżnie, używając
# asyncio.gather(). Zmierz i porównaj czas wykonania.


import asyncio
import time


async def zadanie1():
    await asyncio.sleep(2)
    print('Zadanie 1 zakończone')


async def zadanie2():
    await asyncio.sleep(1)
    print('Zadanie 2 zakończone')


async def main():
    start = time.perf_counter()

    await asyncio.gather(
        zadanie1(),
        zadanie2(),
    )

    print(f'Czas wykonania: {time.perf_counter() - start:.2f} s')


asyncio.run(main())
