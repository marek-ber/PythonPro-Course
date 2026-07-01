from faker import Faker

fake = Faker('pl_PL')

print('Losowe osoby:')
for _ in range(10):
    print(fake.name())

print('\nLosowe zdania:')
for _ in range(10):
    print(fake.sentence())
