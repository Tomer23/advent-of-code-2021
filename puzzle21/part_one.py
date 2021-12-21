FILENAME = './puzzle21/data/input'

pos_1 = 0
pos_2 = 0
with open(FILENAME) as file:
    for line in file:
        player, pos = line.strip().split(': ')
        if player == 'Player 1 starting position':
            pos_1 = int(pos)
        elif player == 'Player 2 starting position':
            pos_2 = int(pos)
    

dice = iter(range(1, 101, 1))
dice_count = 0

score_1, score_2 = 0, 0

def step_with_dice(pos, dice_count, dice):

    dice_load = 0
    for _ in range(3):
        dice_count += 1
        try:
            dice_load += next(dice)
        except StopIteration:
            dice = iter(range(1, 101, 1))
            dice_load += next(dice)

    pos += dice_load
    while pos > 10:
        pos -= 10

    return pos, dice, dice_count

while True:

    pos_1, dice, dice_count = step_with_dice(pos_1, dice_count, dice)
    score_1 += pos_1
    if score_1 >= 1000:
        break

    pos_2, dice, dice_count = step_with_dice(pos_2, dice_count, dice)
    score_2 += pos_2
    if score_2 >= 1000:
        break

print(min([score_1, score_2]) * dice_count)