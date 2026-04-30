# 8. Wyszukiwarka logów: Wyobraź sobie, że masz duży plik log.txt . Napisz program, który
# pyta użytkownika o szukane słowo (np. "ERROR") i zapisuje wszystkie linie zawierające to
# słowo do nowego pliku wyniki_wyszukiwania.txt .

looking_for = input("Podaj słowo do wyszukania: ")

with open("/home/marek-berny/Pulpit/LearnIT/lesson_9/log.txt", "r", encoding="utf-8") as file:
    with open("wyniki_wyszukiwania.txt", "w", encoding="utf-8") as result:
        for i in file:
            if looking_for in i:
                result.write(i)