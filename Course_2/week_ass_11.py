name =input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

email = dict()
for line in handle:
    if not line.startswith('From '): continue
    line = line.split()
    for word in line:
        if word != line[1]: continue
        email[word] = email.get(word, 0) + 1

bigvalue = None
bigkey = None
for key, value in email.items():
    if bigvalue is None or value > bigvalue:
        bigvalue = value
        bigkey = key

print(bigkey, bigvalue)
