FILENAME = './puzzle7/data/input'

with open(FILENAME) as file:
    for line in file:
        initial_positions = [int(x) for x in line.strip().split(',')]

# initial_positions = [16,1,2,0,4,2,7,1,2,14]

min_i = 0
min_fuel = 1000000000000
for i in range(0, max(initial_positions)):
    diff = []
    for crab in initial_positions:
        diff.append(sum(range(abs(crab - i) + 1)))
    if sum(diff) < min_fuel:
        min_fuel = sum(diff)
        min_i = i

print(min_i)
print(min_fuel)