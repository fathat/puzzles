import problem3
num = 1

def evenly_divisible(x, r):
    for i in xrange(2,r):
        if x % i != 0:
            return False
    return True

if __name__ == '__main__':
    for i in xrange(3, 21):
        print i
        num = 1
        while True:
            if evenly_divisible(num, i):
                print "min", num
                print "factors", problem3.prime_factors(num)
                break
            num += 1
            #if i > 19 and num % 10000 == 0:
                #print "@" + str(num)
