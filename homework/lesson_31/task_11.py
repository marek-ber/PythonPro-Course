# 11. 🧠 Sumowanie wyników zadań
# Napisz korutynę dlugie_obliczenia(), która po losowym czasie (od 2 do 5 sekund) zwraca
# losową liczbę całkowitą (od 1 do 100). Uruchom 10 takich zadań współbieżnie i po
# zakończeniu wszystkich oblicz i wypisz sumę ich wyników.
# (challenge)



import asyncio
import random


async def losuj_wynik(numer):
    await asyncio.sleep(random.uniform(2, 5))
    wynik = random.randint(1, 100)
    print(f'Zadanie {numer}: {wynik}')
    return wynik


async def main():
    wyniki = await asyncio.gather(
        *(losuj_wynik(i) for i in range(1, 11))
    )

    print(f'Suma: {sum(wyniki)}')


asyncio.run(main())
