
def alg(n):
    i = 1
    while n != 1:
        n = n/2 if n%2==0 else 3*n+1
        i += 1
    return i

def main():
    longest_n = 1
    nlength = 1
    for p in xrange(1,1000000):
        l = alg(p)
        if l > nlength:
            longest_n = p
            nlength = l
    print longest_n, nlength

#for x in alg(13):
#    print x
main()

