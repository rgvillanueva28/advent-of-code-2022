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

for line in input_file:
    mid = math.floor(len(line.strip())/2)
    c1 = set(line[0:mid])
    c2 = set(line[mid:])
    # print(c1, c2)
    common = c1.intersection(c2)
    letter = ''.join(common)
    sum_priority += priority[letter]

print(sum_priority)