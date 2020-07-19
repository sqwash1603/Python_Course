fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except :
    print('Not Found')
    quit()

count=0
for line in fhand:
    if line.startswith('I'):
        count=count+1
print('There were',count,'I lines in',fname)
