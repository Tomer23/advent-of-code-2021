FILENAME = './puzzle8/data/input'

input_digits = []
output_digits = []

with open(FILENAME) as file:
    for line in file:
        input_digit, output_digit = line.strip().split('|')
        input_digits.append(input_digit.strip().split(' '))
        output_digits.append(output_digit.strip().split(' '))

total = 0
for s in range(len(input_digits)):
    digits = input_digits[s] + output_digits[s]
    digit_dict = {}
    digits = [''.join(sorted(el)) for el in digits]
    digits = list(set(digits))
    output_digit_ordered = [''.join(sorted(el)) for el in output_digits[s]]

    digit_dict[1] = [x for x in digits if len(x) == 2][0]
    digit_dict[4] = [x for x in digits if len(x) == 4][0]
    digit_dict[7] = [x for x in digits if len(x) == 3][0]
    digit_dict[8] = [x for x in digits if len(x) == 7][0]

    digit_dict[9] = [x for x in digits if set(digit_dict[4]) < set(x)]
    digit_dict[9] = [x for x in digit_dict[9] if x != digit_dict[8]][0]

    digit_dict[0] = [x for x in digits if set(digit_dict[7]) < set(x) and not (set(x) < set(digit_dict[9]))]
    digit_dict[0] = [x for x in digit_dict[0] if x != digit_dict[8] and  x != digit_dict[9]][0]
    
    digit_dict[3] = [x for x in digits if [ i for i in range(0,10) if i in digit_dict and set(x) < set(digit_dict[i])] == [8, 9] and set(digit_dict[1]) < set(x)]
    digit_dict[3] = [x for x in digit_dict[3] if x != digit_dict[4]][0]

    digit_dict[5] = [x for x in digits if [ i for i in range(0,10) if i in digit_dict and set(x) < set(digit_dict[i])] == [8, 9] and  x != digit_dict[4] and not (set(digit_dict[1]) < set(x))][0]

    digit_dict[6] = [x for x in digits if set(digit_dict[5]) < set(x)]
    digit_dict[6] = [x for x in digit_dict[6] if x != digit_dict[8] and x != digit_dict[9]][0]

    inv_digit_dict = {v: k for k, v in digit_dict.items()}
    for element in digits:
        if element not in inv_digit_dict:
            digit_dict[2] = element
            inv_digit_dict[element] = 2

    output = ''
    for dig in output_digit_ordered:
        output += str(inv_digit_dict[dig])
    total += int(output)
    print(output)
    
print(total)
