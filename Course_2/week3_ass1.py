fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except :
    print('Not Found')
    quit()

for line in fhand:
    x=line.rstrip()
    print(x.upper())
