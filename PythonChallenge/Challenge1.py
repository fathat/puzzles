## http://www.pythonchallenge.com/pc/def/map.html
from string import maketrans

data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
url = "http://www.pythonchallenge.com/pc/def/map.html"
print ord('m') - ord('k')

in_table = "abcdefghijklmnopqrstuvwxyz"
out_table = "cdefghijklmnopqrstuvwxyzab"

trans = maketrans(in_table, out_table)
print data.translate(trans)
print url.translate(trans)