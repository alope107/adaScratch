from random import randint, shuffle

from numpy import insert

comp_count = 0

def funkysort(data, comparator):
    global comp_count
    comp_count = 0
    checked = set()


    unchecked_positions = list(range(len(data)-1))

    while unchecked_positions:
        pos = unchecked_positions.pop(randint(0, len(unchecked_positions)-1))
        pair = frozenset((data[pos], data[pos+1]))
        if pair not in checked:
            if comparator(data[pos], data[pos+1]):
                data[pos], data[pos+1] = data[pos+1], data[pos]
                if pos > 0 and (pos-1) not in unchecked_positions:
                    insert_pos = 0 if len(unchecked_positions) == 0 else randint(0, len(unchecked_positions)-1)
                    unchecked_positions.insert(insert_pos, pos-1)
                if pos < len(data)-2 and (pos+1) not in unchecked_positions:
                    insert_pos = 0 if len(unchecked_positions) == 0 else randint(0, len(unchecked_positions)-1)
                    unchecked_positions.insert(insert_pos,pos+1)
        checked.add(pair)
    
    return data

def insertion_sort(data, comparator):
    global comp_count
    comp_count = 0
    for i in range(len(data)):
        for j in range(i, 0, -1):
            if comparator(data[j-1], data[j]):
                data[j-1], data[j] = data[j], data[j-1]
            else:
                break
    return data

def comp(a, b):
    global comp_count
    comp_count += 1
    return a < b

data = list(reversed(list(range(10))))
shuffle(data)

data_copy = data[:]
        
insertion_sort(data, comp)
print("Insertion sort: ", comp_count)
funkysort(data_copy, comp)
print("Funkysort: ", comp_count)