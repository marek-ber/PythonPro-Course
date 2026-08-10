# 13. 🧠 **Prosty serwer echa:** Napisz serwer TCP na `localhost:8888` za pomocą `asyncio.start_server()`.

import asyncio


async def obsluz_klienta(reader, writer):
    adres = writer.get_extra_info('peername')
    print(f'Połączono: {adres}')

    while True:
        dane = await reader.read(100)

        if not dane:
            break

        wiadomosc = dane.decode()
        print(f'Odebrano: {wiadomosc}')

        writer.write(dane)
        await writer.drain()

    writer.close()
    await writer.wait_closed()
    print(f'Rozłączono: {adres}')


async def main():
    server = await asyncio.start_server(
        obsluz_klienta,
        '127.0.0.1',
        8888,
    )

    print('Serwer działa na localhost:8888')

    async with server:
        await server.serve_forever()


asyncio.run(main())
