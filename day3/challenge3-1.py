schem = []
sum = 0

def adjacentSymbol(i, j, schem):
    coords = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    for x, y in coords:
        try:
            if x >= 0 and y >= 0:
                if schem[x][y] not in ".1234567890":
                    return True
        except:
            continue
    return False

def adjacentSymbolRange(i, j, k, schem):
    for y in range(j,k):
        if adjacentSymbol(i, y, schem):
            return True
    return False

def sumPartsNums(schem):
    global sum
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
                if adjacentSymbolRange(i, j, k, schem):
                    sum += int(num)
                j = k
            j += 1
        i += 1

    print("Sum of parts numbers:", sum)

with open('day3/challenge3.txt') as file:
    for line in file:
        schem.append(line.replace('\n', ''))

sumPartsNums(schem)