word = "helooolooololol"
starting_pos = 0
while starting_pos >= 0:
    starting_pos = word.find("l", starting_pos)
    print(starting_pos)
    if starting_pos == -1:
            break
    starting_pos += 1