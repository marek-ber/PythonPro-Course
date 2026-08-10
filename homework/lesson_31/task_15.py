# 15. 🧠 Asynchroniczny zapis do pliku
# Napisz program, w którym 5 korutyn współbieżnie generuje jakieś dane tekstowe (np. "Log
# z korutyny X"). Wszystkie powinny zapisywać swoje logi do jednego pliku. Zapewnij, aby
# dostęp do pliku był zsynchronizowany, żeby wpisy się nie pomieszały. Użyj asyncio.Lock
# oraz biblioteki aiofiles (pip install aiofiles).
# (challenge)


import asyncio
import aiofiles


lock = asyncio.Lock()


async def zapisz_log(numer):
    async with lock:
        async with aiofiles.open('logi.txt', 'a', encoding='utf-8') as plik:
            await plik.write(f'Log z zadania {numer}\n')


async def main():
    await asyncio.gather(
        *(zapisz_log(i) for i in range(1, 6))
    )

    print('Logi zostały zapisane.')


asyncio.run(main())
