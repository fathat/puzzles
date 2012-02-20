## mozart

import Image

moz = Image.open('mozart.gif').convert('RGB')
res = Image.new('RGB', (640,480))

w, h = moz.size

for y in xrange(h):
    #find pink blotch
    start = 0
    for x in xrange(640):
        pix = moz.getpixel((x,y))

        if pix == (255, 0, 255): 
            start = x
    for x in xrange(start, 640):
        pix = moz.getpixel((x,y))
        res.putpixel((x-start,y), pix)

res.save('aligned.png')