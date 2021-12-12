FILENAME = './puzzle12/data/input'

pairs = []
with open(FILENAME) as file:
    for line in file:
        pairs.append(line.strip().split('-'))
print(pairs)

cave_list = {}
for pair in pairs:
    if pair[0] not in cave_list:
        cave_list[pair[0]] = []
    if pair[1] not in cave_list:
        cave_list[pair[1]] = []

for cave in cave_list:
    if cave != 'end':
        for pair in pairs:
            if cave == pair[0] and pair[1] not in cave_list[cave] and pair[1] != 'start':
                cave_list[cave].append(pair[1])
            if cave == pair[1] and pair[0] not in cave_list[cave] and pair[0] != 'start':
                cave_list[cave].append(pair[0])

print(cave_list)

route_list = [
    [
        ['start'],
        1,
        0,
        'start'
    ]
]

count = 1
while count > 0:
    for idx, route in enumerate(route_list):
        if route[1] > 0:
            for connection in cave_list[route[0][-1]]:
                if (connection.islower() and (connection not in route[0] or route[2] == 1)) or not connection.islower():
                    new_route = route[0] + [connection]
                    is_double = max([new_route.count(element) for element in new_route if element.islower() and element not in [ 'start', 'end']], default=0)
                    route_list.append([new_route, 1, is_double])
            route_list[idx][1] = 0
    count = sum([ x[1] for x in route_list])
    print(count)

filtered_lists = sum([ 1 for route in route_list if route[0][-1] == 'end'])
print(filtered_lists)
