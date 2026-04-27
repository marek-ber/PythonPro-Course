# 3. Czytanie pliku: Napisz funkcję, która próbuje otworzyć i odczytać plik o podanej nazwie.
# Obsłuż wyjątki FileNotFoundError (gdy pliku nie ma) oraz PermissionError (gdy nie
# ma uprawnień do odczytu).

try:
    file = open("/home/marek/Pulpit/PythonPro-Course/lesson_8/data.txt", mode= "r")
    
except FileNotFoundError as error:
    print(f"Plik nie istnieje {error}")
except PermissionError as error:
    print(f"Brak dostepu do pliku {error}")


file_data = file.readlines()
print(file_data)

file_2 = open("/home/marek/Pulpit/PythonPro-Course/lesson_8/data2.txt", mode= "w")

my_name = "Marek B"

file_2.write(my_name)