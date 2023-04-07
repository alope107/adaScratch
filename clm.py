from datetime import datetime

class Cat:
    def __init__(self, age):
        self.age = age
    
    def speak(self):
        return "Meow"

    @classmethod
    def create_from_birth_year(cls, birth_year):
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(age)

class Lion(Cat):
    def speak(self):
        return "Roar"

omlette = Cat.create_from_birth_year(1909)
simba = Lion.create_from_birth_year(1994)

print(omlette.speak())
print(simba.speak())