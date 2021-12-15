FILENAME = './puzzle15/data/input'

cave = []
with open(FILENAME) as file:
    for line in file:
        cave.append([int(x) for x in list(line.strip())])

scores = [[ 0 for _ in range(len(cave))] for _ in range(len(cave))]

for i in range(len(cave) - 1, -1 , -1):
    for j in range(len(cave) - 1, -1 , -1):
        if i < len(cave) - 1 and j < len(cave) - 1:
            scores[i][j] = cave[i][j] + min([scores[i + 1][j], scores[i][j + 1]])
        elif i < len(cave) - 1 and j == len(cave) - 1:
            scores[i][j] = cave[i][j] + scores[i + 1][j]
        elif i == len(cave) - 1 and j < len(cave) - 1:
            scores[i][j] = cave[i][j] + scores[i][j + 1]
        elif i == len(cave) - 1 and j == len(cave) - 1:
            scores[i][j] = cave[i][j]

#   b
# a   c
#   d


prev_value = 1000000000
current_value = 100000000

while current_value != prev_value:
    prev_value = current_value
    for i in range(0, len(cave)):
        for j in range(0, len(cave)):
            a, b, c, d = 100000, 100000, 100000, 100000
            if i > 0:
                a = scores[i - 1][j]
            if j > 0:
                b = scores[i][j - 1]
            if i < len(cave) - 1:
                d = scores[i + 1][j]
            if j < len(cave) - 1:
                c = scores[i][j + 1]
            if i < len(cave) - 1 and j < len(cave) - 1:
                scores[i][j] = cave[i][j] + min([a, b, c, d])
    current_value = sum([sum(x) for x in scores])
    print(current_value)


print(scores[0][0] - cave[0][0])