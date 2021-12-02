FILENAME = './puzzle1/data/input'

s = 0
previous_value = None
with open(FILENAME) as file:
    for line in file:
        if previous_value:
            if int(line) > previous_value:
                s += 1
        previous_value = int(line)
print(s)