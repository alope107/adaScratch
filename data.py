from datetime import datetime

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.birth_year = datetime.now().year
        self.birth_month = datetime.now().month


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name, species="canis")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "felis")

tabby = Cat("Tabby")
fitz = Dog("Fitz")
rufus = Dog("Rufus")

# print(fitz.name)
# print(rufus.name)

print(tabby.name, tabby.species, tabby.birth_year, tabby.birth_month)

buddy = Animal("Buddy", "lizard")
print(buddy.name, buddy.species, buddy.birth_year, buddy.birth_month)