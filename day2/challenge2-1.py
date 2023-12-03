sum = 0

max = {
    "green": 13,
    "blue": 14,
    "red": 12
}

with open('day2/challenge2.txt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        line = line.replace(":", " :").replace(",", " ,").replace(";", "").split()
        line.append(";")
        i = 0
        while i < len(line):
            if line[i] == "Game":
                game_num = int(line[i+1])
                i += 1
            elif line[i].isnumeric():
                if int(line[i]) > max[line[i+1]]:
                    break
                i += 1
            elif line[i] == ";":
                sum += game_num
            i += 1

print("Sum of possible games: ", sum)