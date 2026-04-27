# 4. Asercja w funkcji: Stwórz funkcję oblicz_srednia(lista_ocen) , która zwraca średnią z
# listy. Użyj assert , aby upewnić się, że przekazana lista nie jest pusta.



def oblicz_srednia(lista_ocen):
    assert len(lista_ocen) > 0, "Lista ocen nie może być pusta."
    return sum(lista_ocen) / len(lista_ocen)


print(oblicz_srednia([3, 4, 5]))