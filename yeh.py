def some_func(n):
    total = 0
    #O(1 * 1) = O(1)
    for i in range(8): #O(1)
        for j in range(22): #O(1)
            total += 1
    return total

print(some_func(22))

resp = {
    "task": {
        "id" : task.task_id,
        "title": task.title,
        "description": task.description,
        "is_complete":False
    }
}