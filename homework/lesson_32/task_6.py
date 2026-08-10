# 6. ✏ (Proste) Aiohttp - Odczyt JSON (echo): Stwórz handler POST na ścieżce /api/echo .
# Handler ma odczytać dane JSON wysłane w ciele ( await request.json() ) i odesłać je z
# powrotem w odpowiedzi web.json_response .

from aiohttp import web

async def echo(request):
    data = await request.json()
    return web.json_response(data)

app = web.Application()

app.router.add_post("/api/echo", echo)


if __name__ == "__main__":
    print("Uruchamiam serwer na [http://127.0.0.1:8080] (http://127.0.0.1:8080)")
    web.run_app(app, host="127.0.0.1", port=8080)