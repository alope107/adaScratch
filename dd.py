from heapq import heappush, heappop

def heapsort(unsorted):
    heap = []

    for item in unsorted:
        heappush(heap, item)

    sorted_list = []

    while len(heap) > 0:
        current_min = heappop(heap)
        sorted_list.append(current_min[1])

    return sorted_list

print(heapsort([
    (4, "Eating"), 
    (22, "Watching Love is Blind ss2"), 
    (1, "Bathroom"), 
    (0, "heartbeat"), 
    (8, "Grading PSEs"), 
    (3, "Drinking water")
]))