# 9. 🧠 Pobieranie statusów HTTP
# Napisz program, który przyjmuje listę adresów URL i współbieżnie sprawdza status HTTP
# każdego z nich. Użyj biblioteki aiohttp. Wskazówka: musisz ją zainstalować (pip install
# aiohttp) i użyć aiohttp.ClientSession. Dla każdego URL wypisz jego status (np.
# "https://google.com - Status: 200").
# (challenge)



import asyncio
import httpx


async def pobierz_status(client, url):
    try:
        response = await client.get(url)
        return url, response.status_code
    except httpx.RequestError:
        return url, 'Błąd połączenia'


async def main():
    urls = [
        'https://www.google.com',
        'https://www.python.org',
        'https://www.github.com',
    ]

    async with httpx.AsyncClient(timeout=10.0) as client:
        wyniki = await asyncio.gather(
            *(pobierz_status(client, url) for url in urls)
        )

    for url, status in wyniki:
        print(f'{url}: {status}')


asyncio.run(main())
