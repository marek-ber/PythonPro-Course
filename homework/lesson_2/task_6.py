# 6. Wyrażenie logiczne: Napisz program, który pyta, czy użytkownik ma prawo jazdy
# ( tak/nie ) i ile ma lat. Wyświetl True , jeśli użytkownik ma 18 lat lub więcej ORAZ ma
# prawo jazdy. W przeciwnym razie wyświetl False.

prawo_jazdy = input("Posiada prawo jazdy (tak / nie): ")
wiek = int(input("Podaj wiek: "))


print(wiek >= 18 and prawo_jazdy == "tak")
