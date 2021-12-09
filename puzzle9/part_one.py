FILENAME = './puzzle9/data/input'

height_points = []
with open(FILENAME) as file:
    for line in file:
        height_points.append([int(x) for x in list(line.strip())])

total = 0
for i in range(0, len(height_points)):
    for j in range(0, len(height_points[0])):
        up, down, left, right = 10, 10, 10, 10
        if i > 0:
            up = height_points[i - 1][j]
        if i < len(height_points) - 1:
            down = height_points[i + 1][j]
        if j > 0:
            left = height_points[i][j - 1]
        if j < len(height_points[0]) - 1:
            right = height_points[i][j + 1]
        if height_points[i][j] < up and height_points[i][j] < down and height_points[i][j] < left and height_points[i][j] < right:
            total += height_points[i][j] + 1
print(total)