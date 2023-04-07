word = input("Please enter a word ")

counts = dict()

for letter in word:
    if letter not in counts:
        counts[letter] = 1
    else:
        counts[letter] += 1
        

to_find = input("What letter are you interested in? ")
if to_find not in counts:
    print("That's not in the word!")
else:
    print(f"The letter {to_find} shows up {counts[to_find]} times")