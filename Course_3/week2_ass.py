import re
handle = open('regex_sum_684864.txt')
numbers = 0
for line in handle:
    line = line.rstrip()
    numbers = numbers + sum(map(lambda x: int(x), re.findall('([0-9]+)', line)))
print(numbers)
