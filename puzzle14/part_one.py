from collections import Counter

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

for n in range(1):
    new_polymer = ''
    last_element = None
    for element in polymer:
        if last_element:
            if last_element + element in instructions:
                new_polymer = new_polymer + instructions[last_element + element] + element
            else:
                new_polymer = new_polymer + element
        else:
            new_polymer = element
        last_element = element
    polymer = new_polymer
    occurences = Counter(list(polymer))
    
print(occurences)
print(max(occurences.values()) - min(occurences.values()))