from copy import deepcopy
map = []

def expand(map):
    new_map = deepcopy(map)

    insertions = []
    for i in range(len(map)):
        if all(x == '.' for x in map[i]):
            insertions.append(i)
    for i in range(len(insertions)):
        new_map.insert(insertions[i] + i, ['.']*len(map[0]))

    insertions = []
    for j in range(len(map[0])):
        if all(map[i][j] == '.' for i in range(len(map))):
            insertions.append(j)
    for j in range(len(insertions)):
        for i in range(len(new_map)):
            new_map[i].insert(insertions[j]+j, '.')
    
    return new_map

def find_galaxies(map):
    coords = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '#':
                coords.append((i, j))

    return coords

with open('day11/challenge11.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    temp = line.replace('\n','')
    map.append([*temp])

map = expand(map)

coords = find_galaxies(map)

sum = 0

for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        sum += (abs(x1 - x2) + abs(y1 - y2))

print("Sum of shorted paths between each galaxy:", sum)