# # 6. Wielokrotne powitanie: Napisz funkcję wielokrotne_powitanie(imie: str, ilosc:
# # int) -> None , która wyświetla powitanie f"Cześć, {imie}!" tyle razy, ile wynosi
# # ilosc . Ta funkcja nie powinna niczego zwracać.

def multiple_greetings(name: str, number: int) -> None:
    for i in range(number):
        print(f"Cześć {name}!")
    return None

print(multiple_greetings("Marek", 6))