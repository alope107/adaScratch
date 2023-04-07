from heapq import heappush, heappop

# Time: nlogn
# Space: n
def heapsort(unsorted):
    heap = []

    for item in unsorted:
        heappush(heap, item)

    ordered = []

    while len(heap) > 0:
        value = heappop(heap)
        ordered.append(value[1])

    return ordered

print(heapsort([
    (4, "rhubarb"),
    (4, "crying"),
    (4, "screaming"),
    (7, "carrots"),
    (1, "sleep"),
    (33, "Asking hot person out"),
    (0, "hydration"),
    (-8, "Mental Health")
]))

    