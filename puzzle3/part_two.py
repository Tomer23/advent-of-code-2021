FILENAME = './puzzle3/data/input'

def load_with_filter(filter, preferred = 1):
    position = sum([1 for x in filter if x != '2'])
    bit_list = [0] * 12
    s = 0
    with open(FILENAME) as file:
        for line in file:
            if line[0:position] == filter[0:position]:
                for id, bit_value in enumerate(line[0:12]):
                    bit_list[id] += int(bit_value)
                s += 1
    if bit_list[position] >= s/2:
        filter = filter[0:position] + str(preferred) + filter[position+1:]
    else:
        filter = filter[0:position] + str(1 - preferred) + filter[position+1:]
    if s == 1:
        filter = ''.join([str(int) for int in bit_list])
    return bit_list, filter

filter = '2' * 12
for i in range(12):
    bit_list, filter = load_with_filter(filter, preferred=1)
    if filter == ''.join([str(int) for int in bit_list]):
        break
oxygen = filter

filter = '2' * 12
for i in range(12):
    bit_list, filter = load_with_filter(filter, preferred=0)
    if filter == ''.join([str(int) for int in bit_list]):
        break
co_two = filter

print(int(oxygen, 2) * int(co_two, 2))
