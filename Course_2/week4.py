a=[1,2,3,4]
b=[5,6,7,8]
c=a+b
print(c)


w=[3,4,6,3,2,57,75,3]
print(w[2:5])
s=list()
s.append('book')
s.append(99)
s.append('cookie')
print(s)


f=['Ira','Nira','Mira']
f.sort()
print(f)
print(len(f))
print(max(f))
print(min(f))



#total=0
#count=0
#while True:
#    inp=input('Enter a number:  ')
#    if inp=='Done':
#        break
#        value=float(inp)
#        total=total+value
#        count=count+1
#average=total/count
#print('Average: ',average)


abc='With three words'
stuff=abc.split()
print(stuff)
print(len(stuff))


fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('X'):
        continue
x=line.split()
print(x)


h = list(range(5))
print(h)



friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])


#fruit = 'Banana'
#fruit[0] = 'b'
#print(fruit)



t = [9, 41, 12, 3, 74, 15]
print(t[2:4])
