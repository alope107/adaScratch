import random

RANGE_LOW = 0
RANGE_HIGH = 100
# pick a random number
random_number = random.randint(RANGE_LOW, RANGE_HIGH)

def guess_the_number():

    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")

    if user_input is None:
        # do something
        # maybe ask another number?

    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print(f"Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    elif user_input == random_number:
        print("You guessed the number!  Good job!")
    elif user_input > random_number:
        print("Your guess is too high")
    elif user_input < random_number:
        print("Your guess is too low")

# Run the guess_the_number function to test it
guess_the_number()



def calculate_subtotal(item_prices):
    total = 0
    for price in item_prices:
        total += price
    return float(total)

def calculate_sales_tax(total, sales_tax_rate=.08):
    sales_tax_total = total * sales_tax_rate
    return float(sales_tax_total)