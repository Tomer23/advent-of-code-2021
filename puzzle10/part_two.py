FILENAME = './puzzle10/data/input'


closing_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
add_value_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []
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
                    break
        if x == len(segment) - 1:
            added_string = ''
            for j in range(len(segment) - 1, -2, -1):
                if segment_positions[j]:
                    if segment_positions[j][-1] in closing_dict:
                        added_string = added_string + closing_dict[segment_positions[j][-1]]
                        segment_positions[j] = segment_positions[j] + closing_dict[segment_positions[j][-1]]
            added_value = 0
            for s in added_string:
                added_value = added_value * 5
                added_value += add_value_dict[s]
            scores.append(added_value)

scores = sorted(scores)
print(scores[int(len(scores) / 2 - 0.5)])