
class Mammal:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def make_noise(self):
        return "AHHHHHHH"

class Bear(Mammal):
    def make_appearance(self):
        return "ʕ •ᴥ• ʔ"

    def make_noise(self):
        return "ROOAAAR!!"

bear = Bear("bear", "wa")
print(bear.make_appearance())
print(bear.make_noise())



class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        
    def add_topping(self, new_topping):
        self.toppings.append(new_topping)
        
class FancyPizza(Pizza):
    def get_fancy_first_topping(self):
        return f"Fancy {self.toppings[0]}"


hawaiian_pizza = Pizza(["pineapple", "ham"])

try:
    next([].__iter__())
except StopIteration as e:
    raise StopIteration(
        "Code continued to request letters after game should have finished."
        ).with_traceback(e.__traceback__)