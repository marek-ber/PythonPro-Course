# 5. Iloczyn elementów: Użyj funkcji reduce() , aby obliczyć iloczyn (wynik mnożenia)
# wszystkich liczb w liście [1, 2, 3, 4, 5] .

numbers = [1, 2, 3, 4, 5]

from functools import reduce

multiplication = reduce(lambda x, y: x * y, numbers)

print(multiplication)