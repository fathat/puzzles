import urllib,re,bz2
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
seed="12345"
info=''
while True:
    req=urllib.urlopen(url+seed)
    text=req.read()
    seed=''.join(re.findall(r"busynothing is (\d+)",text))
    cookies=req.info().getheaders('Set-Cookie')[0]
    byte=cookies.split(';')[0].split('=')[1]
    info+=byte
    try :
        int(seed)
        print "   Info:",byte,"t   Next:",seed
    except :
        print "   Info:",byte,"t   Last:",text
        break
print "info:",bz2.decompress(urllib.unquote_plus(info))