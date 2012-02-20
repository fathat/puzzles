## http://www.pythonchallenge.com/pc/def/peak.html

import pickle
from pprint import pprint

data = pickle.load(open('banner.p'))

def analyze():
    for thing in data:
        #print len(thing)
        print ', '.join(str(number) for symbol, number in thing)
        print sum(number for symbol, number in thing)
        

for row in data:
    rowdata = ''
    for symbol, repeat in row:
        rowdata += symbol*repeat
    print rowdata


#    for symbol, letter in thing:
#        print chr(letter)

#pprint(data)