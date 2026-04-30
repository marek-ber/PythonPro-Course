# 1. Dziennik użytkownika: Napisz program, który w pętli prosi użytkownika o wpisanie jednej
# linii tekstu. Każda wpisana linia powinna być dopisywana (tryb 'a' ) do pliku
# dziennik.txt . Program kończy działanie, gdy użytkownik wpisze "koniec".

def append_to_file(text: str):

    with open("lesson_9/dziennik.txt", mode="a", encoding="utf-8") as f:
        f.write(f"{text} \n")

while True:
    user_input = input("Podaj tekst: ")

    if user_input == 'koniec':
        break
    else:
        append_to_file(user_input)
