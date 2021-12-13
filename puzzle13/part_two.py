FILENAME = './puzzle13/data/input'

dot_list = []
instructions = []
with open(FILENAME) as file:
    for line in file:
        if line[0:4] != 'fold' and line.strip():
            dot_list.append([int(x) for x in line.strip().split(',')])
        elif line[0:4] == 'fold' and line.strip():
            line_processed = line.strip().replace('fold along ', '').split('=')
            instructions.append([line_processed[0], int(line_processed[1])])

n_x = max([x[0] for x in dot_list ]) + 1
n_y = max([x[1] for x in dot_list ]) + 1

table = [[ 0 for _ in range(n_x)] for _ in range(n_y)]

for dots in dot_list:
    table[dots[1]][dots[0]] = 1


def fold_table(table, fold_type, value):
    n_x = len(table[0])
    n_y = len(table)

    if fold_type == 'y':
        new_table = [[ 0 for _ in range(n_x)] for _ in range(value)]
        for i in range(len(table)):
            for j in range(len(table[i])):
                if i < value:
                    if table[i][j] == 1:
                        new_table[i][j] = 1
                elif i > value:
                    if table[i][j] == 1:
                        new_table[2 * value - i][j] = 1

    if fold_type == 'x':
        new_table = [[ 0 for _ in range(value)] for _ in range(n_y)]
        for i in range(len(table)):
            for j in range(len(table[i])):
                if j < value:
                    if table[i][j] == 1:
                        new_table[i][j] = 1
                elif j > value:
                    if table[i][j] == 1:
                        new_table[i][2 * value - j] = 1

    return new_table

for instruction in instructions:
    table = fold_table(table, instruction[0], instruction[1])

for line in table:
    print(' '.join([str(x) if x == 1 else ' ' for x in line]))

