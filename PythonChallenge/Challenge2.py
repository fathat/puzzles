## http://www.pythonchallenge.com/pc/def/ocr.html
import pprint

mess = open('mess.txt').read()
chars = {}

def count_char(c):
    if chars.has_key(c):
        chars[c] = chars[c] + 1
    else:
        chars[c] = 1


for char in mess:
    count_char(char)
    if char.isalpha():
        print char,


pprint.pprint(chars)
