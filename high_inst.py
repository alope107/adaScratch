class Item:
    def __init__(self, condition):
        self.condition = condition

    def get_condition(self):
        return f"my condition is {self.condition}"

def print_3_times(method):
    for _ in range(3):
        print(method())

def print_3_times_with_instance(instance, method):
    for _ in range(3):
        print(method(instance))

trading_card = Item("mint")

# Option 1: use bound method
print_3_times(trading_card.get_condition)
print()
# Option 2: use method from class and manually insert self
print_3_times_with_instance(trading_card, Item.get_condition)

'''
Running this program outputs:
my condition is mint
my condition is mint
my condition is mint

my condition is mint
my condition is mint
my condition is mint
'''