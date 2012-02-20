## http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib2
import cookielib
cj = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#r = opener.open("http://example.com/")

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s"


def next_nothing(text):
    return text.strip().split()[-1]

text = urllib2.urlopen(link % ('12345', )).read()

for i in xrange(400):
    nn = next_nothing(text)
    req = opener.open(link % (nn, ))
    print req.info().getheaders('Set-Cookie')[0]
    text = req.read()
    print text