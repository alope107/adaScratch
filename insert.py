def insertion_sort(array):
    i = 1
    while i < len(array):
        to_insert = array[i]
        insertion_index = i
        # Search in the sorted portion of the array
        # for the correct position to insert array[i]
        while insertion_index > 0 and array[insertion_index-1] > to_insert:
            array[insertion_index] = array[insertion_index-1]
            insertion_index -= 1
            array[insertion_index] = to_insert
        i += 1

my_data = [4, 2, 1, 6, 8, 3, 0, 7, 3]
insertion_sort(my_data)
print(my_data)