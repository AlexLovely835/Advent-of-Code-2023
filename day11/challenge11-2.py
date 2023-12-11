map = []

def expand(map):
    row_expansion = []
    for i in range(len(map)):
        if all(x == '.' for x in map[i]):
            row_expansion.append(i)

    column_expansion = []
    for j in range(len(map[0])):
        if all(map[i][j] == '.' for i in range(len(map))):
            column_expansion.append(j)
    
    return row_expansion, column_expansion

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

row_exp, col_exp = expand(map)

coords = find_galaxies(map)

sum = 0

for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]

        exp = 0
        for row in row_exp:
            if min(x1, x2) <= row <= max(x1, x2):
                exp += 999999
        for col in col_exp:
            if min(y1, y2) <= col <= max(y1, y2):
                exp += 999999
    
        sum += (abs(x1 - x2)) + abs(y1 - y2) + exp

print("Sum of shorted paths between each galaxy:", sum)