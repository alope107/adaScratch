class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person("Jim-Bob", 4),
    Person("Gudetama", 8),
    Person("Auberon", 28),
    Person("Keropi", 34),
    Person("Damien", 36),
    Person("Esmerelda", 92),
    Person("Skeleton", 234)
]

to_find = Person("Jane", 50)

def find_position(people, to_insert):
    # for i in range(len(people)):
    #     person = people[i]
    #     if to_insert.age < person.age:
    #         return i
    # return len(people)

    # Start with lower at 0, upper at end of list
    # Check the middle
    # If middle is younger than to_insert, lower bound adjusts
    # If middle is older than to_insert, upper bound adjusts
    # If middle == to_insert age, return middle index
    # If upper and lower ever cross over, we need upper + 1
    lower = 0
    upper = len(people) - 1
    while lower <= upper:
        # lower = 10 upper = 20
        # upper - lower = 10
        # (upper - lower) // 2 = 5
        # (upper - lower) // 2 + lower = 15
        mid = (upper - lower) // 2 + lower # (upper + lower) // 2
        # print("Checking: ", mid)
        person = people[mid]
        if to_insert.age == person.age:
            return mid
        if to_insert.age < person.age:
            upper = mid - 1
        else:
            lower = mid + 1
    return upper + 1
        

print(find_position(people, to_find))
print(find_position(people, Person("Baby", 1)))
print(find_position(people, Person("Dino", 100000000)))
