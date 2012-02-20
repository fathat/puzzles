
def range_sum(n):
    return sum([x**2 for x in xrange(1,n+1)])

sum_of_squares = range_sum(100)
square_of_sum = sum(x for x in xrange(1, 100+1))**2

print "sum of squares", sum_of_squares
print "square of sum", square_of_sum

print square_of_sum - sum_of_squares
