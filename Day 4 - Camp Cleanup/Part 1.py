import os
import math
import string

input_file = open("input.txt", "r")

counter = 0

for line in input_file:
    g1, g2 = line.strip().split(",")
    g1a, g1b = g1.split("-")
    g2a, g2b = g2.split("-")
    s1 = set(range(int(g1a), int(g1b) + 1))
    s2 = set(range(int(g2a), int(g2b) + 1))

    if(s1.issubset(s2) or s2.issubset(s1)):
        counter += 1


print(counter)