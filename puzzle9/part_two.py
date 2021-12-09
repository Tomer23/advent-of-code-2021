from functools import reduce

FILENAME = './puzzle9/data/input'

height_points = []
with open(FILENAME) as file:
    for line in file:
        height_points.append([int(x) for x in list(line.strip())])


def generate_zero():
    zero_list = []
    for i in range(0, len(height_points)):
        zero_list.append([0 for x in range(0, len(height_points[0]))])
    return zero_list

allocated_points = generate_zero()
basins = []
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
            allocated_points[i][j] = 1
            basin_empty = generate_zero()
            basin_empty[i][j] = 1
            basins.append(basin_empty)
        if height_points[i][j] == 9:
            allocated_points[i][j] = 1

def which_basin(i, j, basins):
    for s in range(len(basins)):
        if basins[s][i][j] == 1:
            return s
    return

count = 1
while count > 0:
    count = 0
    for i in range(0, len(height_points)):
        for j in range(0, len(height_points[0])):
            if allocated_points[i][j] == 0:
                if i > 0:
                    if height_points[i - 1][j] < height_points[i][j] and allocated_points[i - 1][j] == 1:
                        s = which_basin(i - 1, j, basins)
                        allocated_points[i][j] = 1
                        basins[s][i][j] = 1
                        count += 1
                if i < len(height_points) - 1:
                    if height_points[i + 1][j] < height_points[i][j] and allocated_points[i + 1][j] == 1:
                        s = which_basin(i + 1, j, basins)
                        allocated_points[i][j] = 1
                        basins[s][i][j] = 1
                        count += 1
                if j > 0:
                    if height_points[i][j - 1] < height_points[i][j] and allocated_points[i][j - 1] == 1:
                        s = which_basin(i, j - 1, basins)
                        allocated_points[i][j] = 1
                        basins[s][i][j] = 1
                        count += 1
                if j < len(height_points[0]) - 1:
                    if height_points[i][j + 1] < height_points[i][j] and allocated_points[i][j + 1] == 1:
                        s = which_basin(i, j + 1, basins)
                        allocated_points[i][j] = 1
                        basins[s][i][j] = 1
                        count += 1

# print(allocated_points)
# print(basins)

basin_sizes = []
for b in basins:
    basin_sizes.append(sum([sum(x) for x in b]))

print(basin_sizes)
print(sorted(basin_sizes, reverse=True)[:3])
result1 = reduce((lambda x, y: x * y), sorted(basin_sizes, reverse=True)[:3])
print(result1)
