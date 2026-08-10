# 10. 🧠 Współbieżne odliczanie
# Napisz korutynę odliczanie(nazwa, start), która co sekundę drukuje komunikat "{nazwa}:
# zostało {pozostało} sekund". Uruchom trzy takie odliczania współbieżnie, każde z inną
# nazwą i innym czasem początkowym (np. 5s, 3s, 7s).
# (challenge)

import asyncio


async def odliczanie(nazwa, start):
    for liczba in range(start, 0, -1):
        print(f'{nazwa}: {liczba}')
        await asyncio.sleep(1)
    print(f'{nazwa}: koniec')


async def main():
    await asyncio.gather(
        odliczanie('A', 3),
        odliczanie('B', 5),
        odliczanie('C', 7),
    )


asyncio.run(main())
