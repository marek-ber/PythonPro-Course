# 19. 🧠 Generator liczb pierwszych
# Napisz asynchroniczny generator, który co pewien czas (np. 0.1s) "produkuje" kolejną
# liczbę pierwszą. W głównej pętli iteruj po tym generatorze za pomocą async for i wypisuj
# liczby, aż dojdziesz do 100.
# (challenge)

import asyncio


async def generator_danych():
    for i in range(1, 6):
        await asyncio.sleep(1)
        yield i


async def main():
    async for liczba in generator_danych():
        print(f'Nowa wartość: {liczba}')


asyncio.run(main())
