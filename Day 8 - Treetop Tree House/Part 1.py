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

vis_ctr = len(trees_arr) * 4 - 4

while row < max_row:
    col = 1
    while col < max_col:
        # all items to loop here

        curr_val = trees_arr[row][col]

        is_hidden = False
        #check left
        left_col_i = 0
        while (left_col_i < col):
            compared_value = trees_arr[row][left_col_i]
            if (compared_value >= curr_val):
                is_hidden = True
                break
            left_col_i += 1
        
        if (not(is_hidden)):
            vis_ctr += 1
            col += 1
            continue
        
        is_hidden = False
        #right check
        right_col_i = col + 1
        while (right_col_i < len(trees_arr[0])):
            compared_value = trees_arr[row][right_col_i]
            if (compared_value >= curr_val):
                is_hidden = True
                break
            right_col_i += 1
        
        if (not(is_hidden)):
            vis_ctr += 1
            col += 1
            continue

        is_hidden = False
        #top check
        top_row_i = 0
        while (top_row_i < row):
            compared_value = trees_arr[top_row_i][col]
            if (compared_value >= curr_val):
                is_hidden = True
                break
            top_row_i += 1

        if (not(is_hidden)):
            vis_ctr += 1
            col += 1
            continue
        
        is_hidden = False
        #bot check
        bot_row_i = row + 1
        while (bot_row_i < len(trees_arr)):
            compared_value = trees_arr[bot_row_i][col]
            if (compared_value >= curr_val):
                is_hidden = True
                break
            bot_row_i += 1

        if (not(is_hidden)):
            vis_ctr += 1
            col += 1
            continue

        col += 1

    row += 1

print(vis_ctr)