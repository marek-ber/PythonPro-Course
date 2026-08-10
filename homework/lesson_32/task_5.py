# 5. ✏ (Proste) Aiohttp - Odczyt query params: Stwórz handler /api/search , który odczyta
# z request.query parametr q . Jeśli parametr istnieje, zwróć JSON {"szukana_fraza":
# "wartosc_q"} . Jeśli nie, zwróć {"błąd": "Brak parametru q"} .

from aiohttp import web

async def parametr(request):
    q = request.query.get('q')

    if q:
        return web.json_response({"szukana_fraza": q})
    
    return web.json_response({"błąd": "Brak parametru q"})

app = web.Application()

app.router.add_get("/api/search", parametr)


if __name__ == "__main__":
    print("Uruchamiam serwer na [http://127.0.0.1:8080] (http://127.0.0.1:8080)")
    web.run_app(app, host="127.0.0.1", port=8080)