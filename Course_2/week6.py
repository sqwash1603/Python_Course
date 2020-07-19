x=('A','B','C','D','E')
print(x)
for y in x:
    print(y)
(a,b,s)=('X','Y','Z')
print(a,s)


c={'a':10,'b':1,'c':22}
tmp=list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp=sorted(tmp,reverse=True)
print(tmp)


file=open('mbox-short.txt')
counts=dict()
for line in file:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
lst=list()
for k,v in counts.items():
    newtup=(v,k)
    lst.append()
lst=sorted(lst,reverse=True)
for v,k in lst[:10]:
    print(k,v)
