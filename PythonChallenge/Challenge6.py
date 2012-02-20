## http://www.pythonchallenge.com/pc/def/channel.html

import Image

im = Image.open('channel.bmp')

print dir(im)
w, h = im.size

for y in xrange(h):
    for x in xrange(w):
        r, g, b = im.getpixel((x,y))
        #print help(im.putpixel)
        im.putpixel((x,y), (0, 0, b))
im.save('blue.bmp')
#im.save('channel.bmp')
#print im.split()

#red.save('channel-red.jpg')
#green.save('channel-green.jpg')
#blue.save('channel-blue.jpg')