import os

input_file = open("input.txt", "r")

highest_value = 0

current_value = 0;

for line in input_file:
    if (line == "\n"):

        if current_value > highest_value:
            highest_value = current_value
        
        current_value = 0
        continue

    current_value += int(line)

print(highest_value)