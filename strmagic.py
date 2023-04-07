class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is a {type(self).__name__} who is {self.age} years old"

auberon = Person("Auberon", 27)
print(auberon)