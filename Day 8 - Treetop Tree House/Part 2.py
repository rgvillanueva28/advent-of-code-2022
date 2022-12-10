import os
import math
import string

input_file = open("Day 8 - Treetop Tree House\input.txt", "r")

trees_arr = []

row_ctr = 0
for line in input_file:
    chars = []
    for char in line.strip():
        chars.append(char)
    trees_arr.append(chars)
    row_ctr += 1

row = 1
max_row = len(trees_arr) - 1
max_col = len(trees_arr[0]) - 1

highest_score = 0

while row < max_row:
    col = 1
    while col < max_col:
        # all items to loop here
        curr_val = trees_arr[row][col]

        l_score = 0
        r_score = 0
        t_score = 0
        b_score = 0

        #check to the left
        left_col_i = col - 1
        while (left_col_i >= 0):
            compared_value = trees_arr[row][left_col_i]
            if (compared_value >= curr_val):
                l_score += 1
                break
            l_score += 1
            left_col_i -= 1
        
        #check to the right
        right_col_i = col + 1
        while (right_col_i < len(trees_arr[0])):
            compared_value = trees_arr[row][right_col_i]
            if (compared_value >= curr_val):
                r_score += 1
                break
            r_score += 1
            right_col_i += 1
        
        #check to the top
        top_row_i = row - 1
        while (top_row_i >= 0):
            compared_value = trees_arr[top_row_i][col]
            if (compared_value >= curr_val):
                t_score += 1
                break
            t_score += 1
            top_row_i -= 1

        #Check to the bottom
        bot_row_i = row + 1
        while (bot_row_i < len(trees_arr)):
            compared_value = trees_arr[bot_row_i][col]
            if (compared_value >= curr_val):
                b_score += 1
                break
            b_score += 1
            bot_row_i += 1

        # update highest score here
        this_score = l_score * r_score * t_score * b_score

        if(this_score > highest_score):
            highest_score = this_score

        col += 1

    row += 1

print(highest_score)