
# In reality, these lists are more than 10,000,000 elements long
genome_a = [("pos838", "T"), ("pos99", "G"), ("pos67", "C")]
genome_b = [("pos99", "C"), ("pos67", "C"), ("pos838", "T")]

mutation_sites = []

# for position_a, base_a in genome_a:
#    for position_b, base_b in genome_b:
#        if position_a == position_b and base_a != base_b:
#            mutation_sites.append(position_a)

# print(mutation_sites)

genome_a_dict = {}
#O(n)
for position, base in genome_a: #O(n)
   genome_a_dict[position] = base #O(1)

#O(n^2)
for position, base in genome_b: #O(n)
    if genome_a_dict[position] != base: #O(1)
        # something_else() O(n)
        #mutation_sites.append(position) O(1)

print(mutation_sites)


for i in range(n):
    if some_condition:
        break
    a += 1


# O(n + n^2) = O(n^2)











#O(7 * 1) = O(7) = O(1)

#O(n)
for j in range(n): #O(n)
    #O(1)
    for i in range(7): #O(1)
        a += 1







# O(17) = O(17 * 1) = O(1)


"""
n cities

n *  (n-1) * (n-2) * (n-3) ... 1


1 * 2 * 3 * 4 ... n = n!
"""