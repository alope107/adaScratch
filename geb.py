from collections import deque


def search(theorem, target, rules):
    seen = set()
    queue = deque()
    queue.appendleft(theorem)
    while queue:
        current = queue.pop()
        if current == target:
            return True
        seen.add(current)
        if len(seen) % 100 == 0:
            print(len(seen))
        for rule in rules:
            new_theorems = rule(current)
            for new_theorem in new_theorems:
                queue.appendleft(new_theorem)


def add_u(theorem):
    if theorem[-1] == "I":
        return {theorem + "U"}
    return set()

# Assumes string starts with M and M only occurs once -
# True for our starting axiom but not generally
def double_after_m(theorem):
    return {"M"+(theorem[1:]*2)}

def triple_i_to_u(theorem):
    news = set()
    for i in range(len(theorem)):
        if theorem[i:i+3] == "III":
            news.add(theorem[:i] + "U" + theorem[i+3:])
    return news

def double_u_delete(theorem):
    news = set()
    for i in range(len(theorem)):
        if theorem[i:i+2] == "UU":
            news.add(theorem[:i] + theorem[i+2:])
    return news

assert triple_i_to_u("MIII") == {"MU"}
assert triple_i_to_u("MIIII") == {"MIU", "MUI"}
assert triple_i_to_u("MIUII") == set()
assert triple_i_to_u("MIIUII") == set()

assert double_u_delete("MUU") == {"M"}
assert double_u_delete("MUIU") == set()
assert double_u_delete("MUUIUU") == {"MIUU", "MUUI"}

search("MI", "MU", [add_u, double_after_m, triple_i_to_u, double_u_delete])