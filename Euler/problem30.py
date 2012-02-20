
nums = range(2, 1000000)

def is_blam(n):
    digits = str(n)
    return sum(int(d)**5 for d in digits) == n

def main():
    s = 0
    for n in nums:
        if is_blam(n):
            print n
            s += n
    print s

main()
