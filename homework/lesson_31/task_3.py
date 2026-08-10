# 3. ✏ Dwa zadania po kolei
# Stwórz dwie korutyny: zadanie1 śpi przez 2 sekundy i drukuje "Zadanie 1 zakończone", a
# zadanie2 śpi przez 1 sekundę i drukuje "Zadanie 2 zakończone". W głównej korutynie main
# uruchom je sekwencyjnie (używając await na każdej z nich po kolei) i zmierz czas
# wykonania.

import asyncio


async def zadanie1():
    await asyncio.sleep(2)
    print('Zadanie 1 zakończone')


async def zadanie2():
    await asyncio.sleep(1)
    print('Zadanie 2 zakończone')


async def main():
    await zadanie1()
    await zadanie2()


asyncio.run(main())
