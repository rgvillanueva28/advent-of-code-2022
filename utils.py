import string

obj = {}

letter = "a"
i = 1
for letter in string.ascii_letters:
    obj[letter] = i
    i += 1

print(obj)