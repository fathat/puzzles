## http://www.pythonchallenge.com/pc/return/bull.html

# a = [1, 11, 21, 1211, 111221, 

def describe(s):
    groups = []
    last_char = ''
    counter = 0
    for x in s:
        if x != last_char and last_char != '':
            #print counter, last_char
            groups.append((counter, last_char))
            counter = 0
        counter += 1
        last_char = x
    groups.append((counter, last_char))
    rval = ''
    for count, char in groups:
        rval += str(count) + char*count
    return rval
    #return groups


current = '1'

for x in xrange(5):
    next = describe(current)
    print next
    current = next

#print describe('1')
#print describe('11')
#print describe('211')
#print describe('1211')
