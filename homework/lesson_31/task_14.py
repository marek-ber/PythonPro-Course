import asyncio


async def producent(queue):
    for liczba in range(1, 11):
        await queue.put(liczba)
        print(f'Producent dodał: {liczba}')
        await asyncio.sleep(0.2)

    await queue.put(None)


async def konsument(queue):
    while True:
        liczba = await queue.get()

        if liczba is None:
            queue.task_done()
            break

        print(f'Konsument przetworzył: {liczba ** 2}')
        queue.task_done()
        await asyncio.sleep(0.5)


async def main():
    queue = asyncio.Queue()

    producent_task = asyncio.create_task(producent(queue))
    konsument_task = asyncio.create_task(konsument(queue))

    await producent_task
    await queue.join()
    await konsument_task


asyncio.run(main())
