def my_max(data, key_function):
    highest_data = None
    highest_value = None

    for datum in data:
        value = key_function(datum)
        if highest_value is None or value > highest_value:
            highest_data = datum
            highest_value = value
        
    return highest_data

print(my_max(["cheese", "chocolate", "candy"], len))