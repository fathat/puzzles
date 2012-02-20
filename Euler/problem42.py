
words = [w[1:-1] for w in open('words.txt').read().split(',')]

def triangle_numbers(n):
    s = 0
    for i in xrange(1, n):
        s += i
        yield s
        
triangles = list(triangle_numbers(1000))

def word_value(w):
    return sum(ord(c.upper())-64 for c in w)

x = 0
for word in words:
    wv = word_value(word)
    if wv in triangles:
        x += 1
print triangles
print x
#print word_value('sky')

