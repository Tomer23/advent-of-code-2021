FILENAME = './puzzle1/data/input'

s = 0
previous_value = None
current_list = [None, None, None]


def shift_list(input_list):
    input_list[2] = input_list[1]
    input_list[1] = input_list[0]
    input_list[0] = None
    return input_list

with open(FILENAME) as file:
    for line in file:
        current_list = shift_list(current_list)
        current_list[0] = int(line)
        if None not in current_list:
            if previous_value:
                if sum(current_list) > previous_value:
                    s += 1
            previous_value = sum(current_list)
print(s)