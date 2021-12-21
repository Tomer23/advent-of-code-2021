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
    
universe_state = {}
universe_state[(pos_1, 0, pos_2, 0)] = 1

# 1 1 1 - 1
# 1 1 2 - 3
# 1 1 3 - 3
# 2 2 2 - 1
# 2 2 1 - 3
# 2 2 3 - 3
# 3 3 1 - 3
# 3 3 2 - 3 
# 3 3 3 - 1
# 1 2 3 - 6

dice_rolls = [
    [3, 1],
    [4, 3],
    [5, 6],
    [6, 7],
    [7, 6],
    [8, 3],
    [9, 1]
]

def clear_pos(pos, dice_load):
    pos += dice_load
    while pos > 10:
        pos -= 10
    return pos


def step_with_dice(universe_state, player):

    new_universe_state = {}
    for state in universe_state:
        pos_1, score_1, pos_2, score_2 = state
        if player == 1:
            for roll in dice_rolls:
                pos = clear_pos(pos_1, roll[0])
                score = score_1 + pos
                if (pos, score, pos_2, score_2) in new_universe_state:
                    new_universe_state[(pos, score, pos_2, score_2)] = new_universe_state[(pos, score, pos_2, score_2)] + roll[1] * universe_state[state]
                else:
                    new_universe_state[(pos, score, pos_2, score_2)] = roll[1] * universe_state[state]
        if player == 2:
            for roll in dice_rolls:
                pos = clear_pos(pos_2, roll[0])
                score = score_2 + pos
                if (pos_1, score_1, pos, score) in new_universe_state:
                    new_universe_state[(pos_1, score_1, pos, score)] = new_universe_state[(pos_1, score_1, pos, score)] + roll[1] * universe_state[state]
                else:
                    new_universe_state[(pos_1, score_1, pos, score)] = roll[1] * universe_state[state]
    return new_universe_state


def count_winning(universe_state, scores):
    new_universe_state = {}
    for state in universe_state:
        pos_1, score_1, pos_2, score_2 = state
        if score_1 >= 21:
            scores[0] += universe_state[state]
        elif score_2 >= 21:
            scores[1] += universe_state[state]
        else:
            new_universe_state[state] = universe_state[state]
    return new_universe_state, scores

scores = [0, 0]

while True:
    universe_state = step_with_dice(universe_state, 1)
    universe_state, scores = count_winning(universe_state, scores)
    universe_state = step_with_dice(universe_state, 2)
    universe_state, scores = count_winning(universe_state, scores)
    print(scores)
    if not universe_state:
        break

