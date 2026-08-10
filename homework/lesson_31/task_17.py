# 17. 🧠 Łańcuch zależności
# Stwórz łańcuch zależnych od siebie korutyn:
# 1. pobierz_id_uzytkownika(nazwa_uzytkownika) -> zwraca ID po 1s.
# 2. pobierz_posty(id_uzytkownika) -> zwraca listę ID postów po 1s.
# 3. pobierz_komentarze(id_postu) -> zwraca listę komentarzy po 1s.
# Napisz main, które dla nazwy użytkownika pobierze jego ID, następnie listę jego
# postów, a na końcu pobierze komentarze dla wszystkich jego postów współbieżnie.
# Zmierz czas wykonania.
# (challenge)

import asyncio


async def pobierz_user_id():
    await asyncio.sleep(1)
    return 1


async def pobierz_wpisy(user_id):
    await asyncio.sleep(1)
    return [101, 102, 103]


async def pobierz_komentarze(post_id):
    await asyncio.sleep(1)
    return [
        f'Komentarz 1 do wpisu {post_id}',
        f'Komentarz 2 do wpisu {post_id}',
    ]


async def main():
    user_id = await pobierz_user_id()
    wpisy = await pobierz_wpisy(user_id)

    komentarze = await asyncio.gather(
        *(pobierz_komentarze(post_id) for post_id in wpisy)
    )

    print(f'User ID: {user_id}')
    print(f'Wpisy: {wpisy}')
    print(f'Komentarze: {komentarze}')


asyncio.run(main())
