# 2. ✏ (Proste) Aiohttp - Strona powitalna: Stwórz prosty serwer aiohttp , który na ścieżce
# / zwróci odpowiedź web.Response z tekstem <h1>Witaj na mojej stronie!</h1> i
# poprawnym content_type='text/html' .



from aiohttp import web

async def home(request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html"
    )


app = web.Application()

app.router.add_get("/", home)

if __name__ == "__main__":
    print("Uruchamiam serwer na [http://127.0.0.1:8080] (http://127.0.0.1:8080)")
    web.run_app(app, host="127.0.0.1", port=8080)