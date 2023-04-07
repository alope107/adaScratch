import numpy as np

a  = np.array([5, None, 7])

print(f"{(a == None)=}")
print(f"{(a is None)=}")

if a == None:
    print("yay")