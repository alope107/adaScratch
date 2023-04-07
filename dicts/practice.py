favorite_foods = {
    "Elaine" : ["lumpia", "sushi"],
    "Sujin" : ["kimchi", "popcorn"]
}

favorite_foods["Fena"] = ["pizza", "ice cream", "pho"]

# new_person = input("Who is the person? ")
# new_food = input("What's their favorite food? ")

# favorite_foods[new_person] = new_food

# print(favorite_foods)
person = input("Who is the person you're interested in? ")

if person in favorite_foods:
    foods = favorite_foods[person]
    print(f"{person} has {len(foods)} favorite foods")
    print("They are: ")
    for food in foods:
        print(food)
else:
    print(f"{person} is not in my dict")

# favorite_foods["Sujin"] = "popcorn"

# # food = favorite_foods[person]
# print(f"The favorite food of {person} is {favorite_foods['Sujin']}")
