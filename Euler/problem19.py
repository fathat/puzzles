import datetime

counter = 0
for y in xrange(1901, 2001):
    for m in xrange(1, 13):
        dt = datetime.datetime(y, m, 1).weekday()
        if dt == 6:
            counter += 1

print counter
