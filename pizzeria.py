class Pizza:
    def __init__(self, diameter, toppings, crust, price, slices=8):
        self.diameter = diameter
        self.toppings = toppings
        self.crust = crust
        self.price = price
        self.slices = slices

    def eat_slices(self, number):
        self.slices -= number

    def print_description(self):
        print(f"My pizza costs ${self.price} dollars and has {self.slices} slices")

class FrozenPizza(Pizza):
    def __init__(self, diameter, toppings, crust, price, slices=8):
        super().__init__(diameter, toppings, crust, price, slices)
        self.defrosted = False

    def defrost(self):
        self.defrosted = True

    def eat_slices(self, number):
        if not self.defrosted:
            raise Exception("Don't break your teeth")
        super().eat_slices(number)

hawaiian_pizza = Pizza(21, ["pineapple", "bacon"], "thin", 9.99, 8)
frozen_veggie = FrozenPizza(10, ["mushroom", "olives"], "stuffed", 5.99, 8)

def add_tomato_and_eat(my_pizza):
    my_pizza.toppings.append("tomato")
    print(my_pizza.toppings)
    my_pizza.eat_slices(1)
    print(my_pizza.slices)
    

add_tomato_and_eat(hawaiian_pizza)
add_tomato_and_eat(frozen_veggie)

# frozen_veggie.eat_slices(5)
# print(frozen_veggie.slices)
# hawaiian_pizza = Pizza(21, ["pineapple", "bacon"], "thin", 9.99, 8)
# veggie_pizza = Pizza(10, ["mushroom", "olives"], "stuffed", 5.99, 8)

# hawaiian_pizza.toppings[0] = 'peach'
# print(hawaiian_pizza.toppings)

# veggie_pizza.eat_slices(4)
# hawaiian_pizza.print_description()
# veggie_pizza.print_description()