def kth_missing(numbers, k):
    for i in numbers:
        if i>k:
            return k
        else:
            k+=1
    return k

print(kth_missing([1, 2, 3, 4, 5, 6, 7, 8, 10], 2))