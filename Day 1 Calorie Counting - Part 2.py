import os

input_file = open("Day 1 Calorie Counting input.txt", "r")

values = []

current_value = 0;

for line in input_file:
    if (line == "\n"):
        values.append(current_value)
        current_value = 0
        continue

    current_value += int(line)

values.sort()

print("Top 3 = ", values[-3:])

print("sum = ", sum(values[-3:]))