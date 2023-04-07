def multiply_2(num):
    return num * 2

def multiply_3(num):
    return num * 3


a = multiply_2
b = multiply_3
x = 2
x = a(x)
x = b(x)
x = a(x)
print(x)


def wrapper(y,z):
	return y * z

c = wrapper
print(f"The answer is {c(a(3), b(4))}")

a = True
b = False
c = False
  
if a or b and not c:
    print("A or B and not C")
else:
    print("not A or B and C")



# O(n) n = num_reps
def repeat_multiple_times(value, num_of_repetitions):
    for count in range(num_of_repetitions):
        print("The value is", value)







# O(77) = O(1)
repeat_multiple_times(5, 77)



def greet_friends(input_list):
    count = len(input_list)
    finished = False
    while not finished: #O(1)
        for j in range(count): #O(n)
            print(f"Hello, Friend!")
        finished = True

# O(1 * n) = O(n)



def greet_friends(input_list):
    count = len(input_list)
    i = 0
    while i < count: #O(n)
        for j in range(count): #O(n)
            print(f"Hello, Friend #{i+1} in {j+1}!")
        i += 1

#O(n * n) = O(n^2)




def greet_friends(input_list):
    count = len(input_list)
    k = 0
    while k != count: #O(n)
        i = 0
        while i < count: #O(n)
            for j in range(count): #O(n)
                print(f"Hello, Friend #{i+1} in #{j+1}!")
            i += 1
        k += 1

#O(n*n*n) = O(n^3)





# Multiply nested loops O(17*n) =O(n) n=len(input)





def does_value_exist(input_list, value):
    for item in input_list: #O(n) n = len(input_list)
        if item == value: #O(m) m = len(item)
            return True
    return False

(1, 2, 3, 4, 5, 6, 7)
(1, 2, 3, 4, 5, 6, 99)
# len(item) = 8
# m = 8
# O(n * m) = O(n * 8) = O(n)









x = 2
while x < 77:
    x = x * x

'''

x   16
y   55
z   444
'''












