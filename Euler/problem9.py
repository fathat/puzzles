import itertools

def is_py_triplet(a, b, c):
    return (a**2 + b**2) == c**2

possibilities = itertools.combinations(range(1000), 3)

for p in possibilities:
    if is_py_triplet(*p) and sum(p) == 1000:
        print p
        break
