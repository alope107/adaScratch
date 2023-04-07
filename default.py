def say_hello(name="friend"):
    return f"Hello {name}!"

print(say_hello("Coral")) # 1
print(say_hello(name="Dani")) # 2
print(say_hello()) # 3

def average(nums, empty_default=0.0):
    if len(nums) == 0:
        return empty_default
    return sum(nums) / len(nums)

print(average([4, 5, 6])) #1
print(average([])) #2
print(average([], "No average")) #3

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add_item(self, item):
        self.inventory.append(item)
        
rowan = Vendor()
sam = Vendor()

rowan.add_item("ball python")

print(f"Rowan's inventory {rowan.inventory}") #1
print(f"Sam's inventory {sam.inventory}") #2

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add_item(self, item):
        self.inventory.append(item)
        
rowan = Vendor()
sam = Vendor()

rowan.add_item("ball python")

print(f"Rowan's inventory {rowan.inventory}") #1
print(f"Sam's inventory {sam.inventory}") #2