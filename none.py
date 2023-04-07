a = "Hello"
b = "Hell" + "o"
c = "Hell"
c += "o"

print(f"{a=} {b=} {c=}")
print(f"{(a == b) =}")
print(f"{(a == c) =}")
print(f"{(a is b) =}")
print(f"{(a is c) =}")

x = 123456789123456789
y = 123456789123456788
y += 1

print(f"{x=} {y=}")
print(f"{(x == y) =}")
print(f"{x is y =}")