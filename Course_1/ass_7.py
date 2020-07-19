#num=0
#tot=0.0
#while True:
#    sval=input('Enter a number: ')
#    if  sval=='done':
#        break
#    try:
#        fval=float(sval)
#    except:
#        print('Invalid Input')
#        continue
#    num = num+1
#    tot=tot+fval
#print(tot,num,tot/num)
#................................

num = 0
largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        numb = int(num)
    except :
        print('Invalid input')
    if smallest is None :
        smallest = numb
    elif numb<smallest:
        smallest=numb
    elif numb>largest :
        largest = numb

print("Maximum is", largest)
print("Minimum is", smallest)
