import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the link--> ')

count=input('Enter Count: ')
pos=input('Enter Position: ')
counts=int(count)
position=int(pos)-1
for i in range(counts):
    html=urllib.request.urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    print(tags[position].get('href',None))
    i=i-1
    position=position-1
