# an example function that returns a temperature converted to fahrenheit 
# for numeric arguments and returns None for non-numeric arguments.
def convert_to_fahrenheit(temp):
    return 9/5*temp+32


temp_f = convert_to_fahrenheit(0)

if temp_f < 60:
    print("That's too cold!")
else:
    print("That's a nice temp!")






# an example function that returns a value
# def greeting():
#     return "Hello"

# hi = greeting()
# greeting_len = len(hi)
# print(f"Our greeting has {greeting_len} characters")