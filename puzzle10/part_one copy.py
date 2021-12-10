FILENAME = './puzzle10/data/test'


def calculate_segment(segment):
    y = [0, 0, 0, 0]  # ( [ { <
    for x in segment:
        if x == '(':
            y[0] += 1
        elif x == '[':
            y[1] += 1
        elif x == '{':
            y[2] += 1
        elif x == '<':
            y[3] += 1
        elif x == ')':
            y[0] += -1
        elif x == ']':
            y[1] += -1
        elif x == '}':
            y[2] += -1
        elif x == '>':
            y[3] += -1
    return y

closing_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
closing_y_dict = {
    '(': 0,
    '[': 1,
    '{': 2,
    '<': 3
}
add_value_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def can_be_reduced(segment):
    count = 1
    while count > 0:
        start_count = len(segment)
        segment = segment.replace('()', '')
        segment = segment.replace('[]', '')
        segment = segment.replace('\{\}', '')
        segment = segment.replace('<>', '')
        segment = segment.replace('<>', '')
        if len(segment) == start_count:
            count = 0
    return len(segment), segment

with open(FILENAME) as file:
    for line in file:
        segment = line.strip()
        print(segment)
        print(can_be_reduced(segment))


# total = 0
# with open(FILENAME) as file:
#     for line in file:
#         segment = line.strip()
#         min_j = 100000
#         add_value = 0
#         for i in range(0, len(segment)):
#             for j in range(i + 2, len(segment)):
#                 y = calculate_segment(segment[i:j])
#                 if segment[i] in closing_dict:
#                     if segment[j - 1] == closing_dict[segment[i]]:
#                         if y[closing_y_dict[segment[i]]] == 0:
                            
#                             print(segment[i:j])
#                             print(can_be_reduced(segment[i:j]))

#                             if any(n != 0 for n in y):
#                                 if j < min_j:
#                                     min_j = j
#                                     add_value = add_value_dict[segment[j - 1]]
#                                     # print(segment[i:j])
# print(total)