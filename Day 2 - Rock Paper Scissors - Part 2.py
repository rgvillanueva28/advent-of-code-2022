import os

game_mech = {
    "X": {
        "value": 1,
    },
    "Y": {
        "value": 2,
    },
    "Z": {
        "value": 3,
    },
}

enemy_mech = {
    "A": {
        "draw": "X",
        "lose": "Y",
        "win": "Z"
    },
    "B": {
        "win": "X",
        "draw": "Y",
        "lose": "Z"
    },
    "C": {
        "lose": "X",
        "win": "Y",
        "draw": "Z"
    },
}

input_file = open("Day 2 - Rock Paper Scissors.txt", "r")

my_score = 0

for line in input_file:
    enemy, me = line.strip().split(" ")

    my_card = ""
    if (me == "X"): #I Need to lose, so enemy need to win
        my_card = enemy_mech[enemy]["win"]
    elif (me == "Y"): #I Need to draw, so enemy need to draw
        my_card = enemy_mech[enemy]["draw"]
        my_score += 3
    else: #I Need to win, so enemy need to lose
        my_card = enemy_mech[enemy]["lose"]
        my_score += 6

    my_score += game_mech[my_card]["value"]

print(my_score)
