from collections import Counter

word = input("Please enter a word ")

counts = Counter(word)

tallies = counts.most_common()
best_count = tallies[0][1]

best = set()
for letter, tally in tallies:
    if tally == best_count:
        best.add(letter)
    else:
        break

print(f"The most common letters are {best}")

# to_find = input("What letter are you interested in? ")
# if to_find not in counts:
#     print("That's not in the word!")
# else:
#     print(f"The letter {to_find} shows up {counts[to_find]} times")