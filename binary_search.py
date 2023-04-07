# # names = [('arjun', 88), ('auberon', 23), ('damien', 7), ('elora', 92), ('hallie', 31), ('sam', 10), ('xinting', 42)]
# # print(sorted(names, key=lambda x: x[1]))
# # def find_name(sorted_names, my_name):
# #     lower = 0
# #     upper = len(sorted_names) - 1

# #     while upper >= lower:
# #         mid = lower + ((upper - lower) // 2)
# #         current_name = sorted_names[mid]

# #         if current_name == my_name:
# #             return mid
# #         if my_name < current_name:
# #             upper = mid - 1
# #         else:
# #             lower = mid + 1

# #     raise ValueError(f"{my_name} not found in list")

# # names = ['arjun', 'auberon', 'damien', 'elora', 'hallie', 'sam', 'xinting']
# # to_find = 'hallie'
# # index = find_name(names, to_find)
# # print(f"{to_find} is at index {index} in the list!")

# # def ask_user(n):
# #     while True:
# #         resp = input(f"Press 'h' if your number is higher than {n}, 'e' if it is equal and 'l' if it is lower \n")
# #         resp = resp.lower()
# #         if resp == 'h':
# #             return 'higher'
# #         if resp == 'e':
# #             return 'equal'
# #         if resp == 'l':
# #             return 'lower'
# #         print("Invalid input.")

# # def find_num(lower, upper):
# #     q_count = 1

# #     while True:
# #         print(f"Question #{q_count}")
# #         mid = lower + ((upper - lower) // 2)
# #         result = ask_user(mid)

# #         if result == 'equal':
# #             return (mid, q_count)
# #         if result == 'higher':
# #             lower = mid + 1
# #         elif result == 'lower':
# #             upper = mid - 1

# #         q_count += 1

# #         if upper < lower:
# #             raise ValueError("Player is a dirty liar")


# # def find_num(lower, upper):
# #     while True:
# #         mid = lower + ((upper - lower) // 2)

# #         # Asks user whether the midpoint is higher, lower or equal 
# #         # to their number
# #         result = ask_user(mid)

# #         if result == 'equal':
# #             return mid 
# #         if result == 'higher':
# #             lower = mid + 1
# #         elif result == 'lower':
# #             upper = mid - 1

# #         if upper < lower:
# #             raise ValueError("Player is a dirty liar")


# # result, q_count = find_num(1, 1000000)
# # print(f"Your number is {result}!") 
# # print(f"It took me {q_count} question{'s' if q_count > 1 else ''} to find it!")


# def find_place(sorted_names, my_name):
#   lower = 0
#   upper = len(sorted_names) - 1

#   while upper >= lower:
#       mid = lower + ((upper - lower) // 2)
#       current_name = sorted_names[mid]

#       if current_name == my_name:
#           return mid
#       if my_name < current_name:
#           upper = mid - 1
#       else:
#           lower = mid + 1
  
#   return upper + 1

# names = ['arjun', 'auberon', 'damien', 'elora', 'sam', 'xinting']
# to_place = 'hallie'
# index = find_place(names, to_place)
# print(f"{to_place} will be #{index+1} to get food")

def get_higher_or_lower(n):
   while True:
       resp = input(f"Press 'h' if your number is higher than {n}, 'e' if it is equal and 'l' if it is lower \n")
       resp = resp.lower()
       if resp == 'h':
           return 'higher'
       if resp == 'e':
           return 'equal'
       if resp == 'l':
           return 'lower'
       print("Invalid input.")

def find_num(bounds=(1, 1000000)):
   lower, upper = bounds
   q_count = 1

   while True:
       if upper < lower:
           raise ValueError("Player is a dirty liar")

       print(f"Question #{q_count}")
       mid = lower + ((upper - lower) // 2)
       result = get_higher_or_lower(mid)

       if result == 'equal':
           return (mid, q_count)
       if result == 'higher':
           lower = mid + 1
       elif result == 'lower':
           upper = mid - 1

       q_count += 1


result, q_count = find_num()
print(f"Your number is {result}!")
print(f"It took me {q_count} question{'s' if q_count > 1 else ''} to find it!")
  

