# 8. Łączenie map i filter: Mając listę liczb [-5, 2, 8, -1, 0, 10] , użyj filter do
# wybrania tylko liczb dodatnich, a następnie map do obliczenia ich kwadratów. Zrób to w
# jednej linijce.

numbers = [-5, 2, 8, -1, 0, 10]

result = list(map(lambda x: x**2, filter(lambda x: x > 0, numbers)))

print(result)