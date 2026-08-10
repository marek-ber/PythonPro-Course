# 16. 🧠 Ogranicznik zapytań (Rate Limiter)
# Stwórz klasę RateLimiter z metodą acquire(). Klasa powinna pozwalać na wykonanie
# acquire() tylko n razy na sekundę. Jeśli limit jest przekroczony, acquire() powinno
# asynchronicznie czekać tyle, ile trzeba, by kolejne wywołanie było dozwolone. Przetestuj,
# tworząc 20 zadań, które próbują wywołać acquire() w pętli, z ograniczeniem np. do 5
# zapytań/sekundę.
# (challenge)


import asyncio
from pathlib import Path


KATALOG = Path('pliki_testowe')


def utworz_pliki():
    KATALOG.mkdir(exist_ok=True)

    for i in range(1, 101):
        plik = KATALOG / f'plik_{i}.txt'
        plik.write_text(f'Treść pliku numer {i}', encoding='utf-8')


def odczytaj_plik(sciezka):
    return sciezka.read_text(encoding='utf-8')


async def main():
    utworz_pliki()

    pliki = list(KATALOG.glob('*.txt'))

    wyniki = await asyncio.gather(
        *(asyncio.to_thread(odczytaj_plik, plik) for plik in pliki)
    )

    print(f'Odczytano plików: {len(wyniki)}')


asyncio.run(main())
