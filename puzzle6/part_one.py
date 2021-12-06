FILENAME = './puzzle6/data/input'

with open(FILENAME) as file:
    for line in file:
        initial_state = [int(x) for x in line.strip().split(',')]

# initial_state = [3,4,3,1,2]

current_state = {}

for i in range(0,9):
    current_state[i] = sum([1 for x in initial_state if x == i])

n = 256
for step in range(n):
    current_birth = current_state[0]
    for i in range(0,8):
        current_state[i] = current_state[i+1]
    current_state[8] = current_birth
    current_state[6] = current_state[6] + current_birth
    print(current_state)

print(sum([ current_state[x] for x in current_state ]))