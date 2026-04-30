class Animal:
    description = "Some kind of animal"

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_hello(self):
        return "Hello"
    
    def introduce_youself(self):
        return f"Mam na imię {self.name}"
    def change_animal_name(self, new_name):
        self.name = new_name

    def show_age(self):
        return self.__age

dog = Animal("Azor", 10)

cat = Animal("Mruczek", 11)

print(dog.name)

# dog.name = "Burek"

dog.change_animal_name("Reksio")

print(dog.name)

print(dog.__age)

# print(dog.name)
# print(cat.name)

# print(dog.description)
# print(cat.description)

# print(dog.introduce_youself())
# print(cat.introduce_youself())


# my_list = [1, 2, 3]

# my_list.append(4)

# class MyList:
#     def __init__(self, values):
#         self.values = values

#     def append_to_values(self, number):
#         self.values.append(number)
        
# my_list = MyList([1, 2])

# print(my_list.values)

# my_list.append_to_values(3)

# print(my_list.values)
