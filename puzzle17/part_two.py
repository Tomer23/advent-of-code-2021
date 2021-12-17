FILENAME = './puzzle17/data/input'

with open(FILENAME) as file:
    for line in file:
        processed_line = line.strip().replace('target area: ', '')
        p_x, p_y = processed_line.split(', ')
        p_x = p_x.replace('x=', '').split('..')
        p_y = p_y.replace('y=', '').split('..')
        target_coordinates = [[int(p_x[0]), int(p_y[0])], [int(p_x[1]), int(p_y[1])]]
        
print(target_coordinates)

def run_probe(initital_vector):
    x, y = 0, 0
    y_max = 0
    current_vector = initital_vector
    while True:
        x += current_vector[0]
        y += current_vector[1]
        y_max = max([y_max, y])

        if current_vector[0] > 0:
            current_vector[0] -= 1
        current_vector[1] -= 1
        if x >= target_coordinates[0][0] and x <= target_coordinates[1][0] and y >= target_coordinates[0][1] and y <= target_coordinates[1][1]:
            break
        if x > target_coordinates[1][0] or y < target_coordinates[0][1]:
            y_max = None
            break
    return y_max

success_count = 0
n = 500
for i in range(0, target_coordinates[1][0] + 1):
    for j in range(target_coordinates[0][1] - 1, n):
        if run_probe([i, j]) is not None:
            success_count += 1

print(success_count)