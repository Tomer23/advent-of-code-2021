FILENAME = './puzzle2/data/input'

x = 0
y = 0
with open(FILENAME) as file:
    for line in file:
        direction, value = line.split(' ')
        if direction == 'forward':
            x += int(value)
        elif direction == 'down':
            y += int(value)
        elif direction == 'up':
            y -= int(value)
print(x * y)
