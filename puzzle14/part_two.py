import numpy as np
import re

FILENAME = './puzzle14/data/input'

polymer = ''
instructions = {}
with open(FILENAME) as file:
    for line in file:
        if '->' in line and line.strip():
            instructions[line.strip().split(' -> ')[0]] = line.strip().split(' -> ')[1]
        elif '->' not in line and line.strip():
            polymer = line.strip()

print(polymer)

pair_instructions = {}
for pair in instructions:
    pair_instructions[pair] = [ pair[0] + instructions[pair], instructions[pair] + pair[1]]

polymer_pairs = []
for pair in pair_instructions:
    for element in pair_instructions[pair]:
        polymer_pairs.append(pair)
        polymer_pairs.append(element)
for i in range(len(polymer) - 1):
    polymer_pairs.append(polymer[i : i + 2])

polymer_pairs = list(set(polymer_pairs))

polymer_state = []
for pair in polymer_pairs:
    if pair in polymer:
        if pair[0] == pair[1]:
            polymer_state.append([len(re.findall(f'(?={pair})', polymer))])
        else:
            polymer_state.append([polymer.count(pair)])
    else:
        polymer_state.append([0])

polymer_transformation = [[0 for _ in range(len(polymer_pairs))] for _ in range(len(polymer_pairs))]

for pair in pair_instructions:
    for element in pair_instructions[pair]:
        i = polymer_pairs.index(element)
        j = polymer_pairs.index(pair)
        polymer_transformation[i][j] = 1

for n in range(40):
    polymer_state = np.dot(polymer_transformation, polymer_state)

    character_counter = {}
    for idx, pair in enumerate(polymer_pairs):
        for character in pair:
            if character not in character_counter:
                character_counter[character] = polymer_state[idx][0]
            else:
                character_counter[character] = character_counter[character] + polymer_state[idx][0]

    for character in character_counter:
        if character == polymer[0] or character == polymer[-1]:
            character_counter[character] = character_counter[character] - 1
        character_counter[character] = int(character_counter[character] / 2)
        if character == polymer[0] or character == polymer[-1]:
            character_counter[character] = character_counter[character] + 1
    character_counter = dict(sorted(character_counter.items(), key=lambda item: item[1], reverse=True))
    # print(character_counter)
    results = max(character_counter.values()) - min(character_counter.values())
    print("%.0f" % results)