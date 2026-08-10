# 7. ✏ Wiele miast
# Używając korutyny z zadania 6, napisz program, który współbieżnie pobierze dane
# pogodowe dla listy miast: ["Warszawa", "Kraków", "Gdańsk"] i wydrukuje wyniki.
# (proste)


import asyncio


async def pobierz_pogode(miasto):
    await asyncio.sleep(1.5)
    return {
        'miasto': miasto,
        'temperatura': 22,
        'pogoda': 'słonecznie',
    }


async def main():
    miasta = ['Kraków', 'Warszawa', 'Gdańsk']

    wyniki = await asyncio.gather(
        *(pobierz_pogode(miasto) for miasto in miasta)
    )

    for wynik in wyniki:
        print(wynik)


asyncio.run(main())
