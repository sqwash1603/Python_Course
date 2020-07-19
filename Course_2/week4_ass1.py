fname =input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word=line.rstrip().split()
    for element in word:
        if element in lst:
            continue
        else:
            x=lst.append(element)

lst.sort()
print(lst)
