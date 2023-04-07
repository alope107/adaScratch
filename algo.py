def rotate_list(list, shift_by):
    index = len(list) - (shift_by % 5)
    right_half = list[index:]
    left_half = list[:index]    
    return right_half + left_half

def rotate_list_2(list, shift_by):
    index = len(list) - shift_by
    list[:index], list[index:] = (list[index:], list[:index])
    return list


def shift_list_by_one_elem(list):
  first_elem = list[0]
  for index, ele in enumerate(list):
    if ele != first_elem:
      list[0]=ele
      list[index]=first_elem
      first_elem=ele
    # print(list)
  return list

def move_lists_elements_to_given_number(shift_by):
  for i in range(shift_by):
    return shift_list_by_one_elem(list)

print(rotate_list([1, 2, 3, 4, 5], 13))


def rotate_list(list, shift_by):
    shift_by = shift_by % len(list)
    
    for i in range(shift_by):
        list.insert(0, list.pop())
    return list