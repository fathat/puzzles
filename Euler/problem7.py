
def sieve(n):
    p = 2
    primes = [p]
    marked = [False]*n
    x = p
    while True:
        x = p
        while x < n:
            marked[x] = True    
            x += p
        x = p+1
        while x< n:
            if not marked[x]:
                p = x
                primes.append(p)
                break
            x += 1
        if x == n:
            break
    return primes

def main():
    primes = sieve(1000000)
    print primes[10000]
    print len(primes)

if __name__ == '__main__':
    main()
