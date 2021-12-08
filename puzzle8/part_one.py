FILENAME = './puzzle8/data/input'


input_digits = []
output_digits = []

with open(FILENAME) as file:
    for line in file:
        input_digit, output_digit = line.strip().split('|')
        input_digits.append(input_digit.strip().split(' '))
        output_digits.append(output_digit.strip().split(' '))

count = 0
for line in output_digits:
    for element in line:
        if len(element) in [2, 3, 4, 7]:
            count += 1
print(count)