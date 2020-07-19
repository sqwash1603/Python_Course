fname=input('Enter File Name: ')
if len(fname)<1:
    fname='mbox-short.txt'
hand=open(fname)
d=dict()
for line in hand:
    
    #line=line.rstrip()
    #print(line)
    wds=line.split()
    #print(wds)
    for w in wds:
        #print('*****',w,d.get(w,-99))
        #oldcount=d.get(w,0)
        #print(w,'old',oldcount)
        #newcount=oldcount+1
        #d[w]=newcount

        d[w]=d.get(w,0)+1
        #print(w,'New',d[w])


        #print(w)
        #if w in d:
        #    d[w]=d[w]+1
            #print("***Existing***")
        #else:
        #    d[w]=1
            #print('******NEW******')
        #print(w,d[w])
#print(d)

#Most common word..........
largest=-1
theword=None
for k,v in d.items():
    #print(k,v)
    if v>largest:
        largest=v
        theword=w
print(theword,largest)
