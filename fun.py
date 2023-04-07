# I wanted to find the solution with O(n) time compexity that will work with edge cases 
def pairs_with_given_sum(numbers, target):
    num_dict = {}
    for num in numbers:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    number_of_pairs = 0
    for num in numbers:
        second_num = target - num
        if second_num in num_dict and num_dict[second_num] != 0:
            if num == second_num:
                number_of_pairs += (num_dict[second_num] -1)
            else:
                number_of_pairs += num_dict[second_num]
        num_dict[num] -= 1
    return number_of_pairs

print(pairs_with_given_sum([1, 1], 6))