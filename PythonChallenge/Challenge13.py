## http://www.pythonchallenge.com/pc/return/disproportional.html

import Image

directions = ('up', 'down', 'left', 'right')
wire = Image.open('wire.png')
result = Image.new('RGB', (100, 100))


def main():

    i = 0
    x = 50
    y = 50

    left_border = 50
    right_border = 51
    top_border = 50
    bottom_border = 51

    direction = 'down'

    for i in xrange(10000):
        wi = wire.getpixel((i,0))
        print x,y
        result.putpixel((x,y), wi)
        if direction == 'right':
            if x == right_border:
                right_border += 1
                direction = 'up'
            else:
                x += 1
        elif direction == 'down':
           if y == bottom_border:
                bottom_border += 1
                direction = 'right'
           else:
                y += 1
        elif direction == 'left':
           if x == left_border:
                left_border -= 1
                direction = 'down'
           else:
                x -= 1
        elif direction == 'up':
           if y == top_border:
                top_border -= 1
                direction = 'left'
           else:
                y -= 1
    result.save('result.png')

main()