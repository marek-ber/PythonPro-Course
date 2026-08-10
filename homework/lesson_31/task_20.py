# 20. 🧠 Timeout dla zadania
# Napisz korutynę, która śpi przez losowy czas od 1 do 5 sekund. Uruchom ją, ale z
# ograniczeniem czasowym na 3 sekundy. Jeśli korutyna nie zakończy się w tym czasie,
# program powinien rzucić wyjątek asyncio.TimeoutError. Obsłuż ten wyjątek i wypisz
# odpowiedni komunikat. Wskazówka: użyj asyncio.wait_for().
# (challenge)

import asyncio
import random


async def zadanie():
    czas = random.randint(1, 5)
    print(f'Zadanie będzie trwało {czas} s')
    await asyncio.sleep(czas)
    return 'Gotowe'


async def main():
    try:
        wynik = await asyncio.wait_for(
            zadanie(),
            timeout=3,
        )
        print(wynik)
    except asyncio.TimeoutError:
        print('Przekroczono limit 3 sekund.')


asyncio.run(main())
