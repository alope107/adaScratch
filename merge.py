from random import shuffle
def merge_sort(data):
    if len(data) < 2:
        return data
    
    midpoint = len(data) // 2
    left_sorted = merge_sort(data[:midpoint])
    right_sorted = merge_sort(data[midpoint:])

    full_sorted = []
    i = 0
    j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            full_sorted.append(left_sorted[i])
            i += 1
        else:
            full_sorted.append(right_sorted[j])
            j += 1

    full_sorted.extend(left_sorted[i:])
    full_sorted.extend(right_sorted[j:])

    return full_sorted

assert merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert merge_sort([9, 4, 7, 6, 5, 4, 3, 2, 4]) == [2, 3, 4, 4, 4, 5, 6, 7, 9]
assert merge_sort([1]) == [1]
assert merge_sort([2, 1]) == [1, 2]
assert merge_sort([1, 2]) == [1, 2]
data = [9, 4, 7, 6, 5, 4, 3, 2, 4]
shuffle(data)
assert merge_sort(data) == [2, 3, 4, 4, 4, 5, 6, 7, 9]
print("all tests passed!")