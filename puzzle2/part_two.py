FILENAME = './puzzle2/data/input'

x = 0
y = 0
z = 0
with open(FILENAME) as file:
    for line in file:
        direction, value = line.split(' ')
        if direction == 'forward':
            x += int(value)
            y += z * int(value)
        elif direction == 'down':
            z += int(value)
        elif direction == 'up':
            z -= int(value)
print(x * y)
