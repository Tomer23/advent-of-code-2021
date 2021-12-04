FILENAME_NUMBERS = './puzzle4/data/input_numbers'
FILENAME_BOARDS = './puzzle4/data/input_boards'

with open(FILENAME_NUMBERS) as file:
    for line in file:
        bingo_numbers = [int(x) for x in line.split(',')]

s = 0
bingo_boards = [[]]
with open(FILENAME_BOARDS) as file:
    for line in file:
        if line == '\n':
            s += 1
            bingo_boards.append([])
        else:
            bingo_boards[s].append([int(x) for x in line.strip().replace('  ', ' ').split(' ')])

def check_number_on_board(bingo_board_remaining, bingo_number):
    for i in range(5):
        for j in range(5):
            if bingo_board_remaining[i][j] == bingo_number:
                bingo_board_remaining[i][j] = None
    return bingo_board_remaining

def is_board_winning(bingo_board_remaining):
    for i in range(5):
        if all(v is None for v in bingo_board_remaining[i]):
            return True
        if all(v is None for v in [x[i] for x in bingo_board_remaining]):
            return True
    return False


def process_board(bingo_board, bingo_numbers):
    bingo_board_remaining = bingo_board

    for id, bingo_number in enumerate(bingo_numbers):
        bingo_board_remaining = check_number_on_board(bingo_board_remaining, bingo_number)
        if is_board_winning(bingo_board_remaining):
            break
    score = sum([x if x is not None else 0 for y in bingo_board_remaining for x in y]) * bingo_number

    return score, id

score_id_list = []
for i in range(len(bingo_boards)):
    score, id = process_board(bingo_boards[i], bingo_numbers)
    score_id_list.append([score, id])
score_id_list.sort(key = lambda x: -x[1])
print(score_id_list)