#hand=open('mbox-short.txt')
#for line in hand:
    #line=line.rstrip()
    #if line.find('From: ')>=0:
        #print(line)


#import re
#x='My 2 favourite numbers are 11 and 38'
#y=re.findall('[0-9]+',x)
#print(y)
#y=re.findall('[AEIOU]+',x)
#print(y)

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
y=re.findall('^F.+?:',x)
print(y)
