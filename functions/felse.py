user_tater = input("Name a type of potato: ")
taters = ["russet", "kennebec", "yukon gold"]
for tater in taters:
    if user_tater == tater or \
        4 == 5:
        # Found it!
        print("I have one of those!")
        break
else:
    # Didn't find anything..
    print("Sorry, I don't have that")