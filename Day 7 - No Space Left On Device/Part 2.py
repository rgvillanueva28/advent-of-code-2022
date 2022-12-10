import os
import math
import string

input_file = open("Day 7 - No Space Left On Device\input.txt", "r")

"""
--- file array ---
files = [{
    name: "the_name",
    location: "root/located/here",
    size: 12333
}]

--- dirs dictionary ---
dirs = {
    "dir_name": 2938,
    "dir_name_2: 19994
}
"""

files = []
dirs = {"root": 0}
curr_dir = ["root"]

# populating files and dir sizes
for line in input_file:
    arr = line.strip().split(" ")

    if (arr[0] == "$"):
        if (arr[1] == "cd"):
            if (arr[2] == "/"):
                curr_dir = ["root"]
            elif (arr[2] == ".."):
                curr_dir.pop()
            else:
                curr_dir.append(arr[2])
                dirs["/".join(curr_dir)] = 0
        continue
    else:
        if (arr[0] != "dir"):
            size = int(arr[0])
            files.append({"name": arr[1], "size": size,
                         "location": "/".join(curr_dir)})
            loop_dir = []
            
            for item in curr_dir:
                loop_dir.append(item)
                dirs["/".join(loop_dir)] += size



free_space = 70000000 - dirs["root"]
needed_space = 30000000 - free_space
print(needed_space)

val = 0
sorted_sizes = sorted(list(dirs.values()))

for item in sorted_sizes:
    if(item >= needed_space):
        val = item
        break

print(val)