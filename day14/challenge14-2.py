with open("day14/challenge14.txt", "r") as file:
    map = [list(line.replace('\n', '')) for line in file.readlines()]

def print_map():
    for row in map:
        print(''.join(row))
    print("")

def tilt_n(i, j):
    if i <= 0 or map[i-1][j] in "#O":
        return

    map[i][j] = '.'
    map[i-1][j] = 'O'
    tilt_n(i-1, j)

def tilt_e(i, j):
    if j >= len(map[i])-1 or map[i][j+1] in "#O":
        return

    map[i][j] = '.'
    map[i][j+1] = 'O'
    tilt_e(i, j+1)

def tilt_w(i, j):
    if j <= 0 or map[i][j-1] in "#O":
        return

    map[i][j] = '.'
    map[i][j-1] = 'O'
    tilt_w(i, j-1)

def tilt_s(i, j):
    if i >= len(map)-1 or map[i+1][j] in "#O":
        return

    map[i][j] = '.'
    map[i+1][j] = 'O'
    tilt_s(i+1, j)

for k in range(1000):
    for i in range(1, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == 'O':
                tilt_n(i, j)
    for i in range(0, len(map)):
        for j in range(1, len(map[i])):
            if map[i][j] == 'O':
                tilt_w(i, j)
    for i in range(len(map)-1, -1, -1):
        for j in range(0, len(map[i])):
            if map[i][j] == 'O':
                tilt_s(i, j)
    for i in range(0, len(map)):
        for j in range(len(map[i])-1, -1, -1):
            if map[i][j] == 'O':
                tilt_e(i, j)

sum = 0
val = 1
for i in range(len(map)-1, -1, -1):
    sum += (val * map[i].count('O'))
    val += 1

print('Sum of rock worth:', sum)