import math

def factors(n):
    for i in xrange(1,n):
        if n % i == 0:
            yield i

def factor_count(n):
    fc = 0
    sqr = int(math.sqrt(n))

    for i in xrange(1, sqr):
        if n % i == 0:
            fc += 2
    if sqr * sqr == n:
        fc += 1
    return fc

def triangle_numbers():
    i = 1
    s = 0
    while True:
        s += i
        yield s
        i += 1

#for x in zip(triangle_numbers(), xrange(9)):
#    print x

def main():

    for n in triangle_numbers():
        if factor_count(n) > 500:
            print n
            break
main()
