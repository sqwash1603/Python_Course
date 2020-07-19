import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Ennter URL:  ')
count=int(input('Count-> '))
position=int(input('Position-> '))
names=[]

while count>0:
    print(('Retriving: ').format(url))
    html = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')
    tag=soup('a')
    name=tag[position-1].string
    names.append(name)
    url = tag[position-1]['href']
    count=count-1
print(names[-1])
