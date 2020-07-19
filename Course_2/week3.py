#fhand=open('s.txt')
#print(fhand)
#Output----><_io.TextIOWrapper name='s.txt' mode='r' encoding='cp1252'>
#New line
#s='Hello\nworld'
#print(s)
#.........File Processing....
#x=open('s.txt')#Input Hello!!!!1
#for c in x:
#    print(c)
#Output---> Hello!!!!!!!!!!!1111...
#  Counting ines in file........
#f=open('s.txt')
#count=0
#for x in f:
#    count=count+1
#print('Line count: ',count)
#Output---> 6
#reading the whole file.......
#x=open('s.txt')
#i=x.read()
#print(len(i))
#print(i[:50])
#.................................
#searching through a file.......
#f=open('s.txt')
#for line in f:
#    line=line.rstrip()
#    if line.startswith('I '):
#        print(line)
#..........Skipped and Continue.............................
#f=open('s.txt')
#for line in f:
#    line=line.rstrip()
#    if not line.startswith('I '):
#        continue
#print(line)

#.................Prompt For Filr Name........
#fname=input('Enter the file name: ')
#fhand=open(fname)
#count=0
#for line in fhand:
#    if line.startswith('I'):
#        count=count+1
#print('There were',count,'I lines in',fname)
#......................................
#fname=input('Enter the file name: ')
#try:
#    fhand=open(fname)
#except :
#    print('Not Found')
#    quit()

#count=0
#for line in fhand:
#    if line.startswith('I'):
#        count=count+1
#print('There were',count,'I lines in',fname)
