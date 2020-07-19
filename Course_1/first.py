
#astr= 'Hello bob'
#try:
    #istr=int(astr)
#except :
    #istr=-1
#print('First',istr)
#............................
#astr='123'
#try:
    #istr=int(astr)
#except :
    #istr=-1
#print('Second',istr)
#......................
#astr='Bob'
#try:
    #print('Hello')
    #isrt=int(astr)
    #print('There')
#except :
    #istr=-1
#print('Done',istr)
#.......................
a=input('Enter Number:   ')
try:
    b=int(a)
except :
    b=-1
if b>0:
    print('Nice Work')
else:
    print('Not a number')
