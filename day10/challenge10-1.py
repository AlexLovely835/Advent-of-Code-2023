import math

i, j = 0, 0
map = []
visited = []
visiting_queue = []

with open('day10/challenge10.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    temp = line.replace('\n','')
    map.append([*temp])


for x in range(len(map)):
    for y in range(len(map[x])):
        if map[x][y] == 'S':
            print("result")
            sx, sy = x, y
            visited.append((x, y))
            break

if map[sx][sy+1] == '-' or map[sx][sy+1] == '7' or map[sx][sy+1] == 'J':
    visiting_queue.append((sx, sy+1, "west"))
if map[sx][sy-1] == '-' or map[sx][sy-1] == 'L' or map[sx][sy-1] == 'F':
    visiting_queue.append((sx, sy-1, "east"))
if map[sx+1][sy] == '|' or map[sx+1][sy] == 'L' or map[sx+1][sy] == 'J':
    visiting_queue.append((sx+1, sy, "north"))
if map[sx-1][sy] == '|' or map[sx-1][sy] == 'F' or map[sx-1][sy] == '7':
    visiting_queue.append((sx-1, sy, "south"))

while visiting_queue[0][0] != visiting_queue[1][0] or visiting_queue[0][1] != visiting_queue[1][1]:
    i, j, dir = visiting_queue.pop(0)
    tiles = {
        "|": {
            "south": (i-1, j, "south"),
            "north": (i+1, j, "north")
        }, 
        "-": {
            "west": (i, j+1, "west"),
            "east": (i, j-1, "east")
        }, 
        "L": {
            "north": (i, j+1, "west"),
            "east": (i-1, j, "south")
        }, 
        "J": {
            "north": (i, j-1, "east"),
            "west": (i-1, j, "south")
        }, 
        "7": {
            "south": (i, j-1, "east"),
            "west": (i+1, j, "north")
        }, 
        "F": {
            "south": (i, j+1, "west"),
            "east": (i+1, j, "north")
        }
    }
    visited.append((i,j))
    visiting_queue.append((tiles[map[i][j]][dir]))

print("Steps furthest from start:", math.floor((len(visited)+1)/2))