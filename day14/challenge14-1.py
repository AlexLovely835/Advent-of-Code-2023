with open("day14/challenge14.txt", "r") as file:
    map = [list(line.replace('\n', '')) for line in file.readlines()]

def print_map():
    for row in map:
        print(''.join(row))

def tilt(i, j):
    if i <= 0 or map[i-1][j] in "#O":
        return

    map[i][j] = '.'
    map[i-1][j] = 'O'
    tilt(i-1, j)

for i in range(1, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == 'O':
            tilt(i, j)

sum = 0
val = 1
for i in range(len(map)-1, -1, -1):
    sum += (val * map[i].count('O'))
    val += 1

print('Sum of rock worth:', sum)