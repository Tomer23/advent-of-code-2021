FILENAME = './puzzle3/data/input'

bit_list = [0] * 12
s = 0
with open(FILENAME) as file:
    for line in file:
        for id, bit_value in enumerate(line[0:12]):
            bit_list[id] += int(bit_value)
        s += 1
gamma = ''
epsilon = ''
for sum_value in bit_list:
    if sum_value > s/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))
