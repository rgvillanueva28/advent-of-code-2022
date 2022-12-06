import os
import math
import string

input_file = open("input.txt", "r")

string = input_file.readline()
marker = ""

ctr = 4
while True:
    current = string[ctr - 4:ctr]

    if(len(set(current)) == 4):
        marker = current
        break

    ctr += 1


print(marker, "\n", ctr)
