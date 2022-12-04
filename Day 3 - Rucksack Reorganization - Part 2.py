import os
import math
import string

input_file = open("Day 3 - Rucksack Reorganization.txt", "r")

priority = {}
sum_priority = 0

i = 1
for letter in string.ascii_letters:
    priority[letter] = i
    i += 1

l1 = ""
l2 = ""
l3 = ""
ctr = 1

for line in input_file:
    if (ctr == 1):
        l1 = set(line.strip())
    elif (ctr == 2):
        l2 = set(line.strip())
    else:
        l3 = set(line.strip())
    
    if (ctr == 3):
        ctr = 1
        common_initial = l1.intersection(l2)
        common = common_initial.intersection(l3)
        letter = ''.join(common)
        sum_priority += priority[letter]
    else:
        ctr += 1

print(sum_priority)