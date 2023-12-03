schem = []
sum = 0
star_coords = {}

def adjacentSymbol(i, j, schem):
    coords = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    star_coords = []
    for x, y in coords:
        try:
            if x >= 0 and y >= 0:
                if schem[x][y] == "*":
                    star_coords.append((x, y))
        except:
            continue
    return star_coords

def adjacentSymbolRange(i, j, k, schem):
    star_coords = []
    for y in range(j,k):
        star_coords += adjacentSymbol(i, y, schem)
    return list(set(star_coords))

def sumGearRatios(schem):
    global sum
    global star_coords
    i = 0
    j = 0
    while i < len(schem):
        j = 0
        while j < len(schem[i]):
            if schem[i][j].isdigit():
                k = j+1
                num = schem[i][j]
                while k < len(schem[i]):
                    if schem[i][k].isdigit():
                        num += schem[i][k]
                        k += 1
                    else:
                        break
                adjacent_star_coords = adjacentSymbolRange(i, j, k, schem)
                if adjacent_star_coords != []:
                    for x,y in adjacent_star_coords:
                        string = str(x) + "," + str(y)
                        if string in star_coords:
                            star_coords[string].append(int(num))
                        else:
                            star_coords[string] = [int(num)]
                j = k
            j += 1
        i += 1

    for key, value in star_coords.items():
        if len(value) == 2:
            sum += (value[0] * value[1])

    print("Sum of gear ratios:", sum)

with open('day3/challenge3.txt') as file:
    for line in file:
        schem.append(line.replace('\n', ''))



sumGearRatios(schem)