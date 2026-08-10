# 18. 🧠 Anulowanie zadania
# Stwórz zadanie, które działa w nieskończonej pętli, co sekundę drukując "Pracuję...". W
# głównej korutynie main, pozwól mu pracować przez 5 sekund, a następnie je anuluj 
# (task.cancel()). W "pracującej" korutynie obsłuż wyjątek asyncio.CancelledError, aby
# wydrukować komunikat "Anulowano, sprzątam..." przed jej ostatecznym zakończeniem.
# (challenge)


import asyncio


async def pracownik():
    try:
        while True:
            print('Pracuję...')
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('Zadanie zostało anulowane.')
        raise


async def main():
    task = asyncio.create_task(pracownik())

    await asyncio.sleep(5)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print('Anulowanie obsłużone w main().')


asyncio.run(main())
