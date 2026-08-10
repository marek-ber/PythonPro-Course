# 12. 🧠 Kto pierwszy, ten lepszy
# Uruchom 5 zadań, z których każde śpi przez losowy czas (od 1 do 10 sekund), a następnie
# zwraca swój czas uśpienia. Napisz program, który zakończy działanie i wypisze wynik
# pierwszego zakończonego zadania, nie czekając na pozostałe. Wskazówka: użyj
# asyncio.wait() z argumentem return_when=asyncio.FIRST_COMPLETED.
# (challenge)

import asyncio
import random


async def zadanie(numer):
    czas = random.uniform(1, 5)
    await asyncio.sleep(czas)
    return f'Zadanie {numer} wygrało po {czas:.2f} s'


async def main():
    taski = [
        asyncio.create_task(zadanie(i))
        for i in range(1, 6)
    ]

    done, pending = await asyncio.wait(
        taski,
        return_when=asyncio.FIRST_COMPLETED,
    )

    pierwsze = done.pop()
    print(pierwsze.result())

    for task in pending:
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)


asyncio.run(main())
