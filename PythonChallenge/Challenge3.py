## http://www.pythonchallenge.com/pc/def/equality.html

import re


bigmess = open('bigmess.txt').read() 

ems = re.findall('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', bigmess)

for m in ems:
    print m

guarded = ''.join(m[4] for m in ems)
print guarded


