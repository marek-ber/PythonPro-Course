# 10. 🧠 Zadanie 10 – Eksploracja MRO
# Stwórz następującą, złożoną hierarchię dziedziczenia:
# class A
# class B(A)
# class C(A)
# class D(B)
# class E(C)
# class F(D, E) Narysuj schemat tej hierarchii w mermaid. Następnie, nie uruchamiając
# kodu, spróbuj przewidzieć, jakie będzie MRO dla klasy F. Na koniec sprawdź swoją
# odpowiedź, używając print(F.mro()). (challenge)

class A:
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        super().__init__()

class C(A):
    def __init__(self):
        super().__init__()

class D(B):
    def __init__(self):
        super().__init__()

class E(C):
    def __init__(self):
        super().__init__()

class F(D, E):
    def __init__(self):
        super().__init__()

print(F.mro())