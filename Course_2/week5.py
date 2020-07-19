purse=dict()
purse['money']=12
purse['candy']=3
purse['tissue']=75
print(purse)
purse['money']=purse['money']+8
print(purse)
print(len(purse))
print(max(purse))
#.......Counting with dictionaries..................
c=dict()
names=['A','B','A','C','B']
for name in names:
    c[name]=c.get(name,0)+1
print(c)
print(list(c))
print(c.keys())
print(c.items())

#dictionaries with files..............................

counts=dict()
print('Enter a line of text: ')
line=input(' ')
words=line.split()
print('Words:',words)
print('Counting.......')
for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts..',counts)




n=input('File: ')
h=open(n)

x=dict()
for l in h:
    #w=x.split()
    for ww in w:
        x[ww]=x.get(ww,0)+1
bigcount=None
bigword=None
for ww,y in x.items():
    if bigcount is None or y>bigcount :
        bigword=ww
        bigcount=y
print(bigword,bigcount)
