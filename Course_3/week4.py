#import urllib.request, urllib.parse, urllib.error
#fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
#for line in fhand:
#    print(line.decode().strip())
#................Example............
#import urllib.request, urllib.parse, urllib.error
#fhand=urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
#...............
#for line in fhand:
#    print(line.decode().strip())#print the file
#.......................
#counts=dict()
#for line in fhand:
    #words=line.decode().split()
    #for word in words:
#        counts[word]= counts.get(word,0)+1
#print(counts)   # count the words of the file
#...................................
#import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
#url=input('Enter - ')
#html=urllib.request.urlopen(url).read()
#soup=BeautifulSoup(html,'html.parser')
#tags=soup('a')#lists the links
#for tag in tags:
#    print(tag.get('href',None))# find out all links
#...........................................
#BeautifulSoup Example........................
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter - ')
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('a')
for tag in tags:
    print(tag.get('herf',None))
