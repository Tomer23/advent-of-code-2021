FILENAME = './puzzle11/data/input'

grid = []
with open(FILENAME) as file:
    for line in file:
        grid.append([int(x) for x in list(line.strip())])

n = 10

def grid_step(grid):

    flash_grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            grid[i][j] += 1
    s = 1
    while s > 0:
        s = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 9 and flash_grid[i][j] == 0:
                    s += 1
                    flash_grid[i][j] = 1
        for i in range(n):
            for j in range(n):
                if flash_grid[i][j] == 1:
                    for i_f in range(i - 1, i + 2):
                        for j_f in range(j - 1, j + 2):
                            if (i_f, j_f) != (i, j) and i_f in range(n) and j_f in range(n):
                                grid[i_f][j_f] += 1
                    flash_grid[i][j] = 2

    for i in range(n):
        for j in range(n):
            if grid[i][j] > 9:
                grid[i][j] = 0
            
    return grid, flash_grid

step = 0
while True:
    grid, flash_grid = grid_step(grid)
    step += 1
    if int(sum([sum(x) for x in flash_grid]) / 2) == 100:
        break
print(step)
