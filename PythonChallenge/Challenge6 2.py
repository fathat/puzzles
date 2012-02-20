## http://www.pythonchallenge.com/pc/def/channel.html
import zipfile

zf = zipfile.ZipFile('channel.zip')

print zf.comment

def parse_next_nothing(text):
    return text.strip().split()[-1]

nn = parse_next_nothing(zf.read('90052.txt'))


for i in xrange(1600):
    name = '%s.txt' % (nn,)
    text = zf.read(name)
    print zf.getinfo(name).comment
    nn = parse_next_nothing(text)

print zf.comment
