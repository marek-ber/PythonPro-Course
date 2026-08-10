# 6. ✏ Symulacja pobierania danych
# Stwórz korutynę pobierz_pogode(miasto), która po 1.5 sekundy zwraca słownik z fikcyjnymi
# danymi pogodowymi, np. {'miasto': miasto, 'temperatura': 25, 'stan': 'słonecznie'}.


import asyncio


async def pobierz_pogode(miasto):
    await asyncio.sleep(1.5)
    return {
        'miasto': miasto,
        'temperatura': 22,
        'pogoda': 'słonecznie',
    }


async def main():
    pogoda = await pobierz_pogode('Kraków')
    print(pogoda)


asyncio.run(main())
