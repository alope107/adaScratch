from datetime import datetime

class Feline:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_by_birth_year(cls, name, birth_year, honorific):
        years_old = datetime.now().year - birth_year
        name = honorific + " " + name
        return cls(name, years_old)

    def __str__(self):
        return f"{self.name}, age: {self.age}"

    def speak(self):
        return f"{self.name} says 'Meow'"

    @staticmethod
    def get_kingdom():
        return "Animalia"

class Lion(Feline):
    endangered = False

    def speak(self):
        return f"{self.name} says 'Roar'"


Lion.endangered = True
print(Lion.endangered)
maru = Lion.create_by_birth_year("Maru", 2000, "Sra.")
print(maru.endangered)
butter = Lion.create_by_birth_year("Butter", 2022, "Jr.")
# print(maru)
print(butter.endangered)
# print(butter.speak())
# omlette = Feline.create_by_birth_year("Omlette", 2014, "Dr.")
# print(omlette)

# kingdom = Feline.get_kingdom()
# print(kingdom)
# tabby = Feline("Tabby", 8)
# felix = Feline("Felix", 1)

# print(tabby)
# print(felix)
# print(tabby.get_kingdom())
# print(felix.speak())