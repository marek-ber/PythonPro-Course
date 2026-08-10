# 13. 🧠 (Challenge) Aiohttp Klient - Gather: Rozbuduj zadanie 12. Napisz korutynę
# fetch(session, url) , która pobiera dane. W main stwórz listę 3 różnych URL-i (np. z
# https://api.publicapis.org/random?auth=null - wywołaj 3 razy) i użyj
# asyncio.gather , aby pobrać je wszystkie jednocześnie.



import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
    ]

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            fetch(session, urls[0]),
            fetch(session, urls[1]),
            fetch(session, urls[2]),
        )
    for result in results:
        print(result)

asyncio.run(main())