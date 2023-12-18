map = []

with open('day16/challenge16.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    temp = line.replace('\n','')
    map.append([*temp])

energized = [[[] for _ in range(len(map[0]))] for _ in range(len(map))]

visiting_queue = [(0, 0, "west")]

while visiting_queue != []:
    i, j, dir = visiting_queue.pop(0)
    if dir in energized[i][j]:
        continue
    else:
        energized[i][j].append(dir)
    tiles = {
            "|": {
                "south": [(i-1, j, "south")],
                "north": [(i+1, j, "north")],
                "east": [(i+1, j, "north"),(i-1, j, "south")],
                "west": [(i+1, j, "north"),(i-1, j, "south")]
            }, 
            "-": {
                "west": [(i, j+1, "west")],
                "east": [(i, j-1, "east")],
                "south": [(i, j+1, "west"),(i, j-1, "east")],
                "north": [(i, j+1, "west"),(i, j-1, "east")]
            }, 
            ".": {
                "west": [(i, j+1, "west")],
                "east": [(i, j-1, "east")],
                "south": [(i-1, j, "south")],
                "north": [(i+1, j, "north")]
            }, 
            "/": {
                "north": [(i, j-1, "east")],
                "west": [(i-1, j, "south")],
                "south": [(i, j+1, "west")],
                "east": [(i+1, j, "north")]
            }, 
            "\\": {
                "south": [(i, j-1, "east")],
                "west": [(i+1, j, "north")],
                "north": [(i, j+1, "west")],
                "east": [(i-1, j, "south")]
            }, 
        }
    for tile in tiles[map[i][j]][dir]:
        if tile[0] >= 0 and tile[0] < len(map) and tile[1] >= 0 and tile[1] < len(map[0]):
            visiting_queue.append(tile)

print("Number of tiles energized:", sum(sum(1 for tile in line if tile != []) for line in energized))