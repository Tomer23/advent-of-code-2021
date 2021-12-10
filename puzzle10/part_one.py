FILENAME = './puzzle10/data/input'


closing_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
add_value_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

total = 0
with open(FILENAME) as file:
    for line in file:
        segment = line.strip()
        segment_positions = ['' for _ in range(len(segment))]
        s_open = 0
        for x in range(len(segment)):
            if segment[x] in closing_dict:
                segment_positions[s_open] = segment_positions[s_open] + segment[x]
                s_open += 1
            else:
                if closing_dict[segment_positions[s_open - 1][-1]] == segment[x]:
                    segment_positions[s_open - 1] = segment_positions[s_open - 1] + segment[x]
                    s_open -= 1
                else:
                    total += add_value_dict[segment[x]]
                    break
print(total)