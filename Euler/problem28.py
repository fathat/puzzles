dim = 1001
spiral = range(1, dim*dim+1)

def numbers():
    i = 0
    d = 2
    diagonal = []
    r = 0
    while i<dim*dim:
        diagonal.append(spiral[i])
        if r == 4:
            d += 2
            r = 0
        i += d
        r += 1
    return diagonal


print sum(numbers())


