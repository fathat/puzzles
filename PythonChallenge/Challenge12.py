## http://www.pythonchallenge.com/pc/return/evil.html
from array import array
blob = array('B')

blob = open('evil2.gfx', 'rb').read()
data1 = ''
data2 = ''
data3 = ''
data4 = ''
data5 = ''


print len(blob)

for i in xrange(0, len(blob), 5):
    data1 += blob[i]
    data2 += blob[i+1]
    data3 += blob[i+2]
    data4 += blob[i+3]
    data5 += blob[i+4]
#    data4.append(blob[i+3])
#    data5.append(blob[i+4])

open('a.jpg', 'wb').write(data1)
open('b.jpg', 'wb').write(data2)
open('c.jpg', 'wb').write(data3)
open('d.jpg', 'wb').write(data4)
open('e.jpg', 'wb').write(data5)