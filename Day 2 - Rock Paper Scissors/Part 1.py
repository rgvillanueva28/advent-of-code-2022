import os

game_mech = {
    "X": {
        "value": 1,
        "A": "draw",
        "B": "lose",
        "C": "win",
    },
    "Y": {
        "value": 2,
        "A": "win",
        "B": "draw",
        "C": "lose"
    },
    "Z": {
        "value": 3,
        "A": "lose",
        "B": "win",
        "C": "draw"
    },
}

input_file = open("input.txt", "r")

my_score = 0

for line in input_file:
    enemy, me = line.strip().split(" ")

    if (game_mech[me][enemy] == "win"):
        my_score += 6
    elif (game_mech[me][enemy] == "draw"):
        my_score += 3

    my_score += game_mech[me]["value"]

print(my_score)
