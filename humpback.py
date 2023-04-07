from datetime import datetime

    # @classmethod
    # def create_without_age(cls, name):
    #     return cls(name, 0)

class Feline:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_by_birth_year(cls, name, birth_year, honorific):
        years_old = datetime.now().year - birth_year
        name = honorific + " " + name
        return cls(name, years_old)

    # @classmethod
    # def create_without_age(cls, name):
    #     return cls(name, 0)

    def __str__(self):
        return f"{self.name}, age: {self.age}"

    def speak(self):
        return f"{self.name} says 'Meow'"

    @staticmethod
    def get_kingdom():
        return "Animalia"

class Lion(Feline):
    def speak(self):
        return f"{self.name} says 'Roar!'"

butter = Lion.create_by_birth_year("Butter", 1984, "Dr.")
print(butter)
print(butter.speak())
# pete = Feline.create_by_birth_year("Pete", 2016, "Sr.")
# print(pete)

# tabby = Feline("Tabby", 8)
# print(tabby.speak())

# kingdom = Feline.get_kingdom()
# cat_sound = Feline.speak()
# print(cat_sound)
# tabby = Feline("Tabby", 8)
# maru = Feline("Maru", 12)

# print(tabby)
# print(maru)
# print(tabby.speak())