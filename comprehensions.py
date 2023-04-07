words = ["from", "swerve", "of", "shore"]

upper_words = []
for word in words:
    upper_words.append(word.upper())

print(upper_words)
words = ["from", "swerve", "of", "shore"]
upper_words = [word.upper() for word in words]
print(upper_words)


words = ["from", "swerve", "of", "shore"]
long_upper_words = [word.upper() for word in words if len(word) > 2]
print(long_upper_words)

words = ["from", "swerve", "of", "shore"]
long_upper_words = []
for word in words:
    if len(word) > 2:
        long_upper_words.append(word.upper())
print(long_upper_words)


words = ["hello", "how", "are", "you"]
flat = [letter for word in words 
               for letter in word]
print(flat)

