# from math import gcd

# def rotate_list(data, shift_by):
#     if not data:
#         return data
#     denom = gcd(len(data), shift_by)
#     cycle_size = len(data) // denom
#     for i in range(denom):
#         loc = i
#         for _ in range(cycle_size):
#             loc = (loc + shift_by) % len(data)
#             data[i], data[loc] = data[loc], data[i]
#     return data

def rotate_list(data, shift_by):
    if not data:
        return data
    
    shift_by %= len(data)

    swap_pos = 0
    destination = shift_by
    for _ in range(len(data)):
        if destination == swap_pos:
            swap_pos += 1
            destination = (swap_pos + shift_by) % len(data)
            continue
        
        data[swap_pos], data[destination] = data[destination], data[swap_pos]
        destination = (destination + shift_by) % len(data)

    return data

for i in range(-18, 18):
    print(i, rotate_list([1, 2, 3, 4, 5, 6, 7, 8], i))

# print(rotate_list([1, 2, 3, 4, 5, 6, 7, 8], 2))

