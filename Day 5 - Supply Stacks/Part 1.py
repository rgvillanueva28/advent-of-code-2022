import os
import math
import string

input_file = open("input.txt", "r")

stacks = [[] for x in range(9)]


num_line = 1 #what line are we in?
#iterate every line
for line in input_file:
    # Create the given stack
    if (num_line < 9):
        ctr = 0 #what index are we in the line?
        char_ctr = 0 #What index are we every 4 chars?
        stack_num = 0 #what stack index are we?
        #iterate every characted in a line
        for char in line.strip("\n"):
            ctr += 1
            if(char_ctr % 4 == 1): #0 index, we need to get the second char every 4 characters
                if (char != " "):
                    stacks[stack_num].insert(0, char)
                stack_num += 1
            
            char_ctr += 1
    
    # Do the job
    elif (num_line >= 11):
        instruction = line.strip().split(" ")
        move_count = int(instruction[1])
        from_stack = int(instruction[3]) - 1
        to_stack = int(instruction[5]) - 1

        for i in range(move_count):
            remove = stacks[from_stack].pop()
            stacks[to_stack].append(remove)

    num_line += 1

print("".join([x[-1] for x in stacks]))