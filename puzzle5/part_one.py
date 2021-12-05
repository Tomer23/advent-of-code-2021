FILENAME = './puzzle5/data/input'

coordinates = []
with open(FILENAME) as file:
    for line in file:
        x, y = line.split('->')
        x = x.strip().split(',')
        y = y.strip().split(',')
        coordinates.append([[int(x[0]),int(x[1])], [int(y[0]),int(y[1])]])

coordinates_filtered = [pair for pair in coordinates if pair[0][0]==pair[1][0] or pair[0][1]==pair[1][1]]
a = 1000
board = [[0 for _ in range(a)] for _ in range(a)]

for coord_pair in coordinates_filtered:
    if coord_pair[0][0] <= coord_pair[1][0]:
        x_change = 1
    else:
        x_change = -1
    if coord_pair[0][1] <= coord_pair[1][1]:
        y_change = 1
    else:
        y_change = -1

    for i in range(coord_pair[0][0],coord_pair[1][0] + x_change, x_change):
        for j in range(coord_pair[0][1],coord_pair[1][1] + y_change, y_change):
            board[i][j] = board[i][j] + 1

coordinates_remaining = [pair for pair in coordinates if pair[0][0]!=pair[1][0] and pair[0][1]!=pair[1][1]]

for coord_pair in coordinates_remaining:
    if coord_pair[0][0] <= coord_pair[1][0]:
        x_change = 1
    else:
        x_change = -1
    if coord_pair[0][1] <= coord_pair[1][1]:
        y_change = 1
    else:
        y_change = -1
    
    change = abs(coord_pair[0][0] - coord_pair[1][0])
    for d in range(change + 1):
        i = coord_pair[0][0] + x_change * d
        j = coord_pair[0][1] + y_change * d
        board[i][j] = board[i][j] + 1

s = 0
for i in range(0,a):
    for j in range(0,a):
        if board[i][j] >= 2:
            s += 1
print(s)