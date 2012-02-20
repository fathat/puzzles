## http://www.pythonchallenge.com/pc/return/5808.html

import Image

img = Image.open('cave.jpg')
w, h = img.size

result = Image.new('RGB', (w/2, h/2))

for y in xrange(1, h, 2):
    for x in xrange(1, w, 2):
        pixel = img.getpixel((x,y))
        result.putpixel((x/2, y/2), pixel)

result.save('even.bmp')

