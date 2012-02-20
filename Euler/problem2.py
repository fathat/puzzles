
def is_even(x):
    return x%2 == 0

def fib(n):
    sum = 0
    x = 0
    xp = 1

    for i in xrange(0,n):
        #print xp
        yield xp
        last = x
        x = xp
        xp = xp + last
        
def main():
    sum = 0
    for x in fib(80):
        if not is_even(x): continue

        if x > 4000000:
            print "answer", sum
            break
        print "adding", x
        sum += x
        print "sum", sum
main()
#for x in fib(10): print x
