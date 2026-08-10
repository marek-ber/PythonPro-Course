# 8. ✏ Asynchroniczny ping
# Napisz korutynę ping(host), która symuluje pingowanie serwera przez
# asyncio.sleep(random.uniform(0.1, 1.0)) i zwraca f"Host {host} odpowiada". Uruchom ją dla
# 5 różnych hostów współbieżnie.


import asyncio
import random


async def ping(host):
    czas = random.uniform(0.5, 2.0)
    await asyncio.sleep(czas)
    return f'{host} odpowiada po {czas:.2f} s'


async def main():
    hosty = [
        'google.com',
        'github.com',
        'python.org',
        'django-project.com',
        'openai.com',
    ]

    wyniki = await asyncio.gather(
        *(ping(host) for host in hosty)
    )

    for wynik in wyniki:
        print(wynik)


asyncio.run(main())
