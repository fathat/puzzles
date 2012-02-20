
def is_palindrome(s):
    i = 0
    j = len(s)-1
    while i<=j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

for i in xrange(900, 1000):
    for j in xrange(900, 1000):
        s = str(i * j)
        if is_palindrome(s):
            print s
